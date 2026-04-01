import streamlit as st
import hermes

# 1. Page Configuration
st.set_page_config(page_title="Watu Triage", layout="centered", page_icon="📱")

def main():
    # 2. MINIMALIST CSS (Clean, Modern, Simple)
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap');
        
        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
            background-color: #FFFFFF;
            color: #111827;
        }

        #MainMenu, footer, header {visibility: hidden;}

        /* Clean Search Bar */
        .stTextInput > div > div > input {
            border: none;
            border-bottom: 2px solid #E5E7EB;
            border-radius: 0px;
            padding: 1rem 0rem;
            font-size: 1.5rem !important;
            background-color: transparent !important;
            transition: border-color 0.3s;
        }
        .stTextInput > div > div > input:focus {
            border-bottom: 2px solid #2563EB;
            box-shadow: none;
        }

        /* Minimalist Result Area */
        .result-box {
            margin-top: 3rem;
            animation: fadeIn 0.5s ease-in;
        }

        @keyframes fadeIn {
            from { opacity: 0; } to { opacity: 1; }
        }

        .category-title {
            font-size: 1.8rem;
            font-weight: 600;
            letter-spacing: -0.02em;
            margin-bottom: 0.5rem;
        }

        .status-text {
            font-size: 0.9rem;
            font-weight: 500;
            color: #6B7280;
            text-transform: uppercase;
            margin-bottom: 2rem;
        }

        .step-item {
            font-size: 1.1rem;
            line-height: 1.6;
            margin-bottom: 1rem;
            color: #374151;
        }

        .pricing-link {
            color: #2563EB;
            text-decoration: none;
            font-weight: 600;
            border-bottom: 1px solid #2563EB;
        }

        .note-box {
            margin-top: 3rem;
            padding-top: 1.5rem;
            border-top: 1px solid #F3F4F6;
            font-size: 0.95rem;
            color: #6B7280;
            font-style: italic;
        }
        </style>
        """, unsafe_allow_html=True)

    # 3. HEADER
    st.markdown("<p style='font-weight: 600; color: #2563EB; margin-bottom: 0;'>WATU AFTERSALES</p>", unsafe_allow_html=True)
    st.markdown("<h1 style='margin-top: 0; font-weight: 600;'>Triage Assistant</h1>", unsafe_allow_html=True)

    # 4. SEARCH (The "Google" Style)
    raw_input = st.text_input("", placeholder="Search symptom...")
    query = raw_input.lower().strip()

    if query:
        found = False
        for category, data in hermes.SAMSUNG_TRIAGE_DATA.items():
            if any(word in query for word in data["triggers"]):
                found = True
                
                st.markdown(f"""
                <div class="result-box">
                    <div class="category-title">{category}</div>
                    <div class="status-text">
                        {data["warranty_status"]} • {data["routing"]}
                    </div>
                """, unsafe_allow_html=True)

                if "Out of Warranty" in data["warranty_status"]:
                    st.markdown(f"""
                        <p style='margin-bottom: 2rem;'>
                            Financials: <a href="{hermes.PRICING_SHEET_URL}" target="_blank" class="pricing-link">View v3.1 Pricing Sheet</a>
                        </p>
                    """, unsafe_allow_html=True)

                st.markdown("<p style='font-weight: 600; margin-bottom: 1rem;'>Protocol:</p>", unsafe_allow_html=True)
                
                for step in data["action_plan"]:
                    st.markdown(f"<div class='step-item'>{step}</div>", unsafe_allow_html=True)
                
                st.markdown(f"""
                    <div class="note-box">
                        <b>Note:</b> {data['guidance']}
                    </div>
                </div>
                """, unsafe_allow_html=True)
                break

        if not found:
            st.markdown("<p style='color: #EF4444; margin-top: 2rem;'>Symptom not found. Please contact HQ.</p>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
