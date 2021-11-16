'''
Python para conexões de ruas
Módulo Python para recuperar, modelar, analisar e visualizar redes de ruas e outros dados geoespaciais do OSM
'''
import osmnx as ox 
import networkx as nx 
import seaborn as sns
import matplotlib.pyplot as plt
import geopandas as gp
import scipy as sp

ox.config(use_cache=True, log_console=False)

place = "Viçosa, Brazil"
graph = ox.graph_from_place(place, network_type="drive")
nx.draw(graph, node_color='green', node_size=10)
plt.show()

'''
fig, ax = ox.plot_graph(graph)
'''
'''
#Exporta um shapefile com os nós e arestas
ox.save_graph_shapefile(graph, filepath="networkx-shape-Vicosa")
'''
'''
nodes, streets = ox.graph_to_gdfs(graph)
#Quantidade de ruas da cidade
print(len(streets))
print(streets.head().geometry)
'''
'''
buildings = ox.geometries_from_place("Viçosa, Brazil", tags={'building':True})
ox.plot_footprints(buildings)
'''
