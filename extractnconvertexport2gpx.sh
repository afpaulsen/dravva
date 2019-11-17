#!/bin/bash
echo "Running $0"

echo "Unzipping export"
unzip -q export.zip -d export
cd export/activities

for filename in *.gz; do
	[ -e "$filename" ] || continue
	echo "Unzipping $filename"
    gunzip --quiet $filename
done

for filename in *.fit; do
	[ -e "$filename" ] || continue
	echo "Converting $filename to gpx"
    gpsbabel -i garmin_fit -f $filename -o gpx -F $filename.gpx
	rm $filename
done

