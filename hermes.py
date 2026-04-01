import streamlit as st
import pandas as pd

# THE VAULT CONNECTOR
def fetch_vault_data():
    # Replace with your 'Published to Web' CSV link
    vault_url = "YOUR_MASTER_INDEX_CSV_URL"
    try:
        df = pd.read_csv(vault_url)
        return df
    except Exception:
        # Returns empty structure if link is broken
        return pd.DataFrame(columns=["REF_ID", "Procedure", "Tags", "Operational_Steps", "Linked_Nodes", "Critical_Note", "Utility_Link"])

def find_context(query, df):
    query = query.lower()
    # Scans Tags and Procedure names for matches
    results = df[df.apply(lambda row: query in str(row['Tags']).lower() or 
                                     query in str(row['Procedure']).lower(), axis=1)]
    return results
