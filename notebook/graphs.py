#!/usr/bin/python

def get_descendants(G, node, depth=1):
    try:
        if depth == 1:
            return G[node]
        else:
            children = G[node]
            if children:
                children = set.union(*[get_descendants(G, n, depth=depth-1) for n in children])
            return children
                
    except KeyError as e:
        print("The node {} is not in the graph".format(node)) 
        
def get_ancestors(G, node, depth=1):
    try:
        if depth == 1:
            return set([n for n in G if node in get_descendants(G, n, depth=1)])
        else:
            parents = get_ancestors(G, node)
            if parents:
                parents = set.union(*[get_ancestors(G, n, depth=depth-1) for n in parents])
            return parents
             
    except KeyError:
        print("The node {} is not in the graph".format(node)) 
                
def get_siblings(G, node):
    try:
        siblings = set.union(*[get_descendants(G, n) for n in get_ancestors(G, node)])
        return siblings - set(node)
    
    except KeyError:
        print("The node {} is not in the graph".format(node)) 
        
def distance(G, node1, node2):
    try:
        d = 0
        if node2 != node1:
            c = {node1}
            while c:
                d += 1
                c = set.union(*[G[n] for n in c])
                if node2 in c:
                    break
            else:
                d = float("+inf")
        return d
    
    except KeyError:
         print("The node {} is not in the graph".format(node))    
            
if __name__ == "__main__":
    G = {"1": {"2", "3", "4"}, "2": {"4", "5"}, "3": {"6"},
         "4": {"3", "6", "7"}, "5": {"4", "7"}, "6": set(), "7": {"6"}}
    print("Graph G loaded with nodes {}".format(G.keys()))
    node1 = input("Choose a node in G (integer value 1-7) : ")
    node2 = input("Choose a second node in G (integer value 1-7): ")
    
    print("\nThe distance in G from node {} to node {} is {}".format(node1, node2, distance(G, node1, node2)))