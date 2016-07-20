#!/bin/bash
I=$1

echo "Conveting all Snapshots to 2D Images"
$BASE 'printf "~/pfs/runs/ANALYSIS/run_read.sh 0 %d" %I'
'printf "~/pfs/runs/ANALYSIS/mkvid.sh"'
