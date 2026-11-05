import streamlit as st
import pandas as pd

st.set_page_config(page_title="Business Dashboard")

st.title("📊 Business Dashboard")

df = pd.read_csv("data/ventas.csv")

df["Ingresos"] = df["Cantidad"] * df["Precio"]

ventas_totales = df["Ingresos"].sum()

producto_top = (
    df.groupby("Producto")["Cantidad"]
    .sum()
    .idxmax()
)

st.metric(
    "Ventas Totales",
    f"${ventas_totales}"
)

st.metric(
    "Producto Más Vendido",
    producto_top
)

st.subheader("Ingresos por Producto")

ingresos = (
    df.groupby("Producto")["Ingresos"]
    .sum()
)

st.bar_chart(ingresos)

st.subheader("Datos")

st.dataframe(df)