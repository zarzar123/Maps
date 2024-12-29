#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install geopandas folium matplotlib shapely requests


# In[2]:


import geopandas as gpd
import folium
import requests


# In[3]:


boroughs = gpd.read_file('/Users/zarrintasneem/Downloads/limites-administratives-agglomeration-nad83.geojson')
display(boroughs.head())


# In[4]:


import pandas as pd

light_displays = pd.read_csv('/Users/zarrintasneem/Documents/light_displays.csv')


# In[6]:


print(light_displays.isnull())


# In[7]:


print(light_displays[light_displays[['Latitude', 'Longitude']].isnull().any(axis=1)])


# In[8]:


# Drop rows with missing Latitude or Longitude
light_displays = light_displays.dropna(subset=['Latitude', 'Longitude'])

# Alternatively, fill missing values with a default value (e.g., city center)
light_displays['Latitude'] = light_displays['Latitude'].fillna(45.5017)
light_displays['Longitude'] = light_displays['Longitude'].fillna(-73.5673)


# In[10]:


print(light_displays[['Name', 'Latitude', 'Longitude', 'Description']])


# In[11]:


for _, row in light_displays.iterrows():
    print(f"Adding marker for {row['Name']} at {row['Latitude']}, {row['Longitude']}")
    folium.Marker(
        location=[row['Latitude'], row['Longitude']],
        popup=f"<b>{row['Name']}</b><br>{row['Description']}",
        icon=folium.Icon(color='red', icon='info-sign')
    ).add_to(map_montreal)


# In[12]:


folium.Marker(
    location=[45.5017, -73.5673],
    popup="Test Marker",
    icon=folium.Icon(color='blue', icon='info-sign')
).add_to(map_montreal)

map_montreal.save("test_map.html")
map_montreal


# In[13]:


import pandas as pd
import folium

# Load data
light_displays = pd.read_csv('/Users/zarrintasneem/Documents/light_displays.csv')

# Ensure Latitude and Longitude are numeric
light_displays['Latitude'] = pd.to_numeric(light_displays['Latitude'], errors='coerce')
light_displays['Longitude'] = pd.to_numeric(light_displays['Longitude'], errors='coerce')

# Drop rows with missing or invalid coordinates
light_displays = light_displays.dropna(subset=['Latitude', 'Longitude'])

# Create the map
map_montreal = folium.Map(location=[45.5017, -73.5673], zoom_start=12)

# Add markers
for _, row in light_displays.iterrows():
    folium.Marker(
        location=[row['Latitude'], row['Longitude']],
        popup=f"<b>{row['Name']}</b><br>{row['Description']}",
        icon=folium.Icon(color='red', icon='info-sign')
    ).add_to(map_montreal)

# Save and display
map_montreal.save("montreal_light_displays.html")
map_montreal


# In[14]:


pip install keplergl


# In[16]:


pip install pydeck


# In[17]:





# In[19]:


import pandas as pd
import folium
from folium.plugins import BeautifyIcon

# Load data
light_displays = pd.read_csv('/Users/zarrintasneem/Documents/light_displays.csv')

# Ensure Latitude and Longitude are numeric
light_displays['Latitude'] = pd.to_numeric(light_displays['Latitude'], errors='coerce')
light_displays['Longitude'] = pd.to_numeric(light_displays['Longitude'], errors='coerce')

# Drop rows with missing or invalid coordinates
light_displays = light_displays.dropna(subset=['Latitude', 'Longitude'])

# Create a Christmas-themed map with a dark base
map_montreal = folium.Map(location=[45.5017, -73.5673], zoom_start=12, tiles='CartoDB dark_matter')

# Add Christmas-themed markers
for _, row in light_displays.iterrows():
    folium.Marker(
        location=[row['Latitude'], row['Longitude']],
        popup=folium.Popup(
            html=f"""
            <h3 style="color:red;">{row['Name']}</h3>
            <p>{row['Description']}</p>
            """,
            max_width=300
        ),
        icon=BeautifyIcon(
            icon="star",
            icon_shape="marker",
            border_color="gold",
            border_width=3,
            text_color="red",
            background_color="green",
            spin=True  # Adds a spinning effect
        )
    ).add_to(map_montreal)

# Add a snowflake overlay (optional feature)
folium.Marker(
    location=[45.5017, -73.5673],  # Center point
    icon=BeautifyIcon(
        icon="snowflake",
        icon_shape="circle",
        border_color="white",
        background_color="blue",
        text_color="white",
        border_width=2,
    ),
    popup="Merry Christmas!"
).add_to(map_montreal)

# Save and display
map_montreal.save("montreal_christmas_light_displays.html")
map_montreal


# In[20]:


import pandas as pd
import folium
from folium.plugins import BeautifyIcon

