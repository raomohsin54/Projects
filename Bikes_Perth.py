import os
import streamlit as st
import pandas as pd
import pydeck as pdk

# Set the Mapbox API key as an environment variable
os.environ["MAPBOX_API_KEY"] = "pk.eyJ1IjoicmFvbW9oc2luNTQiLCJhIjoiY2xnbjc4cWxhMDJuODNranZhd210bmxhaCJ9.xvSUDLm8omTRDcNzci2wUA"

# Read in the data
df = pd.read_excel(r"C:\Users\mmukhtiar\Downloads\Updated_Traffic_Count.xlsx")

# Convert latitude and longitude to floats
df["LATITUDE"] = df["LATITUDE"].astype(float)
df["LONGITUDE"] = df["LONGITUDE"].astype(float)

# Define the filter options
filter_options = df["BETWEEN_STREETS"].unique()
filter_options = ["All"] + list(filter_options)

# Create the filter widget
selected_filter = st.sidebar.selectbox("Filter by trip between streets", filter_options)

# Filter the data based on the selection
if selected_filter == "All":
    filtered_df = df
else:
    filtered_df = df[df["BETWEEN_STREETS"] == selected_filter]

# Define the initial view state of the map
view_state = pdk.ViewState(
    latitude=filtered_df["LATITUDE"].mean(),
    longitude=filtered_df["LONGITUDE"].mean(),
    zoom=10,
    pitch=0,
    bearing=0
)

# Define the color scale for commute
color_scale = {
    "Weekend": [0, 255, 0],
    "Mon to Sun": [255, 255, 0],
    "Mon to Fri": [255, 0, 0]
}

# Create the scatterplot layer to display the commute data
layer = pdk.Layer(
    "ScatterplotLayer",
    data=filtered_df,
    get_position=["LONGITUDE", "LATITUDE"],
    get_radius=100,
    get_fill_color=lambda row: color_scale.get(row["commute"], [255, 255, 255]),
    get_line_color=[0, 0, 0],
    pickable=True,
    auto_highlight=True,
    tooltip={"text": "{BETWEEN_STREETS}\nCommute: {Commute}\nTrips: {Both}"}
)

# Create the map and add the layer
r = pdk.Deck(
    map_style="mapbox://styles/mapbox/light-v9",
    initial_view_state=view_state,
    layers=[layer],
)

# Display the filter and the map in Streamlit
st.sidebar.markdown("# Traffic Data Filter")
st.sidebar.markdown("Select streets to filter by:")
st.sidebar.markdown("*(or select 'All' to see all data)*")
st.sidebar.markdown("---")
st.sidebar.write(selected_filter)
st.pydeck_chart(r)
