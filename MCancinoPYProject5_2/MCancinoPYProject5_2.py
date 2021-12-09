import folium
import webbrowser

map1 = folium.Map(location=[31.637, -97.083], zoom_start =12)
folium.CircleMarker(location=[31.637, -97.083], radius =500, popup="WACO").add_to(map1)
folium.Marker([33.577, -101.858], popup="Lubbock").add_to(map1)
folium.Marker([31.637, -97.083], popup="TSTC at Waco").add_to(map1)
folium.Marker([30.274, -97.740], popup="Capitol Building").add_to(map1)
folium.Marker([26.220, -97.666], popup="TSTC at Harlingen").add_to(map1)

folium.PolyLine(locations = [(31.637, -97.083), (33.577, -101.858), (30.274, -97.740), (26.220, -97.666)], line_opacity = .6).add_to(map1)

map1.save("Waco.html")
#open in browser
webbrowser.open("Waco.html")