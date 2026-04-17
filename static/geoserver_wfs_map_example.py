# import folium
# from owslib.fes import BBox
# from owslib.wfs import WebFeatureService
# import requests
# import os

# IN_DIR = os.path.dirname(os.path.realpath(__file__))
# OUT_MAP = os.path.join(IN_DIR, "geoserver_wfs_map_example2.html")
import os
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Optional, Tuple

import folium
import requests


WFS_BASE_URL = "https://iramat-apps.cnrs.fr/geoserver/ows?acceptversions=2.0.0"
IN_DIR = os.path.dirname(os.path.realpath(__file__))
OUTPUT_HTML = os.path.join(IN_DIR, "geoserver_wfs_map_example.html")

# Optional: set this explicitly if you know the layer name, for example "workspace:sites"
LAYER_NAME: Optional[str] = None


def get_wfs_capabilities(base_url: str) -> bytes:
    params = {
        "service": "WFS",
        "request": "GetCapabilities",
        "acceptversions": "2.0.0",
    }
    response = requests.get(base_url, params=params, timeout=60)
    response.raise_for_status()
    return response.content


def parse_first_feature_type(capabilities_xml: bytes) -> Tuple[str, Tuple[float, float, float, float]]:
    """
    Returns:
        (feature_type_name, (minx, miny, maxx, maxy))
    """
    ns = {
        "wfs": "http://www.opengis.net/wfs/2.0",
        "ows": "http://www.opengis.net/ows/1.1",
    }

    root = ET.fromstring(capabilities_xml)
    feature_type = root.find(".//wfs:FeatureTypeList/wfs:FeatureType", ns)
    if feature_type is None:
        raise RuntimeError("No WFS FeatureType found in GetCapabilities.")

    name_el = feature_type.find("wfs:Name", ns)
    if name_el is None or not name_el.text:
        raise RuntimeError("FeatureType has no name.")

    bbox_el = feature_type.find("ows:WGS84BoundingBox", ns)
    if bbox_el is None:
        raise RuntimeError("FeatureType has no WGS84BoundingBox.")

    lower_el = bbox_el.find("ows:LowerCorner", ns)
    upper_el = bbox_el.find("ows:UpperCorner", ns)
    if lower_el is None or upper_el is None or not lower_el.text or not upper_el.text:
        raise RuntimeError("Invalid WGS84BoundingBox in GetCapabilities.")

    minx, miny = map(float, lower_el.text.split())
    maxx, maxy = map(float, upper_el.text.split())

    return name_el.text, (minx, miny, maxx, maxy)


def parse_named_feature_type(capabilities_xml: bytes, layer_name: str) -> Tuple[str, Tuple[float, float, float, float]]:
    ns = {
        "wfs": "http://www.opengis.net/wfs/2.0",
        "ows": "http://www.opengis.net/ows/1.1",
    }

    root = ET.fromstring(capabilities_xml)
    for feature_type in root.findall(".//wfs:FeatureTypeList/wfs:FeatureType", ns):
        name_el = feature_type.find("wfs:Name", ns)
        if name_el is None or name_el.text != layer_name:
            continue

        bbox_el = feature_type.find("ows:WGS84BoundingBox", ns)
        if bbox_el is None:
            raise RuntimeError(f"Layer '{layer_name}' has no WGS84BoundingBox.")

        lower_el = bbox_el.find("ows:LowerCorner", ns)
        upper_el = bbox_el.find("ows:UpperCorner", ns)
        if lower_el is None or upper_el is None or not lower_el.text or not upper_el.text:
            raise RuntimeError(f"Layer '{layer_name}' has an invalid WGS84BoundingBox.")

        minx, miny = map(float, lower_el.text.split())
        maxx, maxy = map(float, upper_el.text.split())
        return layer_name, (minx, miny, maxx, maxy)

    raise RuntimeError(f"Layer '{layer_name}' not found in GetCapabilities.")


def get_wfs_geojson(base_url: str, layer_name: str) -> dict:
    params = {
        "service": "WFS",
        "version": "2.0.0",
        "request": "GetFeature",
        "typeNames": layer_name,
        "outputFormat": "application/json",
        "srsName": "EPSG:4326",
    }
    response = requests.get(base_url, params=params, timeout=120)
    response.raise_for_status()
    return response.json()


def build_map(bbox: Tuple[float, float, float, float], geojson_data: dict, layer_name: str) -> folium.Map:
    minx, miny, maxx, maxy = bbox
    center_lat = (miny + maxy) / 2
    center_lon = (minx + maxx) / 2

    m = folium.Map(
        location=[center_lat, center_lon],
        zoom_start=8,
        tiles=None,
        control_scale=True,
    )

    # Google Satellite tiles. This is widely used but unofficial.
    folium.TileLayer(
        tiles="https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}",
        attr="Google",
        name="Google Satellite",
        overlay=False,
        control=True,
    ).add_to(m)

    folium.GeoJson(
        geojson_data,
        name=layer_name,
        tooltip=folium.GeoJsonTooltip(fields=list(_safe_properties(geojson_data)), aliases=None),
    ).add_to(m)

    m.fit_bounds([[miny, minx], [maxy, maxx]])
    folium.LayerControl().add_to(m)
    return m


def _safe_properties(geojson_data: dict):
    features = geojson_data.get("features", [])
    if not features:
        return []
    return features[0].get("properties", {}).keys()


def main() -> None:
    capabilities_xml = get_wfs_capabilities(WFS_BASE_URL)

    if LAYER_NAME:
        layer_name, bbox = parse_named_feature_type(capabilities_xml, LAYER_NAME)
    else:
        layer_name, bbox = parse_first_feature_type(capabilities_xml)

    print(f"Using WFS layer: {layer_name}")
    print(f"WGS84 bounds: {bbox}")

    geojson_data = get_wfs_geojson(WFS_BASE_URL, layer_name)
    m = build_map(bbox, geojson_data, layer_name)
    m.save(str(OUTPUT_HTML))

    # print(f"Map saved to: {OUTPUT_HTML.resolve()}")
    print(f"Map saved to: {OUTPUT_HTML}")


if __name__ == "__main__":
    main()
    # # Save the map   
    # m.save(OUT_MAP)
    # print(f"Map saved as '{OUT_MAP}'")