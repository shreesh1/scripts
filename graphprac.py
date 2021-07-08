import networkx as nx
import matplotlib.pyplot as plt
from pyvis.network import Network
import sys

if(len(sys.argv)!=2):
	print("usage: python3 graphprac.py (1|2)")
	exit(0)

g=nx.Graph()
g.add_edge(1,5,color='r')
g.add_edge(2,3,color='r')
g.add_edge(2,4,color='r')
g.add_edge(6,7,color='r')
g.add_edge(6,8,color='r')
g.add_edge(6,9,color='r')
g.add_edge(6,10,color='r')
g.add_edge(11,12,color='r')
g.add_edge(13,14,color='r')
g.add_edge(13,15,color='r')
g.add_edge(16,17,color='r')
g.add_edge(18,19,color='r')
g.add_edge(20,21,color='r')
g.add_edge(1,3,color='b')
g.add_edge(1,4,color='b')
g.add_edge(1,5,color='b')
g.add_edge(1,7,color='b')
g.add_edge(1,8,color='b')
g.add_edge(1,9,color='b')
g.add_edge(1,10,color='b')
g.add_edge(1,12,color='b')
g.add_edge(1,14,color='b')
g.add_edge(1,15,color='b')
g.add_edge(1,17,color='b')
g.add_edge(1,19,color='b')
g.add_edge(1,21,color='b')


def staticgraph():
	d = dict(g.degree)
	edges = g.edges()
	colors = [g[u][v]['color'] for u,v in edges]
	plt.figure(5,figsize=(20,20))
	nx.draw(g,with_labels=True,node_color='lightblue',nodelist=d.keys(),node_size=[v * 100 for v in d.values()], edge_color=colors,font_size=8,font_color='black')
	plt.show()

def dynamicgraph():
	nt = Network(height='100%', width='100%', bgcolor='#FFFFFF', font_color='black')
	nt.from_nx(g)
	nt.show_buttons()
	nt.force_atlas_2based()
	nt.show('nx.html')


if((sys.argv[1])=='1'):
	staticgraph()
elif((sys.argv[1])=='2'):
	dynamicgraph()
else:
  print("usage: python3 graphprac.py (1|2)")
