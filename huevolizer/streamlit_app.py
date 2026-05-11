import streamlit as st
import pandas as pd
import pyshewhart
import matplotlib.pyplot as plt
from huevolizer.cli import write_control_chart_data

st.title("Cartas de Control de producción diaria de huevos")
X_R_path = "X_R.csv"
raw_data = write_control_chart_data("data/producción_diaria.csv","data/conteo_individuos.csv",output_path=X_R_path)
data = pd.read_csv(X_R_path)
pyshewhart.XbarR(data["Fecha"], data["X"], sample_size=2)
st.pyplot(plt.gcf())
