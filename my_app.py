import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Generate random data
np.random.seed(42)
data = pd.DataFrame({
    'x': np.random.normal(0, 1, 100),
    'y': np.random.normal(0, 1, 100)
})

# Visualize data using a scatter plot
fig, ax = plt.subplots()
sns.scatterplot(x='x', y='y', data=data, ax=ax)
ax.set_title('Scatter plot of x vs. y')
st.pyplot(fig)

# Visualize data using a histogram
fig, ax = plt.subplots()
sns.histplot(data['y'], bins=10, ax=ax)
ax.set_title('Histogram of y')
st.pyplot(fig)

# Visualize data using a box plot
fig, ax = plt.subplots()
sns.boxplot(y='y', data=data, ax=ax)
ax.set_title('Box plot of y')
st.pyplot(fig)

if __name__ == '__main__':
    app()


