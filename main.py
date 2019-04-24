# -*- coding: utf-8 -*-
import random
import networkx as nx

# Type of Argument
argument = ["in", "out", "undec"]
# Generate a random attack!
attacker = random.choice(argument)

# Argument is IN, OUT or UNDECIDED function
def check_arugment(af,argument):
    for (attacker,_) in af.in_edges(argument):
        if af[attacker][labelling]=="in":
            return "out"
        elif af[attacker][labelling]=="undec":
            return "in"
        else:
            return "undec"

# Create sets from Graph!
def powerset( base_set ):
    """ modified from pydoc’s itertools recipe"""
    from itertools import chain, combinations
    base_list = list( base_set )
    combo_list = [ combinations(base_list, r) for r in range(len(base_set)+1) ]

    powerset = set([])
    for ll in combo_list:
        list_of_frozensets = list( map( frozenset, map( list, ll ) ) )
        set_of_frozensets = set( list_of_frozensets )
        powerset = powerset.union( set_of_frozensets )
    return powerset

def generateLabellings(args):
    output=[]
    for ina in powerset(args):
            for outa in powerset(args-ina):
                output.append([ina,outa,(args-ina)-outa])
    # Output = In, Out, Undecided
    return output

# Networkx produce Graph
G = nx.Graph()
# Networkx add nodes
G.add_nodes_from([1, 2, 3, 4, 5, 6])
G.add_edges_from([(1, 2), (3, 4), (5, 6)])
for x in (generateLabellings(G.nodes)):
    print(x)
