import streamlit as st
import hermes

st.set_page_config(page_title="Technical Index", layout="wide", page_icon="📝")

def main():
    # BANKER-WHITE CLEAN THEME
    st.markdown("""
        <style>
        .stApp { background-color: #FFFFFF; }
        .main-card { background-color: #F8FAFC; padding: 25px; border-radius: 12px; border: 1px solid #E2E8F0; }
        .step-entry { background-color: #FFFFFF; border-left: 6px solid #2563EB; padding: 15px; margin-bottom: 10px; font-weight: 600; border-radius: 0 8px 8px 0; }
        .side-link { background-color: #F1F5F9; padding: 12px; border-radius: 8px; margin-bottom: 8px; color: #1E293B; font-weight: 700; border: none; width: 100%; text-align: left; }
        </style>
    """, unsafe_allow_html=True)

    st.title("Technical Knowledge Repository")

    # Load Memory
    vault_df = hermes.load_vault()

    if not vault_df.empty:
        # Search Entry
        query = st.text_input("", placeholder="Search for a procedure or symptom (e.g. 'stolen', 'screen', 'restart')")

        if query:
            results = hermes.search_index(query, vault_df)
            
            if not results.empty:
                sop = results.iloc[0]
                
                col_main, col_side = st.columns([2, 1])
                
                with col_main:
                    st.markdown(f"## {sop['Procedure']}")
                    st.info(f"**Admin Note:** {sop['Critical_Note']}")
                    
                    # Split Operational_Steps by '|'
                    steps = str(sop['Operational_Steps']).split('|')
                    for step in steps:
                        st.markdown(f"<div class='step-entry'>• {step.strip()}</div>", unsafe_allow_html=True)
                
                with col_side:
                    st.subheader("Related Context")
                    # Wide Thinking Logic
                    links = str(sop['Linked_Nodes']).split(',')
                    for r_id in links:
                        link_id = r_id.strip()
                        related_row = vault_df[vault_df['REF_ID'] == link_id]
                        if not related_row.empty:
                            st.info(f"🔗 {related_row.iloc[0]['Procedure']}")
                    
                    st.markdown("---")
                    if pd.notna(sop['Utility_Link']):
                        st.link_button("Access External Tool", sop['Utility_Link'])
            else:
                st.warning("Case not found. Please add this to the Master Index.")

if __name__ == "__main__":
    main()
