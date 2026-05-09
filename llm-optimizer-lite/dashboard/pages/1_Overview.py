import streamlit as st

from dashboard.components.api import get_json

st.title("Overview")
summary = get_json("/analytics/summary")
st.metric("Total Requests", summary.get("total_requests", 0))
st.metric("Estimated Cost (USD)", summary.get("total_estimated_cost_usd", 0.0))
st.metric("P95 Latency (ms)", summary.get("p95_latency_ms", 0))
