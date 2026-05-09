import streamlit as st

from dashboard.components.api import get_json
from dashboard.components.tables import render_table

st.title("Logs")
rows = get_json("/logs")
render_table("Recent Request Logs", rows)