# Load data
light_displays = pd.read_csv('/Users/zarrintasneem/Documents/light_displays.csv')

# Ensure Latitude and Longitude are numeric
light_displays['Latitude'] = pd.to_numeric(light_displays['Latitude'], errors='coerce')
light_displays['Longitude'] = pd.to_numeric(light_displays['Longitude'], errors='coerce')

# Drop rows with missing or invalid coordinates
light_displays = light_displays.dropna(subset=['Latitude', 'Longitude'])

# Create a Christmas-themed map with a dark base
map_montreal = folium.Map(location=[45.5017, -73.5673], zoom_start=12, tiles='CartoDB dark_matter')

# Add custom Christmas-themed markers
for _, row in light_displays.iterrows():
    icon_html = f"""
    <div style="
        background-color:rgba(0,0,0,0.6);
        color:white;
        border-radius:50%;
        width:32px;
        height:32px;
        text-align:center;
        font-size:18px;
        line-height:32px;
        box-shadow:0 0 15px gold;">
        🎄
    </div>
    """
    folium.Marker(
        location=[row['Latitude'], row['Longitude']],
        popup=folium.Popup(
            html=f"""
            <h3 style="color:red; text-shadow: 2px 2px black;">{row['Name']}</h3>
            <p>{row['Description']}</p>
            """,
            max_width=300
        ),
        icon=folium.DivIcon(html=icon_html)
    ).add_to(map_montreal)

# Add animated snowfall using custom JavaScript
snowfall_js = """
L.DomUtil.addClass(document.body, 'snowfall');
"""

snowfall_css = """
<style>
@keyframes snow {
  0% { transform: translateY(0); }
  100% { transform: translateY(100vh); }
}

.snowfall {
  position: relative;
  overflow: hidden;
}

.snowfall:before, .snowfall:after {
  content: '';
  position: absolute;
  top: -50px;
  width: 100%;
  height: 100vh;
  background-image: radial-gradient(white 0.7px, transparent 1px);
  background-size: 1.5vw 1.5vw;
  animation: snow 8s linear infinite;
}

.snowfall:after {
  background-size: 1vw 1vw;
  animation: snow 12s linear infinite;
}
</style>
"""

map_montreal.get_root().html.add_child(folium.Element(snowfall_css))
map_montreal.get_root().script.add_child(folium.Element(snowfall_js))

# Save and display the map
map_montreal.save("montreal_christmas_light_displays_with_snow.html")
map_montreal


# In[21]:


import folium
from folium.plugins import MarkerCluster
import time

# Define Santa's journey: a list of coordinates (latitude, longitude) and city names
santa_journey = [
    {"city": "North Pole", "coordinates": [90, 0]},
    {"city": "New York, USA", "coordinates": [40.7128, -74.0060]},
    {"city": "London, UK", "coordinates": [51.5074, -0.1278]},
    {"city": "Paris, France", "coordinates": [48.8566, 2.3522]},
    {"city": "Tokyo, Japan", "coordinates": [35.6895, 139.6917]},
    {"city": "Sydney, Australia", "coordinates": [-33.8688, 151.2093]},
    {"city": "Cape Town, South Africa", "coordinates": [-33.9249, 18.4241]},
    {"city": "Buenos Aires, Argentina", "coordinates": [-34.6037, -58.3816]},
    {"city": "Montreal, Canada", "coordinates": [45.5017, -73.5673]}
]

# Create a base map centered on the North Pole
santa_map = folium.Map(location=[60, 0], zoom_start=2, tiles="CartoDB dark_matter")

# Add a cluster to track Santa's visited locations
marker_cluster = MarkerCluster().add_to(santa_map)

# Simulate Santa's journey
for stop in santa_journey:
    # Extract city name and coordinates
    city = stop["city"]
    lat, lon = stop["coordinates"]
    
    # Add a marker for Santa's current location
    folium.Marker(
        location=[lat, lon],
        popup=f"<b>Santa is in {city}!</b>",
        icon=folium.Icon(color='red', icon='gift')
    ).add_to(marker_cluster)
    
    # Add a circle representing Santa's magic presence
    folium.CircleMarker(
        location=[lat, lon],
        radius=10,
        color="gold",
        fill=True,
        fill_color="gold",
        fill_opacity=0.5
    ).add_to(santa_map)
    
    # Save the map after each stop
    santa_map.save("santa_tracker.html")
    
    # Simulate Santa traveling for 2 seconds (adjust as needed)
    print(f"Santa is visiting {city}!")
    time.sleep(2)

# Display the final map
santa_map


# In[22]:


import folium
from folium.plugins import MarkerCluster
import time
from IPython.display import display, clear_output

