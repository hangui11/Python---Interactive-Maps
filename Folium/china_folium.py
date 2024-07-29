import folium
import numpy as np
import os
import webbrowser

china_loc = np.array([35.861660, 104.195396])
beijing_loc = np.array([39.904202, 116.407394])
shanghai_loc = np.array([31.224361,121.469170])

map = folium.Map(location=china_loc, zoom_start=5)

center_loc = (beijing_loc+shanghai_loc)/2


angle1 = np.arctan2(beijing_loc[1] - center_loc[1], beijing_loc[0] - center_loc[0])
angle2 = np.arctan2(shanghai_loc[1] - center_loc[1], shanghai_loc[0] - center_loc[0])

radius = np.sqrt(sum(pow(beijing_loc-center_loc,2)))
# print(radius)

num_points = 1000
angles = np.linspace(angle2, angle1, num=num_points)
points = [ [center_loc[0] + radius * np.cos(angle), center_loc[1] + radius * np.sin(angle)] for angle in angles]

folium.Marker(
    location=beijing_loc,
    icon=folium.Icon(icon='info-sign'),
    popup='Beijing City',
    tooltip='Click Me !'
).add_to(map)

folium.Marker(
    location=shanghai_loc,
    icon=folium.Icon(icon='info-sign'),
    popup='Shanghai City',
    tooltip='Click Me !'
).add_to(map)



url = "https://leafletjs.com/examples/custom-icons/{}".format
icon_image = url("leaf-red.png")
shadow_image = url("leaf-shadow.png")

icon = folium.CustomIcon(
    icon_image,
    icon_size=(38, 95),
    icon_anchor=(22, 94),
    shadow_image=shadow_image,
    shadow_size=(50, 64),
    shadow_anchor=(4, 62),
    popup_anchor=(-3, -76),
)


folium.PolyLine(
    points,
    color='blue',
    weight=5,
    tooltip='trayectory'
).add_to(map)

folium.Marker(
    location=center_loc, icon=icon, popup="Center"
).add_to(map)



map.save('china.html')
webbrowser.open('file://' + os.path.realpath('china.html'))