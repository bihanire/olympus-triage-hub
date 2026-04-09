import streamlit as st
import hermes
import pandas as pd

st.set_page_config(page_title="Watu Triage Hub", layout="wide")

def main():
    # MINIMALIST "TECH-LOG" CSS
    st.markdown("""
        <style>
        /* Modern Font Stack */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700&display=swap');
        html, body, [class*="st-"] { font-family: 'Inter', sans-serif; }

        .stApp { background-color: #FFFFFF; }

        /* The Search Box - Clean & Centered */
        .stTextInput input {
            border-radius: 10px !important;
            border: 1px solid #E2E8F0 !important;
            padding: 15px !important;
            font-size: 1.1rem !important;
        }

        /* The Main Result Card */
        .result-container {
            border: 1px solid #F1F5F9;
            border-radius: 20px;
            padding: 40px;
            box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.05);
            background: white;
            margin-top: 20px;
        }

        /* Status Badge for Legal Status */
        .status-badge {
            background: #EFF6FF;
            color: #1D4ED8;
            padding: 6px 16px;
            border-radius: 8px;
            font-size: 0.85rem;
            font-weight: 700;
            display: inline-block;
            margin-bottom: 15px;
        }

        /* Steps - The "Coursera" Checklist Style */
        .step-item {
            display: flex;
            align-items: center;
            padding: 15px 0;
            border-bottom: 1px solid #F1F5F9;
            color: #475569;
        }
        .step-number {
            background: #F1F5F9;
            color: #64748B;
            width: 30px;
            height: 30px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-right: 15px;
            font-size: 0.8rem;
            font-weight: 700;
        }
        </style>
    """, unsafe_allow_html=True)

    # HEADER
    st.title("L1 Triage & Diagnosis Hub")
    st.markdown("<p style='color: #64748B;'>Standardized Operating Procedures for Aftersales Excellence</p>", unsafe_allow_html=True)

    vault_df = hermes.load_vault()

    if not vault_df.empty:
        # SEARCH
        query = st.text_input("", placeholder="Search symptom or procedure (e.g. 'fundi', 'ink', 'arrears')...", label_visibility="collapsed")

        if query:
            results = hermes.search_index(query, vault_df)
            
            if not results.empty:
                sop = results.iloc[0]
                
                # TWO COLUMN LAYOUT
                col_main, col_side = st.columns([2, 1])
                
                with col_main:
                    st.markdown("<div class='result-container'>", unsafe_allow_html=True)
                    st.markdown(f"<div class='status-badge'>REF: {sop.get('REF_ID', 'N/A')}</div>", unsafe_allow_html=True)
                    st.markdown(f"<h1 style='margin:0;'>{sop.get('Title', 'Untitled')}</h1>", unsafe_allow_html=True)
                    
                    # Admin Guidance Box (Clean Yellow)
                    note = sop.get('Admin_Note', '')
                    if note:
                        st.markdown(f"""
                            <div style='background: #FFFBEB; padding: 20px; border-radius: 12px; margin: 25px 0;'>
                                <strong style='color: #92400E;'>Legal & Financial Status:</strong><br>
                                <span style='color: #B45309;'>{note}</span>
                            </div>
                        """, unsafe_allow_html=True)
                    
                    # Workflow
                    st.markdown("### Operational Steps")
                    steps = str(sop.get('Operational_Steps', '')).split('|')
                    for i, step in enumerate(steps):
                        if step.strip():
                            st.markdown(f"""
                                <div class='step-item'>
                                    <div class='step-number'>{i+1}</div>
                                    <div>{step.strip()}</div>
                                </div>
                            """, unsafe_allow_html=True)
                    st.markdown("</div>", unsafe_allow_html=True)

                with col_side:
                    # Sidebar - "Wide Context"
                    st.markdown("### Wide Context")
                    related = hermes.get_linked_nodes(sop.get('Linked_Nodes', ''), vault_df)
                    for item in related:
                        st.button(f"🔗 {item['Title']}", key=item['REF_ID'], use_container_width=True)
                    
                    st.markdown("---")
                    util_link = sop.get('Utility_Link', '')
                    if util_link:
                        st.link_button("🚀 Access Master Sheet", util_link, use_container_width=True)
            else:
                st.info("No matching procedure found. Try broader keywords.")

if __name__ == "__main__":
    main()
