import pandas as pd
import streamlit as st
from streamlit_folium import folium_static
import folium
import plotly.express as px

url= "https://github.com/raomohsin54/Projects/blob/main/Traffic_Count.csv"

# Load the data
df = pd.read_csv(url)

# Add a selectbox to filter by year
years = sorted(df['Count_year'].unique())
selected_year = st.selectbox('Select year', years)

# Filter data by selected year
df_year = df[df['Count_year'] == selected_year]

# Create map
m = folium.Map(location=[df_year['LATITUDE'].mean(), df_year['LONGITUDE'].mean()], zoom_start=12)

# Add markers to map
for _, row in df_year.iterrows():
    popup_text = f"<b>Speed limit:</b> {row['SPEED_LIMIT']} mph<br><b>Direction bound:</b> {row['DIRECTION_BOUND']}<br><b>Percent heavy vehicles:</b> {row['PERCENT_HEAVY_VEHICLES']}%"
    marker = folium.Marker(location=[row["LATITUDE"], row["LONGITUDE"]], popup=popup_text, icon=folium.Icon(color='blue'))
    marker.add_to(m)

# Display map
folium_static(m)

# Display scatter plot
scatter_fig = px.scatter(df_year, x="LONGITUDE", y="LATITUDE", color="SPEED_LIMIT")
scatter_fig.update_traces(marker=dict(size=5, color='red'))
scatter_fig.update_layout(title='Traffic Count Locations', xaxis_title='Longitude', yaxis_title='Latitude')
st.plotly_chart(scatter_fig)

# Display histogram
hist_fig = px.histogram(df_year, x="SPEED_LIMIT")
hist_fig.update_traces(marker=dict(color='green'))
hist_fig.update_layout(title='Speed Limit Histogram', xaxis_title='Speed Limit', yaxis_title='Count')
st.plotly_chart(hist_fig)

# Display bar chart
bar_fig = px.bar(df_year, x="DIRECTION_BOUND", y="PERCENT_HEAVY_VEHICLES")
bar_fig.update_traces(marker=dict(color='purple'))
bar_fig.update_layout(title='Percent Heavy Vehicles by Direction Bound', xaxis_title='Direction Bound', yaxis_title='Percent Heavy Vehicles')
st.plotly_chart(bar_fig)


# Add custom CSS styles
style = """
<style>
body {
    font-size: 16px;
    line-height: 1.5;
    font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
}

h1, h2, h3 {
    font-weight: bold;
    margin-top: 2rem;
    margin-bottom: 1rem;
}

h1 {
    font-size: 2.5rem;
}

h2 {
    font-size: 2rem;
}

h3 {
    font-size: 1.5rem;
}

p {
    margin-bottom: 1rem;
}

.streamlit-table {
    font-size: 1rem;
}

.streamlit-selectbox {
    font-size: 1rem;
    padding: 0.25rem 0.5rem;
    background-color: #f2f2f2;
    border-radius: 4px;
    border: none;
    box-shadow: none;
}

.plotly-graph-div {
    font-size: 1rem;
}

.mapboxgl-ctrl {
    font-size: 1rem;
}

.mapboxgl-popup-content {
    font-size: 1rem;
}
</style>
"""

st.markdown(style, unsafe_allow_html=True)