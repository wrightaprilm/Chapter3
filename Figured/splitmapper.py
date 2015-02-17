#Usage: python splitmapper.py <path to one set of trees> <path to the other> <name of dataframe to write out>

import dendropy
import sys
import pandas as pd

o_file = sys.argv[1]
i_file = sys.argv[2]
df_name = sys.argv[3]

files = [file for file in glob.glob("%s/*" % o_file)]
files1 = [file for file in glob.glob("%s/*" % i_file)]


trees = []
trees1 = []
split1 = [os.path.split(file)[1] for file in files]
split2 = [os.path.split(file)[1] for file in files1]

tree3 = []
tree2 = []

for file in split1:
        if file in split2:
                tree1 = dendropy.Tree.get_from_path('%s%s.nex.t.final' % (o_file,file), 'nexus')
                tree3.append(tree1)
                tree1 = dendropy.Tree.get_from_path('%s%s.con.tre' % (i_file,file), 'nexus')
                tree2.append(tree1)

diffs = []
for tr, tr1 in zip(tree3,tree2):
     tr.encode_bipartitions()
     tr1.encode_bipartitions()
     for bp in tr.bipartition_edge_map:
         if bp in tr1.bipartition_edge_map:
            node = tr.bipartition_edge_map[bp].head_node
            node1 = tr1.bipartition_edge_map[bp].head_node
            if node.label:
                if node1.label:
                    diff = float(node.label) - float(node1.label)
                    diffs.append(diff) 
                
df_name = pd.DataFrame(diffs)
df_name.to_csv(df_name)

