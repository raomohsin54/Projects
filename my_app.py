import streamlit as st
import pandas as pd
import seaborn as sns

# Load iris dataset
iris = sns.load_dataset('iris')

# Sidebar - Select features to plot
st.sidebar.header('Select features')
x_axis = st.sidebar.selectbox('X-axis', iris.columns[:-1])
y_axis = st.sidebar.selectbox('Y-axis', iris.columns[:-1])
hue = st.sidebar.selectbox('Color by', iris.columns[:-1])

# Scatter plot
fig = sns.scatterplot(x=x_axis, y=y_axis, hue=hue, data=iris)
st.pyplot(fig)


if __name__ == '__main__':
    app()


