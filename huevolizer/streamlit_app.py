import streamlit as st
import pandas as pd
import pyshewhart
import matplotlib.pyplot as plt
from huevolizer.cli import write_control_chart_data

st.title("Cartas de Control de producción diaria de huevos")
cartas_path = "cartas.csv"
raw_data = write_control_chart_data("tests/data/producción_diaria.csv","tests/data/conteo_individuos.csv",output_path=cartas_path)
data = pd.read_csv(cartas_path)
pyshewhart.XbarR(data["Fecha"], data["X"], sample_size=2)
st.pyplot(plt.gcf())
