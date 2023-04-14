import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

def app():
    st.set_page_config(page_title="Pairplot using Streamlit", page_icon=":bar_chart:")
    st.title("Pairplot of Penguin dataset")

    # Load dataset
    df = sns.load_dataset("penguins")

    # Show a progress bar while the visualization is loading
    with st.spinner("Loading Visualization..."):
        # Set style and plot
        sns.set_style("ticks")
        graph = sns.pairplot(df, hue="species")

    # Show the plot using Streamlit
    st.pyplot(graph.fig)

if __name__ == '__main__':
    app()


