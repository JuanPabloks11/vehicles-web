import streamlit as st
import pandas as pd
import plotly_express as px

st.header("Cuadro de Mandos - Análisis de Vehículos")

df = pd.read_csv("vehicles_us.csv")

if st.button("Mostrar histograma de precios"):
    fig = px.histogram(df, x="price", nbins=50,
                       title="Distribución de precios")
    st.plotly_chart(fig)