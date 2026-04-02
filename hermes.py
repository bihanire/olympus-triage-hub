import pandas as pd
import streamlit as st

# Your Published CSV Link
VAULT_CSV_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTTK8XlZZGtE9pDMI-RO86ZO5ZhdFxWNqFjs0BMzX_yQLYNYl1IYygcaEqRlF9FyKcfkr3aaidak8R2/pub?gid=157965277&single=true&output=csv"

def load_vault():
    try:
        df = pd.read_csv(VAULT_CSV_URL)
        # Clean IDs and handle any NaN values in Tags/Links
        df['REF_ID'] = df['REF_ID'].astype(str).str.strip()
        df['Tags'] = df['Tags'].fillna("")
        df['Linked_Nodes'] = df['Linked_Nodes'].fillna("")
        return df
    except Exception as e:
        st.error(f"Connection Error: {e}")
        return pd.DataFrame()

def search_index(query, df):
    query = query.lower().strip()
    if not query: return pd.DataFrame()
    # Scans Procedure names and Tags for matches
    mask = (df['Procedure'].str.contains(query, case=False, na=False) | 
            df['Tags'].str.contains(query, case=False, na=False))
    return df[mask]
