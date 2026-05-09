import os

import streamlit as st

st.title("Settings")
st.write("Backend URL", os.getenv("BACKEND_BASE_URL", "http://localhost:8000"))
