import streamlit as st
import pandas as pd

sheet_id = "1wu5nOv1xkv1BZpcGRC63ZDaWUUSiLiZ3WuxuBesXLEY"
gid = "992072017"

def load_google_sheet(sheet_id, gid):
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid={gid}"
    df= pd.read_csv(url)
    return df
