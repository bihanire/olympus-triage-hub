import pandas as pd
import streamlit as st

# Your Single Source of Truth CSV Link
VAULT_CSV_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTTK8XlZZGtE9pDMI-RO86ZO5ZhdFxWNqFjs0BMzX_yQLYNYl1IYygcaEqRlF9FyKcfkr3aaidak8R2/pub?gid=157965277&single=true&output=csv"

def load_vault():
    """
    Fetches the consolidated SOP data, cleans the headers to prevent KeyErrors,
    and prepares the data for relational searching.
    """
    try:
        # 1. Fetch data
        df = pd.read_csv(VAULT_CSV_URL)
        
        # 2. BULLETPROOF HEADERS: Remove any hidden spaces or newlines from column names
        # This prevents the "KeyError: Admin_Note" issue
        df.columns = [str(c).strip() for c in df.columns]
        
        # 3. DATA SCRUBBING: 
        # Convert all columns to strings and handle 'nan' (empty) values
        for col in df.columns:
            df[col] = df[col].astype(str).replace(['nan', 'NaN', 'None'], '')
        
        # 4. ID CLEANING: Ensure REF_IDs are always clean for linking logic
        if 'REF_ID' in df.columns:
            df['REF_ID'] = df['REF_ID'].str.upper().str.strip()
            
        return df
    except Exception as e:
        st.error(f"❌ Connection to Master Sheet Failed: {e}")
        return pd.DataFrame()

def search_index(query, df):
    """
    Scans the Title and Tags for matches. 
    Optimized to find 'symptom language' like 'fundi' or 'bleeding'.
    """
    query = query.lower().strip()
    if not query or df.empty:
        return pd.DataFrame()
    
    # We search both Title and Tags columns
    # Adjust 'Title' to whatever your header is (e.g., 'SOP_Name' or 'Procedure')
    title_col = 'Title' if 'Title' in df.columns else df.columns[1]
    tags_col = 'Tags' if 'Tags' in df.columns else df.columns[2]

    mask = (
        df[title_col].str.contains(query, case=False, na=False) | 
        df[tags_col].str.contains(query, case=False, na=False)
    )
    return df[mask]

def get_linked_nodes(links_string, df):
    """
    Takes the comma-separated REF_IDs from the Linked_Nodes column
    and fetches their full Titles for the 'Wide Context' sidebar.
    """
    if not links_string:
        return []
        
    # Split "RP_01, AD_01" into ['RP_01', 'AD_01']
    target_ids = [i.strip().upper() for i in str(links_string).split(',') if i.strip()]
    
    # Filter the vault for these IDs and return their info
    related = df[df['REF_ID'].isin(target_ids)]
    return related[['REF_ID', 'Title']].to_dict('records')
