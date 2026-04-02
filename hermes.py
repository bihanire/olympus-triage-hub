import pandas as pd
import streamlit as st

# Your Live Google Sheet CSV Link
VAULT_CSV_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTTK8XlZZGtE9pDMI-RO86ZO5ZhdFxWNqFjs0BMzX_yQLYNYl1IYygcaEqRlF9FyKcfkr3aaidak8R2/pub?gid=157965277&single=true&output=csv"

def load_vault():
    try:
        df = pd.read_csv(VAULT_CSV_URL)
        # SCRUB HEADERS: Removes hidden spaces like "Title " or " Tags"
        df.columns = df.columns.str.strip()
        
        # Scrub Data: Clean up the content
        df['REF_ID'] = df['REF_ID'].astype(str).str.strip()
        df['Title'] = df['Title'].fillna("Untitled Procedure")
        df['Tags'] = df['Tags'].fillna("")
        df['Linked_Nodes'] = df['Linked_Nodes'].fillna("")
        return df
    except Exception as e:
        st.error(f"Vault Connection Error: {e}")
        return pd.DataFrame()

def search_index(query, df):
    query = query.lower().strip()
    if not query: return pd.DataFrame()
    
    # SEARCH LOGIC: Scans the 'Title' and 'Tags' columns
    mask = (df['Title'].str.contains(query, case=False, na=False) | 
            df['Tags'].str.contains(query, case=False, na=False))
    return df[mask]
