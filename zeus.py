import streamlit as st
import hermes

# 1. Page Configuration
st.set_page_config(page_title="Watu Technical Hub", layout="centered", page_icon="⚙️")

def main():
    # 2. THE PROFESSIONAL SERVICE UI ENGINE
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');
        
        /* Corporate Light Background */
        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
            background-color: #F3F4F6 !important;
        }

        #MainMenu, footer, header {visibility: hidden;}

        /* High-Contrast Search Input */
        .stTextInput > div > div > input {
            border: 2px solid #1E293B !important;
            border-radius: 12px;
            padding: 1.5rem;
            font-size: 1.3rem !important;
            background-color: #FFFFFF !important;
            color: #0F172A !important;
            font-weight: 600;
        }

        /* Result Module Card */
        .module-card {
            background-color: #FFFFFF;
            padding: 2.5rem;
            border-radius: 20px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);
            margin-top: 2rem;
            border: 1px solid #E2E8F0;
        }

        .module-header {
            font-size: 1.8rem;
            font-weight: 800;
            color: #0F172A !important;
            margin-bottom: 1rem;
            padding-bottom: 12px;
            border-bottom: 4px solid #2563EB;
        }

        /* Status Badges */
        .badge-box {
            display: inline-block;
            padding: 8px 16px;
            border-radius: 8px;
            font-size: 0.85rem;
            font-weight: 700;
            text-transform: uppercase;
            margin-right: 12px;
            margin-bottom: 10px;
        }
        .warranty-badge { background-color: #DBEAFE; color: #1E40AF !important; }
        .routing-badge { background-color: #F1F5F9; color: #475569 !important; }

        /* Action Steps: DEEP BLACK-SLATE FOR READABILITY */
        .action-step {
            background-color: #F8FAFC;
            border-left: 6px solid #2563EB;
            padding: 1.2rem;
            margin-bottom: 1rem;
            border-radius: 4px 12px 12px 4px;
            color: #0F172A !important; 
            font-weight: 600;
            font-size: 1.1rem;
            box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        }

        /* HQ Notice */
        .hq-directive {
            background-color: #FFFBEB;
            border: 1px solid #FEF3C7;
            padding: 1.5rem;
            border-radius: 12px;
            margin-top: 2rem;
            color: #92400E !important;
            font-size: 1rem;
        }

        /* Pricing Link */
        .btn-pricing {
            display: block;
            text-align: center;
            background-color: #111827;
            color: #FFFFFF !important;
            padding: 16px;
            border-radius: 12px;
            text-decoration: none;
            font-weight: 800;
            font-size: 1.1rem;
            margin: 2rem 0;
        }
        </style>
        """, unsafe_allow_html=True)

    # 3. BRANDING
    st.markdown("<p style='font-weight: 800; color: #2563EB; letter-spacing: 0.2em; margin-bottom:0; font-size: 0.9rem;'>WATU CREDIT LTD</p>", unsafe_allow_html=True)
    st.markdown("<h1 style='font-weight: 800; color: #0F172A; margin-top:0; font-size: 3rem; letter-spacing: -0.04em;'>Technical Hub.</h1>", unsafe_allow_html=True)

    # 4. SEARCH
    raw_input = st.text_input("", placeholder="Search diagnostic keyword (e.g. 'battery' or 'screen')")
    query = raw_input.lower().strip()

    if query:
        found = False
        for category, data in hermes.SAMSUNG_TRIAGE_DATA.items():
            if any(word in query for word in data["triggers"]):
                found = True
                
                st.markdown(f"""
                <div class="module-card">
                    <div class="module-header">{category}</div>
                    <div style="margin-bottom: 2rem;">
                        <span class="badge-box warranty-badge">🛡️ {data['warranty_status']}</span>
                        <span class="badge-box routing-badge">📍 {data['routing']}</span>
                    </div>
                """, unsafe_allow_html=True)

                if "Out of Warranty" in data["warranty_status"] or "Display" in category:
                    st.markdown(f'<a href="{hermes.PRICING_SHEET_URL}" target="_blank" class="btn-pricing">VIEW PRICING MATRIX V3.1</a>', unsafe_allow_html=True)

                st.markdown("<p style='font-weight: 800; font-size: 0.9rem; color: #64748B; margin-bottom: 1rem; letter-spacing: 0.05em;'>REQUIRED ACTIONS:</p>", unsafe_allow_html=True)
                
                for step in data["action_plan"]:
                    st.markdown(f"<div class='action-step'>✅ {step}</div>", unsafe_allow_html=True)
                
                st.markdown(f"""
                    <div class="hq-directive">
                        <b>📍 HQ GUIDANCE:</b> {data['guidance']}
                    </div>
                </div>
                """, unsafe_allow_html=True)
                break

        if not found:
            st.error("⚠️ Symptom unmapped. Please initiate manual inspection or contact SIMU HQ.")

if __name__ == "__main__":
    main()
