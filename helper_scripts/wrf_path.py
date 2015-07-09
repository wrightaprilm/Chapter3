import dendropy
from dendropy import Tree, TaxonSet
from dendropy.utility.fileutils import find_files
import csv
import sys
import os
import pandas as pd
o_file = sys.argv[1]
i_file = sys.argv[2]
ilist = find_files(top='./unpart_b/', filename_filter='*.t.final')
olist = find_files(top='./bic_b/', filename_filter='*.t.final')
split1 = [os.path.split(file)[1] for file in ilist]
split2 = [os.path.split(file)[1] for file in olist]
print split2
comparable = [split for split in split1]
print comparable
rf = []
SD = []
p_n = []
tree3 = []
tree2 = []
shared_files = []
for file in split1:
        if file in split2:
                shared_files.append(file)
                print file
                tree1 = dendropy.Tree.get_from_path('%s%s' % ('./bic_b/',file), 'nexus', is_rooted=False)
                tree3.append(tree1)
                tree1 = dendropy.Tree.get_from_path('%s%s' % ('./unpart_b/',file), 'nexus', is_rooted=False)
                tree2.append(tree1)
RF = [tree1.symmetric_difference(tree) for tree1, tree in zip(tree3,tree2)]

junk = zip(shared_files, RF)
df = pd.DataFrame(junk)
print df
df.to_csv('c.csv')

