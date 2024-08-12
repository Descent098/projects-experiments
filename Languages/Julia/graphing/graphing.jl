using Graphs
using GraphPlot

my_graph = Graph(6) # Graph with 6 verticies

# Can also do adjacency matrices
add_edge!(my_graph, 1, 2)
add_edge!(my_graph, 1, 3)
add_edge!(my_graph, 1, 4)
add_edge!(my_graph, 1, 5)
add_edge!(my_graph, 1, 6)

add_edge!(my_graph, 4, 5)
add_edge!(my_graph, 4, 6)

# Setup the Graph
gplot(my_graph, nodelabel=1:6)




