import streamlit as st
import hermes
import pandas as pd

st.set_page_config(page_title="Watu Triage Pro", layout="wide", initial_sidebar_state="collapsed")

def main():
    # THE PROFESSIONAL DESIGN SYSTEM
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;800&display=swap');
        
        * { font-family: 'Plus Jakarta Sans', sans-serif; }
        .stApp { background-color: #F8FAFC; }

        /* HERO HEADER - Clean & Impactful */
        .hero-section {
            background: white;
            padding: 3rem 2rem;
            border-bottom: 1px solid #E2E8F0;
            margin: -6rem -5rem 2rem -5rem;
            text-align: center;
        }

        /* SEARCH BOX - Precision Engineering */
        div[data-baseweb="input"] {
            border-radius: 12px !important;
            border: 2px solid #E2E8F0 !important;
            transition: all 0.3s ease;
        }
        div[data-baseweb="input"]:focus-within {
            border-color: #2563EB !important;
            box-shadow: 0 0 0 4px rgba(37, 99, 235, 0.1) !important;
        }

        /* THE COURSERA CARD GRID */
        .content-container {
            display: grid;
            grid-template-columns: 2fr 1fr;
            gap: 2rem;
            margin-top: 2rem;
        }

        .card {
            background: white;
            border-radius: 20px;
            padding: 2.5rem;
            border: 1px solid #F1F5F9;
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.05);
        }

        /* OPERATIONAL STEPS - Modern Timeline */
        .step-row {
            display: flex;
            padding: 1rem 0;
            border-bottom: 1px solid #F8FAFC;
        }
        .step-icon {
            color: #2563EB;
            font-weight: 800;
            margin-right: 1.5rem;
            min-width: 25px;
        }

        /* CONTEXT BUTTONS - High Fidelity */
        .context-pill {
            display: block;
            background: #1E293B;
            color: white !important;
            padding: 12px 20px;
            border-radius: 10px;
            margin-bottom: 10px;
            text-decoration: none;
            font-weight: 600;
            font-size: 0.9rem;
            transition: all 0.2s;
            text-align: center;
        }
        .context-pill:hover {
            background: #334155;
            transform: scale(1.02);
        }
        </style>
    """, unsafe_allow_html=True)

    # 1. HERO
    st.markdown("""
        <div class="hero-section">
            <h1 style="color: #0F172A; font-size: 2.5rem; font-weight: 800; margin-bottom: 0.5rem;">L1 Triage Hub</h1>
            <p style="color: #64748B; font-size: 1.1rem;">Aftersales Excellence & Diagnostic Logic</p>
        </div>
    """, unsafe_allow_html=True)

    vault_df = hermes.load_vault()

    if not vault_df.empty:
        # 2. SEARCH AREA
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            query = st.text_input("", placeholder="🔍 Search (e.g. 'screen', 'fundi', '30/70')...", label_visibility="collapsed")

        if query:
            results = hermes.search_index(query, vault_df)
            
            if not results.empty:
                sop = results.iloc[0]
                
                # 3. CONTENT GRID
                col_main, col_side = st.columns([2.2, 1], gap="large")
                
                with col_main:
                    st.markdown(f"""
                        <div class="card">
                            <span style="background: #EFF6FF; color: #1E40AF; padding: 4px 12px; border-radius: 6px; font-weight: 700; font-size: 0.8rem;">REF: {sop.get('REF_ID')}</span>
                            <h2 style="margin-top: 1rem; color: #0F172A;">{sop.get('Title')}</h2>
                            
                            <div style="background: #FFFBEB; border: 1px solid #FEF3C7; padding: 1.5rem; border-radius: 12px; margin: 1.5rem 0;">
                                <strong style="color: #92400E;">⚠️ Legal & Financial Warning</strong><br>
                                <span style="color: #B45309;">{sop.get('Admin_Note')}</span>
                            </div>
                            
                            <h4 style="color: #475569; margin-bottom: 1rem;">Execution Steps</h4>
                    """, unsafe_allow_html=True)
                    
                    steps = str(sop.get('Operational_Steps')).split('|')
                    for i, step in enumerate(steps):
                        if step.strip():
                            st.markdown(f"""
                                <div class="step-row">
                                    <div class="step-icon">{i+1}</div>
                                    <div style="color: #334155;">{step.strip()}</div>
                                </div>
                            """, unsafe_allow_html=True)
                    st.markdown("</div>", unsafe_allow_html=True)

                with col_side:
                    st.markdown("""<div class="card" style="padding: 1.5rem;">
                        <h4 style="margin-top:0; color: #64748B;">Wide Context</h4>
                    """, unsafe_allow_html=True)
                    
                    related = hermes.get_linked_nodes(sop.get('Linked_Nodes', ''), vault_df)
                    for item in related:
                        st.markdown(f'<a class="context-pill">🔗 {item["Title"]}</a>', unsafe_allow_html=True)
                    
                    st.markdown("<hr style='border: 0.5px solid #F1F5F9; margin: 2rem 0;'>", unsafe_allow_html=True)
                    
                    util_link = sop.get('Utility_Link', '')
                    if util_link:
                        st.link_button("🚀 Access Master System", util_link, use_container_width=True)
                    st.markdown("</div>", unsafe_allow_html=True)
            else:
                st.info("No matching diagnostic flow found.")
    else:
        st.error("Data Sync Failed.")

if __name__ == "__main__":
    main()
