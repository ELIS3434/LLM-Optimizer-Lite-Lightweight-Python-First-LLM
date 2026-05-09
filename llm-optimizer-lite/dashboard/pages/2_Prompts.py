import streamlit as st

from dashboard.components.api import get_json
from dashboard.components.tables import render_table

st.title("Prompts")
prompts = get_json("/prompts")
render_table("Prompt Registry", prompts)
