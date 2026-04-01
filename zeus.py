import streamlit as st
import hermes

# 1. Page Configuration
st.set_page_config(page_title="Watu Triage Hub", layout="centered", page_icon="🛠️")

def main():
    # 2. HIGH-CONTRAST UX ENGINE (Modern Tech Aesthetic)
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
        
        /* High Contrast Background */
        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
            background-color: #FFFFFF;
            color: #1A1A1A;
        }

        #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}

        /* The "Paper" Card - Sharp & Clear */
        .result-card {
            background: #FFFFFF;
            padding: 2rem;
            border-radius: 12px;
            border: 2px solid #E5E7EB;
            box-shadow: 0 4px 0px 0px #E5E7EB;
            margin-top: 1.5rem;
            animation: slideUp 0.4s ease-out;
        }

        @keyframes slideUp {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }

        /* Bold Search Input for Sunlight */
        .stTextInput > div > div > input {
            border-radius: 8px;
            border: 3px solid #1A1A1A !important;
            padding: 1.2rem;
            font-size: 1.3rem !important;
            font-weight: 600;
            color: #1A1A1A !important;
        }

        /* High-Visibility Protocol Steps */
        .step-text {
            color: #1A1A1A;
            font-size: 1.2rem;
            font-weight: 600;
            margin: 0.8rem 0;
            padding-left: 10px;
            border-left: 4px solid #2563EB;
        }

        /* Sharp Status Badges */
        .badge-sharp {
            background: #1A1A1A;
            color: #FFFFFF;
            padding: 5px 15px;
            border-radius: 4px;
            font-weight: 800;
            font-size: 0.8rem;
            text-transform: uppercase;
        }

        .pricing-link {
            display: block;
            text-align: center;
            background: #2563EB;
            color: white !important;
            padding: 1rem;
            border-radius: 8px;
            text-decoration: none;
            font-weight: 800;
            font-size: 1.1rem;
            margin-top: 1.5rem;
        }

        .staff-note {
            background: #F3F4F6;
            padding: 1rem;
            border-radius: 8px;
            font-size: 1rem;
            color: #374151;
            border: 1px solid #D1D5DB;
            margin-top: 2rem;
        }
        </style>
        """, unsafe_allow_html=True)

    # 3. HEADER
    st.markdown("<h1 style='text-align: left; color: #1A1A1A; font-weight: 800; font-size: 2.5rem; margin-bottom: 0;'>Triage Hub</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: left; color: #4B5563; font-size: 1rem; margin-bottom: 2rem; text-transform: uppercase; letter-spacing: 1px;'>Watu Aftersales Technical Protocol</p>", unsafe_allow_html=True)

    # 4. SEARCH
    raw_input = st.text_input("", placeholder="ENTER SYMPTOM (e.g. BATTERY)")
    query = raw_input.lower().strip()

    if query:
        found = False
        for category, data in hermes.SAMSUNG_TRIAGE_DATA.items():
            if any(word in query for word in data["triggers"]):
                found = True
                
                st.markdown(f"""
                <div class="result-card">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.5rem;">
                        <h2 style="margin: 0; color: #1A1A1A; font-weight: 800; font-size: 1.5rem;">{category}</h2>
                        <span class="badge-sharp">{"WARRANTY" if "In-Warranty" in data["warranty_status"] else "OUT OF WARRANTY"}</span>
                    </div>
                    
                    <p style="color: #2563EB; font-weight: 800; font-size: 1rem; margin-bottom: 1.5rem;">ROUTING: {data["routing"]}</p>
                """, unsafe_allow_html=True)

                # Pricing Section
                if "Out of Warranty" in data["warranty_status"]:
                    st.markdown(f"""
                        <a href="{hermes.PRICING_SHEET_URL}" target="_blank" class="pricing-link">VIEW OFFICIAL PRICING SHEET</a>
                        <p style="text-align: center; font-size: 0.8rem; margin-top: 5px; color: #6B7280;">Refer to v3.1 Chart for Model-Specific Quotes</p>
                    """, unsafe_allow_html=True)

                st.markdown("<p style='font-weight: 800; font-size: 0.9rem; color: #1A1A1A; border-bottom: 2px solid #1A1A1A; display: inline-block; margin-bottom: 1rem;'>TECHNICAL STEPS</p>", unsafe_allow_html=True)
                
                for step in data["action_plan"]:
                    st.markdown(f"<div class='step-text'>{step}</div>", unsafe_allow_html=True)
                
                st.markdown(f"""
                    <div class="staff-note">
                        <b>📍 HQ GUIDANCE:</b> {data['guidance']}
                    </div>
                </div>
                """, unsafe_allow_html=True)
                break

        if not found:
            st.error("❌ SYMPTOM NOT RECOGNIZED. CALL SIMU HQ AFTER SALES IMMEDIATELY.")

    # 5. FOOTER
    st.markdown("<p style='text-align: center; color: #9CA3AF; font-weight: 800; font-size: 0.7rem; margin-top: 50px; letter-spacing: 2px;'>OFFICIAL WATU AFTERSALES PROTOCOL | REPORT ISSUES TO @SIMUREPAIRS</p>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
