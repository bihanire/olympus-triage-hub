import pandas as pd
import streamlit as st

# Your Live Google Sheet CSV Link
VAULT_CSV_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTTK8XlZZGtE9pDMI-RO86ZO5ZhdFxWNqFjs0BMzX_yQLYNYl1IYygcaEqRlF9FyKcfkr3aaidak8R2/pub?gid=157965277&single=true&output=csv"

def load_vault():
    try:
        # Pulling fresh data from the sheet
        df = pd.read_csv(VAULT_CSV_URL)
        
        # CLEANUP: Remove hidden spaces in headers
        df.columns = df.columns.str.strip()
        
        # Ensure critical columns are treated as strings to avoid errors
        cols_to_fix = ['REF_ID', 'Title', 'Tags', 'Operational_Steps', 'Linked_Nodes']
        for col in cols_to_fix:
            if col in df.columns:
                df[col] = df[col].astype(str).str.strip()
        
        # Fill empty cells to prevent crashes
        df = df.fillna("")
        return df
    except Exception as e:
        st.error(f"Vault Connection Offline: {e}")
        return pd.DataFrame()

def search_index(query, df):
    query = query.lower().strip()
    if not query: return pd.DataFrame()
    
    # Global Search: Checks Title and Tags
    mask = (df['Title'].str.contains(query, case=False, na=False) | 
            df['Tags'].str.contains(query, case=False, na=False))
    return df[mask]
