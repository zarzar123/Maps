#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install folium


# In[2]:


import folium

# Create a map centered on Montreal
montreal_map = folium.Map(location=[45.5017, -73.5673], zoom_start=12)

# Add markers for various points of interest
poi = [
    {"name": "Mount Royal Park", "location": [45.5048, -73.5878]},
    {"name": "Old Port of Montreal", "location": [45.5043, -73.5540]},
    {"name": "Montreal Museum of Fine Arts", "location": [45.4984, -73.5792]},
    {"name": "Biodome", "location": [45.5607, -73.5510]},
    {"name": "Saint Joseph's Oratory", "location": [45.4911, -73.6187]}
]

# Add the POIs to the map
for place in poi:
    folium.Marker(place["location"], popup=place["name"]).add_to(montreal_map)

# Save the map to an HTML file
montreal_map.save("montreal_map.html")

# Display the map in the Jupyter Notebook (if applicable)
montreal_map


# In[ ]:




