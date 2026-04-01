import streamlit as st
import hermes

# 1. Executive Configuration
st.set_page_config(page_title="Watu Triage Hub", layout="centered", page_icon="💎")

def main():
    # 2. THE 2026 ARTSY DESIGN ENGINE
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&family=Space+Grotesk:wght@300;700&display=swap');
        
        /* The Canvas: Pure Banker White */
        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
            background-color: #FDFDFD !important;
            color: #0F172A;
        }

        #MainMenu, footer, header {visibility: hidden;}

        /* Ultra-Minimal Underline Search */
        .stTextInput > div > div > input {
            border: none;
            border-bottom: 1px solid #E2E8F0;
            border-radius: 0px;
            padding: 1.5rem 0rem;
            font-size: 1.8rem !important;
            font-family: 'Space Grotesk', sans-serif;
            font-weight: 300;
            background-color: transparent !important;
            transition: all 0.6s cubic-bezier(0.16, 1, 0.3, 1);
            color: #0F172A !important;
        }
        .stTextInput > div > div > input:focus {
            border-bottom: 2px solid #2563EB;
            padding-left: 10px;
            box-shadow: none;
        }

        /* Glassmorphism Results Card */
        .result-container {
            margin-top: 4rem;
            animation: artsyFade 1s ease-out;
        }

        @keyframes artsyFade {
            from { opacity: 0; filter: blur(10px); transform: translateY(20px); }
            to { opacity: 1; filter: blur(0); transform: translateY(0); }
        }

        .category-header {
            font-family: 'Space Grotesk', sans-serif;
            font-size: 3rem;
            font-weight: 700;
            letter-spacing: -0.06em;
            color: #0F172A;
            line-height: 1;
            margin-bottom: 0.5rem;
        }

        .status-pill {
            font-size: 0.75rem;
            font-weight: 800;
            color: #64748B;
            text-transform: uppercase;
            letter-spacing: 0.2em;
            margin-bottom: 4rem;
            display: flex;
            gap: 15px;
        }

        .step-item {
            font-size: 1.25rem;
            line-height: 1.6;
            margin-bottom: 1.5rem;
            color: #334155;
            font-weight: 400;
            border-left: 1px solid #E2E8F0;
            padding-left: 20px;
            transition: all 0.3s ease;
        }
        .step-item:hover {
            border-left: 3px solid #2563EB;
            color: #0F172A;
        }

        .pricing-matrix {
            display: inline-block;
            font-family: 'Space Grotesk', sans-serif;
            font-weight: 700;
            color: #2563EB;
            text-decoration: none;
            font-size: 1rem;
            letter-spacing: 0.05em;
            border-bottom: 2px solid #2563EB;
            margin-bottom: 3rem;
        }

        .guidance-footer {
            margin-top: 5rem;
            padding: 2rem;
            background-color: #F8FAFC;
            border-radius: 4px;
            font-size: 0.95rem;
            color: #475569;
            border-top: 1px solid #E2E8F0;
        }
        </style>
        """, unsafe_allow_html=True)

    # 3. ARTSY BRANDING
    st.markdown("<p style='font-weight: 800; color: #2563EB; margin-bottom: 0; font-size: 0.75rem; letter-spacing: 0.3em;'>WATU CREDIT LTD</p>", unsafe_allow_html=True)
    st.markdown("<h1 style='margin-top: 0; font-family: Space Grotesk; font-weight: 700; letter-spacing: -0.07em; font-size: 4.5rem; line-height: 0.9;'>Triage Engine.</h1>", unsafe_allow_html=True)

    # 4. THE SEARCH
    raw_input = st.text_input("", placeholder="Search diagnostic keyword...")
    query = raw_input.lower().strip()

    if query:
        found = False
        for category, data in hermes.SAMSUNG_TRIAGE_DATA.items():
            if any(word in query for word in data["triggers"]):
                found = True
                st.markdown(f"""
                <div class="result-container">
                    <div class="category-header">{category}</div>
                    <div class="status-pill">
                        <span>● {data["warranty_status"]}</span>
                        <span>● {data["routing"]}</span>
                    </div>
                """, unsafe_allow_html=True)

                if "Out of Warranty" in data["warranty_status"] or "Display" in category:
                    st.markdown(f'<a href="{hermes.PRICING_SHEET_URL}" target="_blank" class="pricing-matrix">ACCESS PRICING MATRIX V3.1 →</a>', unsafe_allow_html=True)

                st.markdown("<p style='font-weight: 800; margin-bottom: 2rem; font-size: 0.8rem; color: #0F172A; letter-spacing: 0.1em;'>TECHNICAL PROTOCOL</p>", unsafe_allow_html=True)
                for step in data["action_plan"]:
                    st.markdown(f"<div class='step-item'>{step}</div>", unsafe_allow_html=True)
                
                st.markdown(f"""
                    <div class="guidance-footer">
                        <b style="color:#0F172A">HQ DIRECTIVE:</b> {data['guidance']}
                    </div>
                </div>
                """, unsafe_allow_html=True)
                break

        if not found:
            st.markdown("<p style='color: #94A3B8; margin-top: 4rem; font-family: Space Grotesk; font-size: 1.2rem;'>System unmapped. Please initiate manual escalation.</p>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
