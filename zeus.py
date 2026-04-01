import streamlit as st
import hermes

st.set_page_config(page_title="Technical Hub", layout="wide")

def main():
    # CLEAN, MINIMALIST UI
    st.markdown("""
        <style>
        .main-panel { background-color: #FFFFFF; padding: 20px; border-radius: 8px; }
        .side-panel { background-color: #F8FAFC; padding: 20px; border-left: 1px solid #E2E8F0; height: 100vh; }
        .step-block { background-color: #F1F5F9; padding: 15px; border-radius: 5px; margin-bottom: 10px; font-weight: 500; }
        .warning-box { background-color: #FFF7ED; border-left: 5px solid #EA580C; padding: 15px; color: #9A3412; margin-bottom: 20px; }
        </style>
    """, unsafe_allow_html=True)

    st.subheader("Knowledge Repository")
    
    # LOAD DATA
    index_df = hermes.fetch_vault_data()
    
    # SEARCH BAR
    search_query = st.text_input("", placeholder="Search procedures, symptoms, or keywords...")

    if search_query:
        matches = hermes.find_context(search_query, index_df)
        
        if not matches.empty:
            active_sop = matches.iloc[0] # Best match
            
            col1, col2 = st.columns([2, 1])
            
            with col1:
                st.markdown(f"## {active_sop['Procedure']}")
                st.markdown(f"<div class='warning-box'><b>Note:</b> {active_sop['Critical_Note']}</div>", unsafe_allow_html=True)
                
                # Split steps by the pipe character
                steps = str(active_sop['Operational_Steps']).split('|')
                for step in steps:
                    st.markdown(f"<div class='step-block'>• {step.strip()}</div>", unsafe_allow_html=True)
            
            with col2:
                st.markdown("<div class='side-panel'>", unsafe_allow_html=True)
                st.markdown("### Related Context")
                
                # THROW WIDE: Pulling the Linked Nodes
                links = str(active_sop['Linked_Nodes']).split(',')
                for node_id in links:
                    node_data = index_df[index_df['REF_ID'] == node_id.strip()]
                    if not node_data.empty:
                        if st.button(f"🔗 {node_data.iloc[0]['Procedure']}", key=node_id):
                            # This button could trigger a rerun with the new ID
                            pass
                
                st.markdown("---")
                if pd.notna(active_sop['Utility_Link']):
                    st.link_button("Access External Tool", active_sop['Utility_Link'])
                st.markdown("</div>", unsafe_allow_html=True)
        else:
            st.warning("No matching procedure found in the current index.")

if __name__ == "__main__":
    main()
