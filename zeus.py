import streamlit as st
import hermes
import pandas as pd

st.set_page_config(page_title="Technical Hub", layout="wide", page_icon="📝")

def main():
    # BANKER-WHITE PROFESSIONAL THEME
    st.markdown("""
        <style>
        .stApp { background-color: #FFFFFF; }
        .main-card { background-color: #F8FAFC; padding: 25px; border-radius: 12px; border: 1px solid #E2E8F0; }
        .step-entry { background-color: #FFFFFF; border-left: 6px solid #2563EB; padding: 15px; margin-bottom: 10px; font-weight: 600; border-radius: 0 8px 8px 0; }
        .side-note { background-color: #FFFBEB; border: 1px solid #FEF3C7; padding: 15px; border-radius: 8px; color: #92400E; font-size: 0.95rem; }
        </style>
    """, unsafe_allow_html=True)

    st.title("Technical Knowledge Repository")

    # LOAD THE VAULT
    vault_df = hermes.load_vault()

    if not vault_df.empty:
        # GLOBAL SEARCH
        query = st.text_input("", placeholder="Search procedures, symptoms, or tags (e.g. 'stolen', 'screen', 'restart')")

        if query:
            results = hermes.search_index(query, vault_df)
            
            if not results.empty:
                sop = results.iloc[0] # Take the best match
                
                col_main, col_side = st.columns([2, 1])
                
                with col_main:
                    st.markdown(f"## {sop['Title']}")
                    if pd.notna(sop['Admin_Note']):
                        st.markdown(f"<div class='side-note'><b>Admin Guidance:</b><br>{sop['Admin_Note']}</div>", unsafe_allow_html=True)
                    
                    st.markdown("### Operational Steps")
                    # Split steps by the pipe character '|'
                    steps = str(sop['Operational_Steps']).split('|')
                    for step in steps:
                        if step.strip():
                            st.markdown(f"<div class='step-entry'>• {step.strip()}</div>", unsafe_allow_html=True)
                
                with col_side:
                    st.subheader("Related Context")
                    # THE WIDE-THINKING SIDEBAR
                    links = str(sop['Linked_Nodes']).split(',')
                    for r_id in links:
                        link_id = r_id.strip()
                        related_row = vault_df[vault_df['REF_ID'] == link_id]
                        if not related_row.empty:
                            st.info(f"🔗 {related_row.iloc[0]['Title']}")
                    
                    st.markdown("---")
                    if 'Utility_Link' in vault_df.columns and pd.notna(sop['Utility_Link']):
                        st.link_button("Access External Tool", sop['Utility_Link'])
            else:
                st.warning("No matching procedure found. The Encyclopedia is still growing.")

if __name__ == "__main__":
    main()
