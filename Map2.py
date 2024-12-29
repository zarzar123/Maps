#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install folium


# In[4]:


pip install urllib3==1.26.16


# In[5]:


import folium

# Create a map centered around a specific location (e.g., downtown San Francisco)
map_center = [37.7749, -122.4194]  # Latitude and longitude for San Francisco
map = folium.Map(location=map_center, zoom_start=13)

# Add a marker for a point of interest (e.g., City Hall)
folium.Marker(
    [37.7793, -122.4192], 
    popup='San Francisco City Hall',
    tooltip='Click for more info'
).add_to(map)

# Add a Circle marker for a park (Golden Gate Park)
folium.CircleMarker(
    location=[37.7694, -122.4862],
    radius=50,
    popup='Golden Gate Park',
    color='green',
    fill=True,
    fill_color='green'
).add_to(map)

# Add a marker for a public transportation station (e.g., BART station)
folium.Marker(
    [37.7837, -122.4089], 
    popup='Powell Street BART Station',
    tooltip='Click for more info',
    icon=folium.Icon(color='blue', icon='info-sign')
).add_to(map)

# Add another Circle marker for another park (Mission Dolores Park)
folium.CircleMarker(
    location=[37.7596, -122.4269],
    radius=50,
    popup='Mission Dolores Park',
    color='purple',
    fill=True,
    fill_color='purple'
).add_to(map)

# Show the map
map


# In[ ]:




