import streamlit as st
import hermes
import pandas as pd

# 1. PAGE CONFIGURATION
st.set_page_config(
    page_title="L1 Triage & Diagnosis LLM", 
    layout="wide", 
    page_icon="🛡️"
)

def main():
    # 2. ELITE UI STYLING (High Contrast for Branch Visibility)
    st.markdown("""
        <style>
        .stApp { background-color: #F1F5F9; }
        
        /* Main Procedure Card */
        .main-card { 
            background-color: #FFFFFF; 
            padding: 30px; 
            border-radius: 16px; 
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
            border: 1px solid #E2E8F0;
            color: #1E293B !important;
            margin-bottom: 20px;
        }
        
        /* Header and Text Styling */
        h1, h2, h3 { color: #0F172A !important; font-weight: 800 !important; }
        .stMarkdown, p, span { color: #334155 !important; }

        /* Step Entry Blocks */
        .step-entry { 
            background-color: #F8FAFC; 
            border-left: 6px solid #2563EB; 
            padding: 18px; 
            margin-bottom: 12px; 
            font-weight: 700; 
            color: #0F172A !important;
            border-radius: 0 8px 8px 0;
            font-size: 1.1rem;
        }

        /* Legal & Financial Warning Box */
        .warning-box { 
            background-color: #FEFCE8; 
            border: 1px solid #FEF08A; 
            padding: 20px; 
            border-radius: 12px; 
            color: #854D0E !important; 
            font-size: 1rem;
            margin-bottom: 25px;
        }
        
        /* Sidebar Panel */
        .side-panel {
            background-color: #FFFFFF;
            padding: 20px;
            border-radius: 12px;
            border: 1px solid #E2E8F0;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<h1 style='text-align: center;'>L1 Triage & Diagnosis Hub</h1>", unsafe_allow_html=True)

    # 3. LOAD DATA FROM HERMES
    vault_df = hermes.load_vault()

    if not vault_df.empty:
        # SEARCH INTERFACE
        query = st.text_input("", placeholder="🔍 Search symptom (e.g., 'fundi', 'ink', 'arrears', 'stolen')...", label_visibility="collapsed")

        if query:
            results = hermes.search_index(query, vault_df)
            
            if not results.empty:
                # Get the top matching row
                sop = results.iloc[0]
                
                # Create Layout: 70% Main Content, 30% Sidebar
                col_main, col_side = st.columns([2.2, 1])
                
                with col_main:
                    st.markdown("<div class='main-card'>", unsafe_allow_html=True)
                    st.markdown(f"<h2>{sop.get('Title', 'No Title')}</h2>", unsafe_allow_html=True)
                    
                    # Display Legal/Financial Note (Admin_Note)
                    admin_note = sop.get('Admin_Note', '')
                    if admin_note and admin_note.strip() != "":
                        st.markdown(f"<div class='warning-box'><b>⚠️ LEGAL & FINANCIAL STATUS:</b><br>{admin_note}</div>", unsafe_allow_html=True)
                    
                    # Display Operational Steps
                    st.markdown("### Operational Steps")
                    steps_raw = sop.get('Operational_Steps', '')
                    if steps_raw:
                        steps = str(steps_raw).split('|')
                        for step in steps:
                            if step.strip():
                                st.markdown(f"<div class='step-entry'>• {step.strip()}</div>", unsafe_allow_html=True)
                    st.markdown("</div>", unsafe_allow_html=True)
                
                with col_side:
                    st.markdown("<div class='side-panel'>", unsafe_allow_html=True)
                    st.markdown("### Related Context")
                    
                    # Fetch Linked Nodes for "Wide Thinking"
                    linked_nodes_str = sop.get('Linked_Nodes', '')
                    related_items = hermes.get_linked_nodes(linked_nodes_str, vault_df)
                    
                    if related_items:
                        for item in related_items:
                            st.info(f"🔗 **{item['Title']}**")
                    else:
                        st.write("No related procedures linked.")
                    
                    st.markdown("---")
                    
                    # External Utility Links
                    util_link = sop.get('Utility_Link', '')
                    if util_link and util_link.strip() != "":
                        st.link_button("🚀 Access Master Sheet/Form", util_link, use_container_width=True)
                    
                    st.markdown("</div>", unsafe_allow_html=True)
            else:
                st.warning("No matching SOP found. Try broader keywords like 'Repair' or 'Legal'.")
    else:
        st.error("System Offline. Please ensure the Master Spreadsheet is accessible.")

if __name__ == "__main__":
    main()
