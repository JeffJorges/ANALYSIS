#!/bin/bash
clear

echo "Setting up enviroment for png->mp4 conversion."
rm -rf temp

echo "--Loading module"
module load ffmpeg

echo "--Making temp folders and coping files"
mkdir temp
cp *.png temp/

echo "--Resizing Images"
mogrify -resize 1200x1200 temp/*.png

echo "--Morphing Images Together"
convert temp/*.png -delay 10 -morph 10 temp/%05d.png

echo "--Stitching Images Into Video"
ffmpeg -r 25 -i temp/%05d.png output.mp4

echo "--Done."
rm -rf temp
