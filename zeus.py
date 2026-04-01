import streamlit as st
import hermes

# 1. Page Configuration
st.set_page_config(page_title="Watu Triage", layout="centered", page_icon="📱")

def main():
    # 2. THE DESIGN ENGINE (Pure Minimalism)
    st.markdown("""
        <style>
        /* Import Inter Font */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap');
        
        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
            background-color: #FFFFFF;
            color: #111827;
        }

        /* Hide Default Junk */
        #MainMenu, footer, header {visibility: hidden;}

        /* Modern Underline Search Bar */
        .stTextInput > div > div > input {
            border: none;
            border-bottom: 2px solid #E5E7EB;
            border-radius: 0px;
            padding: 1rem 0rem;
            font-size: 1.4rem !important;
            background-color: transparent !important;
            transition: border-color 0.4s;
        }
        .stTextInput > div > div > input:focus {
            border-bottom: 2px solid #2563EB;
            box-shadow: none;
        }

        /* Result Section Styling */
        .result-container {
            margin-top: 3rem;
            animation: fadeIn 0.6s ease-out;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); }
        }

        .category-header {
            font-size: 1.7rem;
            font-weight: 600;
            letter-spacing: -0.025em;
            margin-bottom: 0.25rem;
        }

        .sub-status {
            font-size: 0.85rem;
            font-weight: 500;
            color: #6B7280;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin-bottom: 2rem;
        }

        .step-text {
            font-size: 1.1rem;
            line-height: 1.7;
            margin-bottom: 0.8rem;
            color: #374151;
        }

        .action-link {
            display: inline-block;
            color: #2563EB;
            text-decoration: none;
            font-weight: 600;
            border-bottom: 1.5px solid #2563EB;
            margin-bottom: 2rem;
        }

        .footer-note {
            margin-top: 4rem;
            padding-top: 2rem;
            border-top: 1px solid #F3F4F6;
            font-size: 0.9rem;
            color: #9CA3AF;
            text-align: center;
        }
        </style>
        """, unsafe_allow_html=True)

    # 3. HEADER
    st.markdown("<p style='font-weight: 600; color: #2563EB; margin-bottom: 0; font-size: 0.9rem;'>WATU AFTERSALES</p>", unsafe_allow_html=True)
    st.markdown("<h1 style='margin-top: 0; font-weight: 600; letter-spacing: -0.04em;'>Triage Hub</h1>", unsafe_allow_html=True)

    # 4. SEARCH BOX
    raw_input = st.text_input("", placeholder="Describe the symptom...")
    query = raw_input.lower().strip()

    if query:
        found = False
        for category, data in hermes.SAMSUNG_TRIAGE_DATA.items():
            if any(word in query for word in data["triggers"]):
                found = True
                
                st.markdown(f"""
                <div class="result-container">
                    <div class="category-header">{category}</div>
                    <div class="sub-status">{data["warranty_status"]} • {data["routing"]}</div>
                """, unsafe_allow_html=True)

                if "Out of Warranty" in data["warranty_status"] or "Pricing" in category:
                    st.markdown(f'<a href="{hermes.PRICING_SHEET_URL}" target="_blank" class="action-link">Open Pricing Sheet v3.1</a>', unsafe_allow_html=True)

                st.markdown("<p style='font-weight: 600; margin-bottom: 1rem; font-size: 0.95rem; color: #111827;'>PROTOCOL:</p>", unsafe_allow_html=True)
                
                for step in data["action_plan"]:
                    st.markdown(f"<div class='step-text'>• {step}</div>", unsafe_allow_html=True)
                
                st.markdown(f"""
                    <div style="margin-top: 2.5rem; color: #6B7280; font-size: 0.95rem; font-style: italic; border-left: 3px solid #E5E7EB; padding-left: 1rem;">
                        <b>Guidance:</b> {data['guidance']}
                    </div>
                </div>
                """, unsafe_allow_html=True)
                break

        if not found:
            st.markdown("<p style='color: #EF4444; margin-top: 2rem; font-weight: 500;'>Symptom unmapped. Please escalation to SIMU HQ Repairs.</p>", unsafe_allow_html=True)

    # 5. FOOTER
    st.markdown("<div class='footer-note'>OFFICIAL WATU LOGIC | @SIMUREPAIRS</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
