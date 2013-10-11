#!/bin/python

#Code that does "topological_sort" of DAG using Depth_First_Search Algorithm.

#graph is represented as "adjacency-list"
#NOTE: the graph is DAG(Directed Acyclic Graph)
graph={}

#another parallel-dictionary for storing the meta-data of the nodes of the graph
meta_data_graph={}

stack=[]
timer=0
#for given i/p "current_node", it goes deeper and deeper, travelling the graph.   
def go_deeper(current_node):
    global graph, meta_data_graph, stack, timer

    neighbour_nodes=graph[current_node]
    len_of_list=len(neighbour_nodes)
    i=0

    while i<len_of_list :
        if( meta_data_graph[neighbour_nodes[i]]['discovery_time'] is None):
            stack.append(neighbour_nodes[i])
            timer=timer+1
            meta_data_graph[neighbour_nodes[i]].update({'discovery_time':timer})

            neighbour_nodes=graph[neighbour_nodes[i]]
            len_of_list=len(neighbour_nodes)
            i=0
        else :
            i=i+1
    
#for given i/p "popped_node", return 0 if the node has 0 unvisited neighbour nodes, else return the unvisited neighbour node.  
def has_unvisited_neighbours(popped_node):
    for neighbour_nodes in graph[popped_node]:
        if( meta_data_graph[neighbour_nodes]['discovery_time'] is None):
            return neighbour_nodes
       
    return 0;
       
def depth_first_search():
    global graph, meta_data_graph, stack, timer
   
    #for every node, add 2 extra attributes as "meta-data"
    for nodes in graph.keys() :
        meta_data_graph[nodes]={'discovery_time':None, 'finished_time':None}
       
    #any random node selected to start with
    current_node=1
   
    if ( meta_data_graph[current_node]['discovery_time'] is None ) :
        timer=timer+1
        meta_data_graph[current_node].update({'discovery_time':timer})
        stack.append(current_node)
   
    go_deeper(current_node);
           
    #reached the deepest point in graph, so start the back-track
    #for first pop, no need to do any checking
    while stack :
	#Print the element from the stack that is to be popped.
	#Insert it in the left-most position of the linked list.
	print stack[-1]

        popped_node=stack.pop()
        timer=timer+1
        meta_data_graph[popped_node]['finished_time']=timer
    
        #we don't pop last element immediately, we confirm if its "poppable" !   
        if ( stack ) :
            popped_node=stack[-1]

        current_node=has_unvisited_neighbours(popped_node)
        if ( current_node ):
            #put current_node in stack
            timer=timer+1
            meta_data_graph[current_node].update({'discovery_time':timer})
            stack.append(current_node)
       
            go_deeper(current_node);
       
def topological_sort():
    depth_first_search()
    #we can use meta_data_graph of above function to get the topological_sort.( which I haven't used )
    #In the topological_sort,from left-to-right, the nodes are descendingly arranged wrt to their "discovery_time"
    print meta_data_graph
   
def add_node(node, node_neighbours ):
    global graph
    graph[node]=node_neighbours
 
def main():
    add_node(1, [2,6,8] )
    add_node(2, [4] )
    add_node(3, [2,5,7] )
    add_node(4, [] )
    add_node(5, [] )
    add_node(6, [4] )
    add_node(7, [6] )
    add_node(8, [7] )
       
    topological_sort()
 
main()

