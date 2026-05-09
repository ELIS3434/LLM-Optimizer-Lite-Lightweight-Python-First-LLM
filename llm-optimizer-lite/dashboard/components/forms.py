import streamlit as st


def prompt_create_form() -> dict[str, str] | None:
    with st.form("prompt_create"):
        name = st.text_input("Prompt name")
        submitted = st.form_submit_button("Create")
    if submitted and name:
        return {"name": name}
    return None
