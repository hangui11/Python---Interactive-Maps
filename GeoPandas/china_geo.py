import geopandas
import webbrowser
import matplotlib.pyplot as plt
import os

gdf = geopandas.read_file('./cn.json')
if gdf.crs == 'EPSG:4326':
    gdf = gdf.to_crs('EPSG:3857')
gdf["area"] = gdf.area

# the coordinate (x, y) where x = longitude and y = latitude
b = gdf.plot("area", legend=True)
plt.savefig('china_geo.jpg')

a = gdf.explore("area", legend=False)
a.save('china_geo.html')

webbrowser.open('file://' + os.path.realpath('china_geo.html'))