#! /bin/bash
# untested

# downloads SD data
wget "https://zenodo.org/records/4487613/files/data.zip?download=1"
unzip data.zip -d ../data/temp/
rm -r data.zip
mv ../data/temp/data/dataSD1500/* ../data/raw/
mv ../data/temp/data/dataSD750/* ../data/raw/

# downloads summary
wget "https://zenodo.org/records/4487613/files/summary.zip?download=1"
unzip data.zip -d ../data/temp/
rm -r summary.zip
mv ../data/temp/dataSummary* ../data/raw/