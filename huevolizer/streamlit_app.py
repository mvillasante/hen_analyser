import streamlit as st

from huevolizer.app_helpers import (
    render_control_chart,
    render_egg_count_form,
    render_individual_count_form,
)

# --- Page layout ---
st.title("Cartas de Control de producción diaria de huevos")

st.subheader("Carta de Control")
render_control_chart()

col1, col2 = st.columns(2)
with col1:
    st.subheader("Agregar huevos del día")
    render_egg_count_form()
with col2:
    st.subheader("Agregar nuevo conteo")
    render_individual_count_form()

