#!/usr/bin/env python
# coding: utf-8

# In[4]:


pip install folium


# In[8]:


import folium
from folium.plugins import MiniMap

# Create a map centered on Montreal
montreal_coords = [45.5017, -73.5673]
map_montreal = folium.Map(location=montreal_coords, zoom_start=12, tiles="Stamen Terrain", 
                          attr="Map tiles by Stamen Design, under CC BY 3.0. Data by OpenStreetMap, under ODbL.")

# Add a marker for Mount Royal with a custom icon and popup with an image
mount_royal_coords = [45.5049, -73.5874]
mount_royal_popup = folium.Popup('<b>Mount Royal</b><br><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Mount_Royal_Montreal.jpg/250px-Mount_Royal_Montreal.jpg" width="150px">', max_width=250)
folium.Marker(
    mount_royal_coords, 
    popup=mount_royal_popup,
    icon=folium.Icon(color="green", icon="info-sign"),
).add_to(map_montreal)

# Add a circle marker for Old Montreal with reduced opacity
old_montreal_coords = [45.5081, -73.5540]
folium.CircleMarker(
    old_montreal_coords,
    radius=30,
    popup="Old Montreal",
    color="blue",
    fill=True,
    fill_opacity=0.4,
    fill_color="blue",
).add_to(map_montreal)

# Add McGill University with a custom icon and popup with an image
mcgill_coords = [45.5048, -73.5772]
mcgill_popup = folium.Popup('<b>McGill University</b><br><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/McGill_University_Montreal.JPG/250px-McGill_University_Montreal.JPG" width="150px">', max_width=250)
folium.Marker(
    mcgill_coords,
    popup=mcgill_popup,
    icon=folium.Icon(color="red", icon="university"),
).add_to(map_montreal)

# Add Olympic Stadium with a custom icon and popup with an image
olympic_stadium_coords = [45.5597, -73.5517]
olympic_popup = folium.Popup('<b>Olympic Stadium</b><br><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/7a/Stade_olympique.JPG/250px-Stade_olympique.JPG" width="150px">', max_width=250)
folium.Marker(
    olympic_stadium_coords,
    popup=olympic_popup,
    icon=folium.Icon(color="orange", icon="flag"),
).add_to(map_montreal)

# Add additional layers with proper attributions
folium.TileLayer('CartoDB positron').add_to(map_montreal)
folium.TileLayer('Stamen Toner', attr="Map tiles by Stamen Design, under CC BY 3.0. Data by OpenStreetMap, under ODbL.").add_to(map_montreal)
folium.TileLayer('Stamen Watercolor', attr="Map tiles by Stamen Design, under CC BY 3.0. Data by OpenStreetMap, under ODbL.").add_to(map_montreal)
folium.TileLayer('openstreetmap').add_to(map_montreal)

# Add a minimap to the map
minimap = MiniMap(toggle_display=True)
map_montreal.add_child(minimap)

# Layer control to toggle between tile sets
folium.LayerControl().add_to(map_montreal)

# Save the map to an HTML file
map_montreal.save("montreal_map.html")

# Display the map (if running in a Jupyter notebook or similar environment)
map_montreal


# In[ ]:




