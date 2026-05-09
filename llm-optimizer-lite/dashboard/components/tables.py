import pandas as pd
import streamlit as st


def render_table(title: str, rows: list[dict]) -> None:
    st.subheader(title)
    st.dataframe(pd.DataFrame(rows))
