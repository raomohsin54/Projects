import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

# Load the data
chart_data = pd.read_excel(r'C:\Users\mmukhtiar\Downloads\Updated_Traffic_Count.xlsx')

# Set page title and color
st.set_page_config(page_title="Traffic Count Analysis", page_icon="🚲", layout="wide", initial_sidebar_state="expanded")
st.markdown("<h1 style='text-align: center; color: #008000;'>Traffic Count Analysis</h1>", unsafe_allow_html=True)

# Show the data in a table
st.write("## Traffic Count Data")
st.write(chart_data)

# Map visualization using PyDeck
st.write("## Traffic Count Map Visualization")
st.pydeck_chart(pdk.Deck(
    map_style="mapbox://styles/mapbox/light-v9",
    initial_view_state=pdk.ViewState(
        latitude=-31.9667,
        longitude=115.8178,
        zoom=11,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
            "HexagonLayer",
            data=chart_data,
            get_position="[lon, lat]",
            radius=200,
            elevation_scale=4,
            elevation_range=[0, 1000],
            pickable=True,
            extruded=True,
            auto_highlight=True,
            tooltip={"html": "<b>Commute:</b> {commute}<br/><b>Count:</b> {Both}", "style": {"color": "white"}},
        ),
        pdk.Layer(
            "ScatterplotLayer",
            data=chart_data,
            get_position="[lon, lat]",
            get_color="[200, 30, 0, 160]",
            get_radius=200,
            auto_highlight=True,
            tooltip={"html": "<b>Commute:</b> {commute}<br/><b>Count:</b> {Both}", "style": {"color": "white"}},
        ),
    ],
))
