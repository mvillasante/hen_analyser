import streamlit as st
import pandas as pd
import pyshewhart
import matplotlib.pyplot as plt
from huevolizer.cli import write_control_chart_data
import os

st.title("Cartas de Control de producción diaria de huevos")

col1, col2 = st.columns(2)
with col1:
    st.subheader("Agregar nuevo conteo")
    with st.form("nuevo_conteo"):
        fecha = st.date_input("Fecha")
        gallinas = st.number_input("Gallinas", min_value=0, step=1)
        gallos = st.number_input("Gallos", min_value=0, step=1)
        pollos = st.number_input("Pollos", min_value=0, step=1)
        observaciones = st.text_area("Observaciones")
        submitted = st.form_submit_button("Guardar")
        if submitted:
            new_row = pd.DataFrame([{
                "Fecha": fecha.strftime("%Y-%m-%d"),
                "Gallinas": gallinas,
                "Gallos": gallos,
                "Pollos": pollos,
                "Observaciones": observaciones,
            }])
            file_path = "data/conteo_individuos.csv"
            new_row.to_csv(file_path, mode="a", index=False, header=not os.path.exists(file_path))
            st.success("Conteo guardado")
            st.rerun()

with col2:
    st.subheader("Agregar huevos del día")
    with st.form("nuevos_huevos"):
        fecha = st.date_input("Fecha")
        huevos = st.number_input("Huevos", min_value=0, step=1)
        submitted_h = st.form_submit_button("Guardar")
        if submitted_h:
            new_row = pd.DataFrame([{
                "Fecha": fecha.strftime("%Y-%m-%d"),
                "Huevos": huevos,
            }])
            file_path = "data/producción_diaria.csv"
            new_row.to_csv(file_path, mode="a", index=False, header=not os.path.exists(file_path))
            st.success("Huevos guardados")
            st.rerun()

X_R_path = "X_R.csv"
write_control_chart_data("data/producción_diaria.csv","data/conteo_individuos.csv",output_path=X_R_path)
data = pd.read_csv(X_R_path)
pyshewhart.XbarR(data["Fecha"], data["X"], sample_size=2)
st.pyplot(plt.gcf())
