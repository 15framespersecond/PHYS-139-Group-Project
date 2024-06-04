#! /bin/bash
wget "https://zenodo.org/records/4487613/files/data.zip?download=1"
unzip data.zip -d ../data/temp/
rm -r data.zip
mv ../data/temp/data/dataSD1500/* ../data/raw/
mv ../data/temp/data/dataSD750/* ../data/raw/

# note untested