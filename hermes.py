def load_vault():
    try:
        df = pd.read_csv(VAULT_CSV_URL)
        
        # This is the "Magic Fix": It strips spaces from all column headers automatically
        df.columns = [str(c).strip() for c in df.columns]
        
        # Ensure ID and critical columns are strings
        for col in df.columns:
            df[col] = df[col].astype(str).replace('nan', '')
            
        return df
    except Exception as e:
        st.error(f"Vault Connection Error: {e}")
        return pd.DataFrame()
