import gpxpy
import gpxpy.gpx
import folium
from time import localtime, strftime
import glob
import os

print ("Running " + __file__)

#my_map = folium.Map( zoom_start=14,tiles='http://tile.stamen.com/toner-background/{z}/{x}/{y}.png',attr="<a href=http://maps.stamen.com/>Stamen</a>")
my_map = folium.Map( zoom_start=14,tiles='http://tile.stamen.com/watercolor/{z}/{x}/{y}.png',attr="<a href=http://maps.stamen.com/>Stamen</a>")

for filename in glob.glob(os.getcwd() + '/export/activities/*.gpx'):
	print("Reading " + filename)
	gpx_file = open(filename, 'r')
	gpx = gpxpy.parse(gpx_file)

	try:
		time = gpx.tracks[0].segments[0].points[0].time
	except (IndexError, KeyError) as e:
		time = "N/A"

	points = []
	for track in gpx.tracks:
		for segment in track.segments:        
			for point in segment.points:
				points.append(tuple([point.latitude, point.longitude]))
	if points:
		folium.PolyLine(points, color="purple", weight=1.5, opacity=0.4).add_to(my_map) #Removed: tooltip=filename
		print("Added " + str(len(points)) + " points, starting at " + time.strftime('%d/%m/%Y %H:%M:%S'))
	else:
		print("Ignored file with no points")

		

# Save map
mapname = "maps/" + strftime("%Y_%m_%d_%H_%M_%S", localtime()) + ".html"
my_map.save(mapname)

print("Saved map to " + mapname)