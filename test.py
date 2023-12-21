import osmnx as ox
from streetview import search_panoramas
from streetview import get_streetview
import networkx as nx


# create network from that bounding box
G_ori = ox.graph_from_bbox(north, south, east, west, network_type="walk")

G_ori.nodes



panos = search_panoramas(lat=45.46462348718231, lon=9.214696838590351)
first = panos[0]

get_streetview()

x_values = nx.get_node_attributes (Chicago, 'x')

graph_with_geometries = list(G_ori.edges (data=True))


ox.bearing.calculate_bearing(lat1, lng1, lat2, lng2)