import streamlit as st
import hermes
import pandas as pd

st.set_page_config(page_title="L1 Triage Hub", layout="wide", page_icon="🛡️")

def main():
    # ELITE UI CUSTOM CSS (Coursera-Inspired)
    st.markdown("""
        <style>
        /* Main Background */
        .stApp { background-color: #F9FAFB; }
        
        /* Hero Section */
        .hero {
            background: linear-gradient(90deg, #1E293B 0%, #334155 100%);
            padding: 40px;
            border-radius: 20px;
            color: white;
            text-align: center;
            margin-bottom: 30px;
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
        }

        /* Modern Modern Card Style */
        .sop-card {
            background: white;
            padding: 25px;
            border-radius: 16px;
            border: 1px solid #E5E7EB;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
            transition: transform 0.2s;
        }
        .sop-card:hover { transform: translateY(-5px); box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1); }

        /* Badge Styling */
        .badge {
            display: inline-block;
            padding: 4px 12px;
            border-radius: 9999px;
            font-size: 0.75rem;
            font-weight: 700;
            text-transform: uppercase;
            margin-bottom: 10px;
        }
        .badge-blue { background: #DBEAFE; color: #1E40AF; }
        .badge-yellow { background: #FEF3C7; color: #92400E; }

        /* Step Entry Styling */
        .step-entry {
            background: #F8FAFC;
            border-left: 4px solid #3B82F6;
            padding: 12px;
            margin-bottom: 8px;
            border-radius: 0 8px 8px 0;
            color: #334155;
            font-size: 0.95rem;
        }
        </style>
    """, unsafe_allow_html=True)

    # 1. HERO HEADER
    st.markdown("""
        <div class='hero'>
            <h1 style='color: white; margin: 0;'>L1 Triage & Diagnosis Hub</h1>
            <p style='color: #94A3B8; font-size: 1.1rem;'>The single source of truth for Aftersales Excellence</p>
        </div>
    """, unsafe_allow_html=True)

    vault_df = hermes.load_vault()

    if not vault_df.empty:
        # 2. SEARCH BAR (Modernized)
        query = st.text_input("", placeholder="🔍 Search symptom (e.g., 'fundi', 'ink', 'arrears')...", label_visibility="collapsed")

        if query:
            results = hermes.search_index(query, vault_df)
            
            if not results.empty:
                sop = results.iloc[0]
                
                col_main, col_side = st.columns([2.5, 1])
                
                with col_main:
                    # RENDER MAIN CONTENT AS A CARD
                    st.markdown(f"""
                        <div class='sop-card'>
                            <span class='badge badge-blue'>Technical SOP</span>
                            <h2>{sop.get('Title', 'No Title')}</h2>
                            <hr style='margin: 20px 0; border: 0; border-top: 1px solid #E5E7EB;'>
                            <div style='background: #FFFBEB; padding: 15px; border-radius: 12px; border: 1px solid #FEF3C7; margin-bottom: 20px;'>
                                <strong style='color: #92400E;'>💡 LEGAL & FINANCIAL CONTEXT:</strong><br>
                                <span style='color: #B45309;'>{sop.get('Admin_Note', 'No guidance provided.')}</span>
                            </div>
                            <h4 style='color: #475569;'>Operational Steps</h4>
                    """, unsafe_allow_html=True)
                    
                    steps_raw = sop.get('Operational_Steps', '')
                    for step in str(steps_raw).split('|'):
                        if step.strip():
                            st.markdown(f"<div class='step-entry'>{step.strip()}</div>", unsafe_allow_html=True)
                    
                    st.markdown("</div>", unsafe_allow_html=True)
                
                with col_side:
                    # RELATED CONTEXT CARD
                    st.markdown("<div class='sop-card'>", unsafe_allow_html=True)
                    st.markdown("<h4 style='margin-top:0;'>Related Context</h4>", unsafe_allow_html=True)
                    
                    linked_nodes_str = sop.get('Linked_Nodes', '')
                    related_items = hermes.get_linked_nodes(linked_nodes_str, vault_df)
                    
                    if related_items:
                        for item in related_items:
                            # Using Streamlit info box for related links for better visibility
                            st.info(f"🔗 **{item['Title']}**")
                    
                    st.markdown("<br>", unsafe_allow_html=True)
                    util_link = sop.get('Utility_Link', '')
                    if util_link and util_link.strip() != "":
                        st.link_button("🚀 Access Tools", util_link, use_container_width=True)
                    st.markdown("</div>", unsafe_allow_html=True)
            else:
                st.warning("No matches found. Try a different keyword.")
    else:
        st.error("Connection Offline.")

if __name__ == "__main__":
    main()