# Define Santa's journey: a list of coordinates (latitude, longitude) and city names
santa_journey = [
    {"city": "North Pole", "coordinates": [90, 0]},
    {"city": "New York, USA", "coordinates": [40.7128, -74.0060]},
    {"city": "London, UK", "coordinates": [51.5074, -0.1278]},
    {"city": "Paris, France", "coordinates": [48.8566, 2.3522]},
    {"city": "Tokyo, Japan", "coordinates": [35.6895, 139.6917]},
    {"city": "Sydney, Australia", "coordinates": [-33.8688, 151.2093]},
    {"city": "Cape Town, South Africa", "coordinates": [-33.9249, 18.4241]},
    {"city": "Buenos Aires, Argentina", "coordinates": [-34.6037, -58.3816]},
    {"city": "Montreal, Canada", "coordinates": [45.5017, -73.5673]}
]

# Create a base map centered on the North Pole
santa_map = folium.Map(location=[60, 0], zoom_start=2, tiles="CartoDB dark_matter")

# Add a cluster to track Santa's visited locations
marker_cluster = MarkerCluster().add_to(santa_map)

# Simulate Santa's journey
for i, stop in enumerate(santa_journey):
    # Extract city name and coordinates
    city = stop["city"]
    lat, lon = stop["coordinates"]

    # Add a marker for Santa's current location
    folium.Marker(
        location=[lat, lon],
        popup=f"<b>Santa is in {city}!</b>",
        icon=folium.Icon(color='red', icon='gift')
    ).add_to(marker_cluster)
    
    # Add a circle representing Santa's magic presence
    folium.CircleMarker(
        location=[lat, lon],
        radius=10,
        color="gold",
        fill=True,
        fill_color="gold",
        fill_opacity=0.5
    ).add_to(santa_map)
    
    # Add a polyline to show the path from the previous location
    if i > 0:
        prev_lat, prev_lon = santa_journey[i - 1]["coordinates"]
        folium.PolyLine(
            [[prev_lat, prev_lon], [lat, lon]],
            color="red",
            weight=2.5,
            dash_array="5, 5"
        ).add_to(santa_map)
    
    # Update and display the map in Jupyter Notebook
    santa_map.save("santa_tracker.html")
    clear_output(wait=True)
    display(santa_map)
    
    # Simulate Santa traveling for 2 seconds
    print(f"Santa is visiting {city}!")
    time.sleep(2)

# Save the final map to an HTML file
santa_map.save("santa_tracker_final.html")
print("Santa's journey is complete! Check out santa_tracker_final.html")


# In[25]:





# In[24]:


import os
print(os.getcwd())


# In[34]:


import folium
from IPython.display import display, clear_output
import time

# Define Santa's journey: a list of coordinates (latitude, longitude) and city names
santa_journey = [
    {"city": "North Pole", "coordinates": [90, 0]},
    {"city": "New York, USA", "coordinates": [40.7128, -74.0060]},
    {"city": "London, UK", "coordinates": [51.5074, -0.1278]},
    {"city": "Paris, France", "coordinates": [48.8566, 2.3522]},
    {"city": "Tokyo, Japan", "coordinates": [35.6895, 139.6917]},
    {"city": "Sydney, Australia", "coordinates": [-33.8688, 151.2093]},
    {"city": "Cape Town, South Africa", "coordinates": [-33.9249, 18.4241]},
    {"city": "Buenos Aires, Argentina", "coordinates": [-34.6037, -58.3816]},
    {"city": "Montreal, Canada", "coordinates": [45.5017, -73.5673]}
]

# Create the base map centered at the North Pole
santa_map = folium.Map(location=[60, 0], zoom_start=2, tiles="CartoDB dark_matter")

# Add all the destination markers
for stop in santa_journey:
    folium.Marker(
        location=stop["coordinates"],
        popup=f"<b>Santa visits {stop['city']}!</b>",
        icon=folium.Icon(color="red", icon="santa_clause")
    ).add_to(santa_map)

# Simulate Santa's movement with a moving marker
santa_icon_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Christmas_tradition.svg/1200px-Christmas_tradition.svg.png"

# Add the moving Santa marker
santa_marker = folium.Marker(
    location=santa_journey[0]["coordinates"],
    icon=folium.CustomIcon(santa_icon_url, icon_size=(50, 50))
)
santa_marker.add_to(santa_map)

# Save the map
santa_map.save("santa_tracker.html")

# Display and update Santa's journey in the notebook
for i, stop in enumerate(santa_journey):
    clear_output(wait=True)  # Clear the notebook cell output
    santa_marker.location = stop["coordinates"]  # Update Santa's location
    santa_map.save("santa_tracker.html")  # Save the updated map
    
    display(santa_map)  # Display the map in the notebook
    print(f"Santa is now in {stop['city']}!")  # Print Santa's current location
    time.sleep(2)  # Pause for 2 seconds to simulate movement

print("Santa has completed his journey!")


# In[ ]:





# In[ ]:




