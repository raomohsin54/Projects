import pandas as pd
import streamlit as st
from streamlit_folium import folium_static
import folium
import plotly.express as px

# Load the data
df = pd.read_csv(r"C:\Users\mmukhtiar\Downloads\Traffic_Count.csv")

df['START_DATE'] = pd.to_datetime(df['START_DATE'])
df['MONTH'] = df['START_DATE'].dt.month
df = df.sort_values('MONTH')


# Set page title and layout
st.set_page_config(page_title="Perth Bike Data (2014 to 2019)", page_icon="🚲", layout="wide", initial_sidebar_state="auto")

# Add a selectbox to filter by year
years = sorted(df['Count_year'].unique())
selected_year = st.selectbox('Select year', years)

# Filter data by selected year
df_year = df[df['Count_year'] == selected_year]
df_year['MONTH_NAME'] = df_year['START_DATE'].dt.month_name()
df_year = df_year.sort_values(by='MONTH_NAME')


# Create a new column for daily_totals
df_year['daily_totals'] = df_year.groupby('START_DATE')['PRIMARY_KEY'].transform('count')

# Create map
m = folium.Map(location=[df_year['LATITUDE'].mean(), df_year['LONGITUDE'].mean()], zoom_start=12, tiles='CartoDB dark_matter')

# Add markers to map
for _, row in df_year.iterrows():
    popup_text = f"<b>Speed limit:</b> {row['SPEED_LIMIT']} mph<br><b>Direction bound:</b> {row['DIRECTION_BOUND']}<br><b>Percent heavy vehicles:</b> {row['PERCENT_HEAVY_VEHICLES']}%"
    marker = folium.Marker(location=[row["LATITUDE"], row["LONGITUDE"]], popup=popup_text, icon=folium.Icon(color='blue'))
    marker.add_to(m)

# Display map
st.subheader("Map of Traffic Count Locations")
folium_static(m)

# Display scatter plot
scatter_fig = px.scatter(df_year, x="LONGITUDE", y="LATITUDE", color="SPEED_LIMIT")
scatter_fig.update_traces(marker=dict(size=5, color='red'))
scatter_fig.update_layout(title='Traffic Count Locations', xaxis_title='Longitude', yaxis_title='Latitude', font=dict(color='black'))
st.subheader("Scatter Plot of Traffic Count Locations")
st.plotly_chart(scatter_fig)

# Display histogram
hist_fig = px.histogram(df_year, x="SPEED_LIMIT")
hist_fig.update_traces(marker=dict(color='green'))
hist_fig.update_layout(title='Speed Limit Histogram', xaxis_title='Speed Limit', yaxis_title='Count', font=dict(color='black'))
st.subheader("Histogram of Speed Limits")
st.plotly_chart(hist_fig)

# Display bar chart
bar_fig = px.bar(df_year, x="DIRECTION_BOUND", y="PERCENT_HEAVY_VEHICLES")
bar_fig.update_traces(marker=dict(color='purple'))
bar_fig.update_layout(title='Percent Heavy Vehicles by Direction Bound', xaxis_title='Direction Bound', yaxis_title='Percent Heavy Vehicles', font=dict(color='black'))
st.subheader("Bar Chart of Percent Heavy Vehicles by Direction Bound")
st.plotly_chart(bar_fig)

# Display line chart
line_fig = px.line(df_year, x="MONTH_NAME", y="daily_totals")
line_fig.update_traces(mode='lines+markers')
line_fig.update_layout(title='Daily Traffic Volume by Month', xaxis_title='Month', yaxis_title='Traffic Volume', font=dict(color='black'))
st.subheader("Line Chart of Daily Traffic Volume by Month")
st.plotly_chart(line_fig)