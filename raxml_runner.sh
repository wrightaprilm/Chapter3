for file in *
do
../../programs/raxmlHPC-SSE3  -fa -s $file -m MULTIGAMMA -K MK -n $file -x 1234 -p 12354 -# 100 --asc-corr=lewis
done
