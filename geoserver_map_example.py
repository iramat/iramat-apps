import folium
from owslib.fes import BBox
from owslib.wfs import WebFeatureService
import requests
import os

IN_DIR = os.path.dirname(os.path.realpath(__file__))
OUT_MAP = os.path.join(IN_DIR, "wfs_map.html")

# GeoServer WFS endpoint
wfs_url = "https://iramat-apps.cnrs.fr/geoserver/ows?acceptversions=2.0.0"

# Create a folium map with Google Satellite basemap
def create_map_with_google_satellite():
    # Initialize the map with a default location (will be updated later)
    m = folium.Map(location=[0, 0], zoom_start=2, tiles=None)

    # Add Google Satellite tiles (requires internet connection)
    google_sat = folium.TileLayer(
        tiles='https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}',
        attr='Google Satellite',
        name='Google Satellite',
        overlay=False,
        control=True
    ).add_to(m)

    return m

# Fetch WFS data and get its bounding box
def get_wfs_bbox(wfs_url, typename):
    wfs = WebFeatureService(wfs_url, version='2.0.0')
    # Get the first layer name if typename is not provided
    if not typename:
        layers = list(wfs.contents)
        if not layers:
            raise ValueError("No layers found in WFS.")
        typename = layers[0]
    # Get the bounding box of the layer
    bbox = wfs.contents[typename].boundingBox
    return bbox, typename

# Add WFS layer to the map using GeoJSON
def add_wfs_layer(m, wfs_url, typename, bbox):
    # Construct WFS request URL
    wfs_request = (
        f"{wfs_url}&service=WFS&version=2.0.0&request=GetFeature"
        f"&typeNames={typename}&outputFormat=application/json"
        f"&bbox={bbox[0]},{bbox[1]},{bbox[2]},{bbox[3]},urn:ogc:def:crs:EPSG::4326"
    )

    # Fetch GeoJSON data
    response = requests.get(wfs_request)
    geojson_data = response.json()

    # Add GeoJSON to the map
    folium.GeoJson(
        geojson_data,
        name=typename
    ).add_to(m)

    # Fit the map to the bounding box
    m.fit_bounds([[bbox[1], bbox[0]], [bbox[3], bbox[2]]])

# Main script
if __name__ == "__main__":
    # Create the map
    m = create_map_with_google_satellite()

    # Get the WFS bounding box and layer name
    try:
        bbox, typename = get_wfs_bbox(wfs_url, typename=None)
        print(f"Using layer: {typename}")
    except Exception as e:
        print(f"Error fetching WFS data: {e}")
        exit(1)

    # Add WFS layer and fit the map
    add_wfs_layer(m, wfs_url, typename, bbox)

    # Add layer control
    folium.LayerControl().add_to(m)

    # Save the map   
    m.save(OUT_MAP)
    print(f"Map saved as '{OUT_MAP}'")