import streamlit as st
import hermes
import pandas as pd

st.set_page_config(page_title="Technical Hub", layout="wide", page_icon="📝")

def main():
    # ELITE BANKER UI - HIGH CONTRAST & DEPTH
    st.markdown("""
        <style>
        .stApp { background-color: #F1F5F9; } /* Subtle Gray Background */
        
        /* Main SOP Card */
        .main-card { 
            background-color: #FFFFFF; 
            padding: 30px; 
            border-radius: 16px; 
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
            border: 1px solid #E2E8F0;
            color: #1E293B !important;
            margin-bottom: 20px;
        }
        
        /* Typography Fixes */
        h1, h2, h3 { color: #0F172A !important; font-weight: 800 !important; }
        .stMarkdown, p, span { color: #334155 !important; }

        /* Step Entry - Bold & High Contrast */
        .step-entry { 
            background-color: #F8FAFC; 
            border-left: 6px solid #2563EB; 
            padding: 18px; 
            margin-bottom: 12px; 
            font-weight: 700; 
            color: #0F172A !important;
            border-radius: 0 8px 8px 0;
            font-size: 1.1rem;
            box-shadow: inset 0 1px 2px rgba(0,0,0,0.02);
        }

        /* Guidance Box (Yellow) */
        .side-note { 
            background-color: #FEFCE8; 
            border: 1px solid #FEF08A; 
            padding: 20px; 
            border-radius: 12px; 
            color: #854D0E !important; 
            font-size: 1rem;
            margin-bottom: 25px;
        }
        
        /* Side Panel Styling */
        .side-panel {
            background-color: #FFFFFF;
            padding: 20px;
            border-radius: 12px;
            border: 1px solid #E2E8F0;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<h1 style='text-align: center;'>Technical Knowledge Hub</h1>", unsafe_allow_html=True)

    # 1. LOAD THE MEMORY
    vault_df = hermes.load_vault()

    if not vault_df.empty:
        # 2. SEARCH INTERFACE
        query = st.text_input("", placeholder="🔍 Search procedures, symptoms, or tags...", label_visibility="collapsed")

        if query:
            results = hermes.search_index(query, vault_df)
            
            if not results.empty:
                sop = results.iloc[0]
                
                # Create the Wide-Thinking Layout
                col_main, col_side = st.columns([2.2, 1])
                
                with col_main:
                    st.markdown(f"<div class='main-card'>", unsafe_allow_html=True)
                    st.markdown(f"<h2>{sop['Title']}</h2>", unsafe_allow_html=True)
                    
                    if pd.notna(sop['Admin_Note']) and str(sop['Admin_Note']).strip() != "":
                        st.markdown(f"<div class='side-note'><b>💡 ADMIN GUIDANCE:</b><br>{sop['Admin_Note']}</div>", unsafe_allow_html=True)
                    
                    st.markdown("### Operational Steps")
                    steps = str(sop['Operational_Steps']).split('|')
                    for step in steps:
                        if step.strip():
                            st.markdown(f"<div class='step-entry'>• {step.strip()}</div>", unsafe_allow_html=True)
                    st.markdown("</div>", unsafe_allow_html=True)
                
                with col_side:
                    st.markdown("<div class='side-panel'>", unsafe_allow_html=True)
                    st.markdown("### Related Context")
                    # RELATIONAL LOGIC: Link IDs to Titles
                    links = str(sop['Linked_Nodes']).split(',')
                    for r_id in links:
                        link_id = r_id.strip()
                        related_row = vault_df[vault_df['REF_ID'] == link_id]
                        if not related_row.empty:
                            st.info(f"🔗 {related_row.iloc[0]['Title']}")
                    
                    st.markdown("---")
                    # External Links
                    if 'Utility_Link' in vault_df.columns and pd.notna(sop['Utility_Link']):
                        st.link_button("🚀 Open External Tool", str(sop['Utility_Link']), use_container_width=True)
                    st.markdown("</div>", unsafe_allow_html=True)
            else:
                st.warning("No matching procedure found. The Encyclopedia is still growing.")
    else:
        st.error("Connection failed. Check your Google Sheet CSV Publish link.")

if __name__ == "__main__":
    main()
