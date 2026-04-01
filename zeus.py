import streamlit as st
import hermes

# 1. Page Config
st.set_page_config(page_title="Watu Triage Hub", layout="centered", page_icon="⚙️")

def main():
    # 2. THE CUSTOMER CARE UI ENGINE
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');
        
        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
            background-color: #F3F4F6 !important;
            color: #1F2937;
        }

        #MainMenu, footer, header {visibility: hidden;}

        /* Search Bar: Bold & Clear */
        .stTextInput > div > div > input {
            border: 2px solid #D1D5DB;
            border-radius: 12px;
            padding: 1.2rem;
            font-size: 1.2rem !important;
            background-color: #FFFFFF !important;
            box-shadow: 0 1px 2px rgba(0,0,0,0.05);
        }

        /* Result Module */
        .module-card {
            background-color: #FFFFFF;
            padding: 2rem;
            border-radius: 16px;
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
            margin-top: 2rem;
            border: 1px solid #E5E7EB;
        }

        .module-header {
            font-size: 1.5rem;
            font-weight: 800;
            color: #111827;
            margin-bottom: 1rem;
            border-bottom: 2px solid #F3F4F6;
            padding-bottom: 0.5rem;
        }

        /* Color Coded Status Badges */
        .badge {
            display: inline-block;
            padding: 4px 12px;
            border-radius: 6px;
            font-size: 0.75rem;
            font-weight: 700;
            text-transform: uppercase;
            margin-right: 8px;
        }
        .badge-warranty { background-color: #DBEAFE; color: #1E40AF; }
        .badge-routing { background-color: #F3F4F6; color: #374151; }

        /* Step Section */
        .step-box {
            background-color: #F9FAFB;
            border-left: 4px solid #2563EB;
            padding: 1rem;
            margin-bottom: 0.8rem;
            border-radius: 0 8px 8px 0;
            font-weight: 500;
        }

        /* HQ Note Section */
        .hq-note {
            background-color: #FFFBEB;
            border: 1px solid #FEF3C7;
            padding: 1rem;
            border-radius: 12px;
            margin-top: 1.5rem;
            color: #92400E;
            font-size: 0.9rem;
        }

        .pricing-btn {
            display: block;
            text-align: center;
            background-color: #111827;
            color: white !important;
            padding: 12px;
            border-radius: 8px;
            text-decoration: none;
            font-weight: 700;
            margin: 1.5rem 0;
        }
        </style>
        """, unsafe_allow_html=True)

    # BRANDING
    st.markdown("<p style='font-weight: 800; color: #2563EB; letter-spacing: 0.1em; margin-bottom:0;'>WATU AFTERSALES</p>", unsafe_allow_html=True)
    st.markdown("<h1 style='font-weight: 800; color: #111827; margin-top:0;'>Diagnostic Triage</h1>", unsafe_allow_html=True)

    query = st.text_input("", placeholder="Enter symptom (e.g. cracked screen, wont charge)").lower().strip()

    if query:
        found = False
        for category, data in hermes.SAMSUNG_TRIAGE_DATA.items():
            if any(word in query for word in data["triggers"]):
                found = True
                
                st.markdown(f"""
                <div class="module-card">
                    <div class="module-header">🔍 {category}</div>
                    <div style="margin-bottom: 1.5rem;">
                        <span class="badge badge-warranty">🛡️ {data['warranty_status']}</span>
                        <span class="badge badge-routing">📍 {data['routing']}</span>
                    </div>
                """, unsafe_allow_html=True)

                if "Out of Warranty" in data["warranty_status"] or "Display" in category:
                    st.markdown(f'<a href="{hermes.PRICING_SHEET_URL}" target="_blank" class="pricing-btn">💰 OPEN PRICING MATRIX V3.1</a>', unsafe_allow_html=True)

                st.markdown("<p style='font-weight: 700; font-size: 0.9rem; color: #4B5563;'>MANDATORY ACTION STEPS:</p>", unsafe_allow_html=True)
                
                for step in data["action_plan"]:
                    st.markdown(f"<div class='step-box'>{step}</div>", unsafe_allow_html=True)
                
                st.markdown(f"""
                    <div class="hq-note">
                        <b>💡 HQ DIRECTIVE:</b> {data['guidance']}
                    </div>
                </div>
                """, unsafe_allow_html=True)
                break

        if not found:
            st.error("⚠️ Symptom unmapped. Please initiate manual inspection and contact SIMU HQ.")

if __name__ == "__main__":
    main()
