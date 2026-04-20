import os
import xml.etree.ElementTree as ET
from typing import Tuple

import folium
import requests


WMS_BASE_URL = "https://iramat-apps.cnrs.fr/geoserver/ows?version=1.3.0"
LAYER_NAME = "vialas:mne"

IN_DIR = os.path.dirname(os.path.realpath(__file__))
OUTPUT_HTML = os.path.join(IN_DIR, "geoserver_wms_map_example.html")


def get_wms_capabilities(base_url: str) -> bytes:
    params = {
        "service": "WMS",
        "request": "GetCapabilities",
        "version": "1.3.0",
    }
    response = requests.get(base_url, params=params, timeout=60)
    response.raise_for_status()
    return response.content


def parse_named_wms_layer_bbox(capabilities_xml: bytes, layer_name: str) -> Tuple[float, float, float, float]:
    """
    Returns:
        (minx, miny, maxx, maxy) in EPSG:4326
    """
    ns = {
        "wms": "http://www.opengis.net/wms",
    }

    root = ET.fromstring(capabilities_xml)

    for layer in root.findall(".//wms:Layer", ns):
        name_el = layer.find("wms:Name", ns)
        if name_el is None or name_el.text != layer_name:
            continue

        # Prefer EX_GeographicBoundingBox if available
        ex_bbox = layer.find("wms:EX_GeographicBoundingBox", ns)
        if ex_bbox is not None:
            west = ex_bbox.find("wms:westBoundLongitude", ns)
            east = ex_bbox.find("wms:eastBoundLongitude", ns)
            south = ex_bbox.find("wms:southBoundLatitude", ns)
            north = ex_bbox.find("wms:northBoundLatitude", ns)

            if all(el is not None and el.text for el in (west, east, south, north)):
                minx = float(west.text)
                maxx = float(east.text)
                miny = float(south.text)
                maxy = float(north.text)
                return (minx, miny, maxx, maxy)

        # Fallback: LatLonBoundingBox (older style)
        latlon_bbox = layer.find("wms:LatLonBoundingBox", ns)
        if latlon_bbox is not None:
            minx = float(latlon_bbox.attrib["minx"])
            miny = float(latlon_bbox.attrib["miny"])
            maxx = float(latlon_bbox.attrib["maxx"])
            maxy = float(latlon_bbox.attrib["maxy"])
            return (minx, miny, maxx, maxy)

        raise RuntimeError(f"Layer '{layer_name}' found, but no geographic bounding box was available.")

    raise RuntimeError(f"Layer '{layer_name}' not found in WMS GetCapabilities.")


def build_map(bbox: Tuple[float, float, float, float], wms_base_url: str, layer_name: str) -> folium.Map:
    minx, miny, maxx, maxy = bbox
    center_lat = (miny + maxy) / 2
    center_lon = (minx + maxx) / 2

    m = folium.Map(
        location=[center_lat, center_lon],
        zoom_start=12,
        tiles=None,
        control_scale=True,
    )

    folium.TileLayer(
        tiles="OpenStreetMap",
        name="OpenStreetMap",
        overlay=False,
        control=True,
    ).add_to(m)

    folium.WmsTileLayer(
        url=wms_base_url,
        name=layer_name,
        layers=layer_name,
        fmt="image/png",
        transparent=True,
        version="1.3.0",
        attr="GeoServer WMS",
        overlay=True,
        control=True,
    ).add_to(m)

    m.fit_bounds([[miny, minx], [maxy, maxx]])
    folium.LayerControl().add_to(m)

    return m


def main() -> None:
    capabilities_xml = get_wms_capabilities(WMS_BASE_URL)
    bbox = parse_named_wms_layer_bbox(capabilities_xml, LAYER_NAME)

    print(f"Using WMS layer: {LAYER_NAME}")
    print(f"WGS84 bounds: {bbox}")

    m = build_map(bbox, WMS_BASE_URL, LAYER_NAME)
    m.save(OUTPUT_HTML)

    print(f"Map saved to: {OUTPUT_HTML}")


if __name__ == "__main__":
    main()