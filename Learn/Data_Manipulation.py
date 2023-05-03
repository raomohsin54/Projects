import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns 
import time

st.title("Sales App")
st.markdown('Use this app to make your own scatterplot about sales!')

sale_file = st.file_uploader('Select you file')

@st.cache_data()
def load_file(sale_file):
    time.sleep(3)
    if sale_file is not None: 
        df = pd.read_csv(sale_file)
    else: 
        df = pd.read_csv(r"C:\Users\mmukhtiar\Downloads\archive (3)\sales_data_sample.csv", encoding='iso-8859-1')
    return(df)
sale_df = load_file(sale_file)


selected_x_var = st.selectbox('What do you want the x variable to be?', ['PRICEEACH', 'QUANTITYORDERED', 'SALES'])

selected_y_var = st.selectbox('What do you want the y variable to be?', ['QUANTITYORDERED', 'SALES', 'PRICEEACH'])

selected_year = st.selectbox('What year do you want to select?', ['2003', '2004', 'Total'])

if selected_year == '2003':
    sale_df = sale_df[sale_df['YEAR_ID'] == 2003]
elif selected_year == '2004':
    sale_df = sale_df[sale_df['YEAR_ID'] == 2004]
else:
    pass

fig, ax = plt.subplots()
ax = sns.scatterplot(x=sale_df[selected_x_var], y=sale_df[selected_y_var], hue=sale_df['DEALSIZE'])
plt.xlabel(selected_x_var)
plt.ylabel(selected_y_var)

plt.title('Scatterplot of Sales: {}'. format(selected_year))

st.pyplot(fig)