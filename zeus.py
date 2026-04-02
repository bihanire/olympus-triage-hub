import streamlit as st
import hermes

st.set_page_config(page_title="Watu Technical Hub", layout="wide", page_icon="📱")

def main():
    # PROFESSIONAL BANKER-WHITE UI
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');
        html, body, [class*="css"] { font-family: 'Inter', sans-serif; background-color: #FFFFFF !important; }
        #MainMenu, footer, header {visibility: hidden;}
        
        .stTextInput > div > div > input {
            border: 2px solid #0F172A !important; border-radius: 8px; padding: 1.2rem;
            font-size: 1.2rem !important; font-weight: 600; color: #0F172A !important;
        }

        .sop-card {
            background-color: #F8FAFC; padding: 2.5rem; border-radius: 12px;
            border: 1px solid #E2E8F0; margin-top: 1.5rem;
        }

        .action-step {
            background-color: #FFFFFF; border-left: 6px solid #2563EB;
            padding: 1rem; margin-bottom: 10px; font-weight: 700; color: #1E293B !important;
            box-shadow: 0 1px 2px rgba(0,0,0,0.05);
        }

        .directive-box {
            background-color: #FFFBEB; border: 1px solid #FEF3C7;
            padding: 1rem; border-radius: 8px; color: #92400E !important; font-size: 0.95rem;
        }
        </style>
        """, unsafe_allow_html=True)

    # BRANDING
    st.markdown("<p style='font-weight: 800; color: #2563EB; letter-spacing: 0.2em; margin-bottom:0;'>WATU CREDIT LTD</p>", unsafe_allow_html=True)
    st.markdown("<h1 style='font-weight: 800; color: #0F172A; margin-top:0; font-size: 3rem; letter-spacing: -0.05em;'>Technical Hub.</h1>", unsafe_allow_html=True)

    # GLOBAL SEARCH
    query = st.text_input("", placeholder="Search SOPs or Symptoms (e.g. 'police abstract', 'frozen', 'water damage')").lower().strip()

    if query:
        found = False
        for module, data in hermes.SAMSUNG_TRIAGE_DATA.items():
            # SCAN EVERYTHING: Triggers + Action Steps + Guidance
            search_pool = " ".join(data['triggers'] + data['action_plan'] + [data['guidance']]).lower()
            
            if query in search_pool:
                found = True
                col1, col2 = st.columns([2, 1])
                with col1:
                    st.markdown(f"### 📋 {module}")
                    for step in data["action_plan"]:
                        st.markdown(f"<div class='action-step'>✅ {step}</div>", unsafe_allow_html=True)
                with col2:
                    st.markdown("### 🔍 Details")
                    st.info(f"**Status:** {data['status']}")
                    st.markdown(f"<div class='directive-box'><b>📌 HQ GUIDANCE:</b><br>{data['guidance']}</div>", unsafe_allow_html=True)
                    st.markdown("---")
                    st.markdown(f"**Official Routing:**\n{data['routing']}")
                    st.link_button("Price Matrix v3.1", hermes.PRICING_SHEET_URL)
                st.markdown("---")
        
        if not found:
            st.error("No SOP match found. Check spelling or try a different keyword.")
    else:
        st.info("System Ready. Search above for Triage or SOP assistance.")

if __name__ == "__main__":
    main()
