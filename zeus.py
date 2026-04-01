import streamlit as st
import hermes

# 1. Page Configuration
st.set_page_config(page_title="Watu Triage Hub", layout="centered", page_icon="⚡")

def main():
    # 2. THE MOTION ENGINE (Advanced CSS)
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
        
        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
            background: radial-gradient(circle at top right, #f8fafc, #e2e8f0);
        }

        /* 🏎️ FADE IN ANIMATION FOR THE WHOLE PAGE */
        .stApp {
            animation: fadeInPage 0.8s ease-out;
        }
        @keyframes fadeInPage {
            from { opacity: 0; } to { opacity: 1; }
        }

        /* 🛸 SEARCH BAR GLOW */
        .stTextInput > div > div > input {
            border-radius: 15px;
            border: 2px solid #cbd5e1;
            padding: 1.2rem;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        }
        .stTextInput > div > div > input:focus {
            border-color: #2563eb;
            transform: scale(1.02);
            box-shadow: 0 10px 25px -5px rgba(37, 99, 235, 0.2);
        }

        /* ✨ INTERACTIVE RESULT CARD */
        .result-card {
            background: rgba(255, 255, 255, 0.8);
            backdrop-filter: blur(12px);
            padding: 2.5rem;
            border-radius: 24px;
            border: 1px solid rgba(255, 255, 255, 0.3);
            box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1);
            margin-top: 2rem;
            animation: slideUp 0.6s cubic-bezier(0.23, 1, 0.32, 1);
            transition: transform 0.3s ease;
        }
        .result-card:hover {
            transform: translateY(-5px);
        }

        @keyframes slideUp {
            from { opacity: 0; transform: translateY(40px); }
            to { opacity: 1; transform: translateY(0); }
        }

        /* 🏷️ PULSING BADGES */
        .badge {
            padding: 6px 16px;
            border-radius: 50px;
            font-weight: 800;
            font-size: 0.75rem;
            text-transform: uppercase;
            letter-spacing: 1px;
            animation: pulse 2s infinite;
        }
        @keyframes pulse {
            0% { box-shadow: 0 0 0 0 rgba(34, 197, 94, 0.4); }
            70% { box-shadow: 0 0 0 10px rgba(34, 197, 94, 0); }
            100% { box-shadow: 0 0 0 0 rgba(34, 197, 94, 0); }
        }

        /* 🔘 BUTTON WITH MOTION */
        .pricing-btn {
            display: block;
            text-align: center;
            background: linear-gradient(135deg, #2563eb, #1d4ed8);
            color: white !important;
            padding: 1rem;
            border-radius: 12px;
            text-decoration: none;
            font-weight: 700;
            margin-top: 2rem;
            transition: all 0.3s ease;
        }
        .pricing-btn:hover {
            letter-spacing: 1px;
            filter: brightness(1.1);
            box-shadow: 0 10px 15px -3px rgba(37, 99, 235, 0.4);
        }
        </style>
        """, unsafe_allow_html=True)

    # 3. CONTENT AREA
    st.markdown("<h1 style='text-align: center; color: #0f172a; font-weight: 800; font-size: 3rem; margin-bottom: 0;'>Triage Hub</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #64748b; font-size: 1.2rem; margin-bottom: 2rem;'>Motion Engine v2.6 | Watu Aftersales</p>", unsafe_allow_html=True)

    raw_input = st.text_input("", placeholder="Type symptom (e.g. 'cracked screen')")
    query = raw_input.lower().strip()

    if query:
        found = False
        for category, data in hermes.SAMSUNG_TRIAGE_DATA.items():
            if any(word in query for word in data["triggers"]):
                found = True
                
                # THE RESULT CARD
                st.markdown(f"""
                <div class="result-card">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <h2 style="margin: 0; color: #1e293b;">{category}</h2>
                        <span class="badge" style="background: #dcfce7; color: #166534;">
                            {"Warranty" if "In-Warranty" in data["warranty_status"] else "Out of Warranty"}
                        </span>
                    </div>
                    <p style="color: #3b82f6; font-weight: 700; margin-top: 10px; font-size: 0.9rem;">📍 {data["routing"]}</p>
                    <hr style="opacity: 0.1; margin: 1.5rem 0;">
                """, unsafe_allow_html=True)

                # Pricing Section
                if "Out of Warranty" in data["warranty_status"]:
                    st.markdown(f"""
                        <div style="background: #fffbeb; border: 1px dashed #f59e0b; padding: 1rem; border-radius: 12px; margin-bottom: 1rem;">
                            <p style="margin:0; color: #92400e; font-weight: bold;">PRICE REFERENCE NEEDED</p>
                            <a href="{hermes.PRICING_SHEET_URL}" target="_blank" class="pricing-btn">OPEN PRICING SHEET</a>
                        </div>
                    """, unsafe_allow_html=True)

                st.markdown("<p style='font-weight: 800; font-size: 0.8rem; color: #94a3b8; letter-spacing: 1px;'>EXECUTION PROTOCOL:</p>", unsafe_allow_html=True)
                for step in data["action_plan"]:
                    st.markdown(f"<p style='color: #475569; margin: 0.5rem 0; font-size: 1.05rem;'>⚡ {step}</p>", unsafe_allow_html=True)
                
                st.markdown(f"""
                    <div style="background: #eff6ff; padding: 1rem; border-radius: 12px; margin-top: 1.5rem; border-left: 5px solid #3b82f6;">
                        <p style="margin: 0; font-size: 0.95rem; color: #1e3a8a;"><b>Pro Tip:</b> {data['guidance']}</p>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                break

        if not found:
            st.warning("⚠️ Symptom unmapped. Escalate to SIMU HQ immediately.")

    # 4. FOOTER
    st.markdown("<p style='text-align: center; color: #94a3b8; font-weight: bold; margin-top: 4rem;'>SYSTEM STATUS: ONLINE | @SIMUREPAIRS</p>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
