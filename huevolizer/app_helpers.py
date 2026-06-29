"""Helper functions for the Streamlit app UI."""

import matplotlib.pyplot as plt
import os
import pandas as pd
import pyshewhart
import streamlit as st
from typing import Optional

from huevolizer.control_limits import X_R_limits_calculator

# --- Configuration ---
COUNT_FILE = "data/conteo_individuos.csv"
EGG_FILE = "data/produccion_diaria.csv"
XR_FILE = "data/X_R.csv"
SAMPLE_SIZE = 2
CSV_DATE_FORMAT = "%Y-%m-%d"


def render_individual_count_form() -> None:
    """Render the form to add a new individual count record."""
    with st.form("individual_count"):
        fecha = st.date_input("Fecha")
        gallinas = st.number_input("Gallinas", min_value=0, step=1)
        gallos = st.number_input("Gallos", min_value=0, step=1)
        pollos = st.number_input("Pollos", min_value=0, step=1)
        observaciones = st.text_area("Observaciones")
        if st.form_submit_button("Guardar"):
            if gallinas <= 0 and gallos <= 0 and pollos <= 0:
                st.error("Debe ingresar al menos un ave.")
                return
            new_row = pd.DataFrame(
                [
                    {
                        "Fecha": fecha.strftime(CSV_DATE_FORMAT),
                        "Gallinas": gallinas,
                        "Gallos": gallos,
                        "Pollos": pollos,
                        "Observaciones": observaciones,
                    }
                ]
            )
            try:
                append_to_csv(new_row, COUNT_FILE)
                st.success("Conteo guardado")
                st.rerun()
            except OSError as e:
                st.error(f"Error al guardar: {e}")


def render_egg_count_form() -> None:
    """Render the form to add a new daily egg count record."""
    with st.form("egg_count"):
        fecha = st.date_input("Fecha")
        huevos = st.number_input("Huevos", min_value=0, step=1)
        if st.form_submit_button("Guardar"):
            if huevos <= 0:
                st.error("Debe ingresar un número positivo de huevos.")
                return
            new_row = pd.DataFrame(
                [
                    {
                        "Fecha": fecha.strftime(CSV_DATE_FORMAT),
                        "Huevos": huevos,
                    }
                ]
            )
            try:
                append_to_csv(new_row, EGG_FILE)
                st.success("Huevos guardados")
                st.rerun()
            except OSError as e:
                st.error(f"Error al guardar: {e}")


def render_control_chart():
    """Compute and display the X-bar/R control chart."""
    xr_data = compute_and_save_xr_data(EGG_FILE, COUNT_FILE, XR_FILE)
    xr_last_n_rows = xr_data[-100:].reset_index()
    pyshewhart.XbarR(xr_last_n_rows["Fecha"], xr_last_n_rows["X"], sample_size=SAMPLE_SIZE)
    st.pyplot(plt.gcf())
    plt.close()  # clean up the figure to avoid memory leaks


def compute_and_save_xr_data(
    egg_path: str, count_path: str, output_path: str
) -> Optional[pd.DataFrame]:
    """Read daily egg and count data, compute X-R chart data, save and return it.

    Returns None if either input file is missing or empty.
    """
    eggs = pd.read_csv(egg_path)
    counts = pd.read_csv(count_path)
    if eggs is None or counts is None:
        return None
    calculator = X_R_limits_calculator(eggs, counts)
    calculator.save_x_r(output_path)
    return calculator.xr


def append_to_csv(df: pd.DataFrame, file_path: str) -> None:
    """Append a DataFrame to a CSV file, creating header only if file is new."""
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    df.to_csv(file_path, mode="a", index=False, header=not os.path.exists(file_path))
