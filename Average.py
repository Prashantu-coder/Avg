import streamlit as st
import pandas as pd

# Function to load Google Sheet
def load_google_sheet(sheet_id, gid):
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid={gid}"
    df = pd.read_csv(url)
    return df

st.set_page_config(page_title="Live Google Sheet Viewer", layout="wide")

st.title("📊 Live Google Sheet Viewer")

# Input fields for Sheet ID & GID
sheet_id = st.text_input("1wu5nOv1xkv1BZpcGRC63ZDaWUUSiLiZ3WuxuBesXLEY")
gid = st.text_input("992072017")

if st.button("Load Sheet"):
    try:
        df = load_google_sheet(sheet_id, gid)
        st.success("✅ Sheet loaded successfully!")
        st.dataframe(df, use_container_width=True)
    except Exception as e:
        st.error(f"❌ Failed to load sheet: {e}")
