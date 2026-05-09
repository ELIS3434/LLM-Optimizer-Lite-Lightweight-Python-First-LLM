import streamlit as st

from dashboard.components.api import get_json
from dashboard.components.tables import render_table

st.title("Experiments")
experiments = get_json("/experiments")
render_table("Experiments", experiments)
