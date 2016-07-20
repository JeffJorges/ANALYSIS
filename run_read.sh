#!/bin/bash
module load python
#START=$(date +%s.%N)

I=$1
while [ $I -lt $(($2+1)) ]; do
    #$BASE 'echo "%d" $I'
    $BASE `printf "python plot_snapshot.py %d -dAGG" $I`
    I=$(($I+1))
done

#END=$(date +%s.%N)
#DIFF=$((END - START))
#echo $BASE '"%d" $DIFF'