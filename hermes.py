import pandas as pd
import streamlit as st

VAULT_CSV_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTTK8XlZZGtE9pDMI-RO86ZO5ZhdFxWNqFjs0BMzX_yQLYNYl1IYygcaEqRlF9FyKcfkr3aaidak8R2/pub?gid=157965277&single=true&output=csv"

def load_vault():
    try:
        df = pd.read_csv(VAULT_CSV_URL)
        df.columns = [str(c).strip() for c in df.columns]
        for col in df.columns:
            df[col] = df[col].astype(str).replace(['nan', 'NaN', 'None'], '')
        if 'REF_ID' in df.columns:
            df['REF_ID'] = df['REF_ID'].str.upper().str.strip()
        return df
    except Exception as e:
        st.error(f"Vault Offline: {e}")
        return pd.DataFrame()

def search_index(query, df):
    query = query.lower().strip()
    if not query or df.empty: return pd.DataFrame()
    # Matches against Title and Tags
    mask = (df['Title'].str.contains(query, case=False, na=False) | 
            df['Tags'].str.contains(query, case=False, na=False))
    return df[mask]

def get_linked_nodes(links_string, df):
    if not links_string: return []
    target_ids = [i.strip().upper() for i in str(links_string).split(',') if i.strip()]
    return df[df['REF_ID'].isin(target_ids)][['REF_ID', 'Title']].to_dict('records')
