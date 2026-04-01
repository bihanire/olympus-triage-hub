import streamlit as st
import hermes

# 1. Page Configuration
st.set_page_config(page_title="Watu Technical Hub", layout="centered", page_icon="📱")

def main():
    # 2. THE MASTER UI ENGINE (Forced High Contrast)
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');
        
        /* Force high contrast white theme */
        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
            background-color: #FFFFFF !important;
            color: #1E293B !important;
        }

        #MainMenu, footer, header {visibility: hidden;}

        /* Search Bar: Deep Border and Black Text */
        .stTextInput > div > div > input {
            border: 2px solid #1E293B !important;
            border-radius: 12px;
            padding: 1.2rem;
            font-size: 1.2rem !important;
            background-color: #FFFFFF !important;
            color: #1E293B !important;
            font-weight: 600;
        }

        /* Result Module Card */
        .module-card {
            background-color: #F8FAFC;
            padding: 2.5rem;
            border-radius: 20px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
            margin-top: 2rem;
            border: 1px solid #E2E8F0;
        }

        .module-header {
            font-size: 1.6rem;
            font-weight: 800;
            color: #0F172A !important;
            margin-bottom: 1rem;
            border-bottom: 3px solid #2563EB;
            padding-bottom: 10px;
        }

        /* Badges */
        .badge {
            display: inline-block;
            padding: 6px 14px;
            border-radius: 8px;
            font-size: 0.8rem;
            font-weight: 700;
            text-transform: uppercase;
            margin-right: 10px;
            margin-bottom: 10px;
        }
        .badge-warranty { background-color: #DBEAFE; color: #1E40AF !important; }
        .badge-diagnosis { background-color: #F1F5F9; color: #475569 !important; }

        /* Step Boxes: FORCED DARK TEXT ON CLEAN BACKGROUND */
        .step-box {
            background-color: #FFFFFF;
            border-left: 6px solid #2563EB;
            padding: 1.2rem;
            margin-bottom: 1rem;
            border-radius: 4px 12px 12px 4px;
            color: #1E293B !important; 
            font-weight: 600;
            font-size: 1.1rem;
            box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        }

        .hq-directive {
            background-color: #FFFBEB;
            border: 1px solid #FEF3C7;
            padding: 1.2rem;
            border-radius: 12px;
            margin-top: 2rem;
            color: #92400E !important;
            font-size: 1rem;
        }

        .pricing-btn {
            display: block;
            text-align: center;
            background-color: #1E293B;
            color: #FFFFFF !important;
            padding: 14px;
            border-radius: 10px;
            text-decoration: none;
            font-weight: 700;
            margin: 2rem 0;
        }
        </style>
        """, unsafe_allow_html=True)

    # BRANDING
    st.markdown("<p style='font-weight: 800; color: #2563EB; letter-spacing: 0.15em; margin-bottom:0; font-size: 0.8rem;'>WATU CREDIT LTD</p>", unsafe_allow_html=True)
    st.markdown("<h1 style='font-weight: 800; color: #0F172A; margin-top:0; font-size: 2.8rem; letter-spacing: -0.04em;'>Technical Hub.</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: #64748B; font-weight: 500;'>Warranty & Diagnosis Assist</p>", unsafe_allow_html=True)

    query = st.text_input("", placeholder="Search symptom (e.g. 'cracked screen' or 'battery drain')").lower().strip()

    if query:
        found = False
        for category, data in hermes.SAMSUNG_TRIAGE_DATA.items():
            if any(word in query for word in data["triggers"]):
                found = True
                
                st.markdown(f"""
                <div class="module-card">
                    <div class="module-header">🔍 {category}</div>
                    <div style="margin-bottom: 2rem;">
                        <span class="badge badge-warranty">🛡️ {data['warranty_status']}</span>
                        <span class="badge badge-diagnosis">📍 {data['routing']}</span>
                    </div>
                """, unsafe_allow_html=True)

                if "Out of Warranty" in data["warranty_status"] or "Display" in category:
                    st.markdown(f'<a href="{hermes.PRICING_SHEET_URL}" target="_blank" class="pricing-btn">💰 OPEN PRICING MATRIX V3.1</a>', unsafe_allow_html=True)

                st.markdown("<p style='font-weight: 800; font-size: 0.85rem; color: #64748B; margin-bottom: 1rem; letter-spacing: 0.05em;'>REQUIRED ACTIONS:</p>", unsafe_allow_html=True)
                
                for step in data["action_plan"]:
                    st.markdown(f"<div class='step-box'>✅ {step}</div>", unsafe_allow_html=True)
                
                st.markdown(f"""
                    <div class="hq-directive">
                        <b>📍 HQ GUIDANCE:</b> {data['guidance']}
                    </div>
                </div>
                """, unsafe_allow_html=True)
                break

        if not found:
            st.error("⚠️ Symptom unmapped. Please initiate manual inspection or contact simurepairs@watu.africa.")

    # FOOTER
    st.markdown("<p style='text-align: center; color: #94A3B8; font-size: 0.75rem; margin-top: 5rem; font-weight: 700; letter-spacing: 0.1em;'>PROPRIETARY LOGIC | @SIMUREPAIRS</p>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
