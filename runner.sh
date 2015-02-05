 for file in ./morph/raw/*.phy;  
 do  
 var=$(head -1 $file | cut -d " " -f2);  
 nu=$(grep -Eo '[0-9]{1,4}' ./morph/partition_finder.cfg | cut -d "-" -f2); 
 echo $nu 
 echo $var; 
 sed -i "s/$nu/$var/g" ./morph/partition_finder.cfg;  
 cp $file ./morph/file.phy;  
 python PartitionFinderMorphology.py morph/ --cmdline-extras=' --asc-corr=lewis' --force
cp ./morph/analysis/start_tree/RAxML_result.BLTREE ./$file.start.tree
 cp ./morph/analysis/best_scheme.txt ./$file.best
 done
