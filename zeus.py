import streamlit as st
import hermes

# Page Configuration
st.set_page_config(page_title="Watu Triage Hub", layout="centered", page_icon="📱")

def main():
    # THE DESIGN ENGINE
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
        html, body, [class*="css"] { font-family: 'Inter', sans-serif; background-color: #F8FAFC; }
        #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
        .main-card { background: white; padding: 2rem; border-radius: 16px; box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1); border: 1px solid #E2E8F0; margin-top: 2rem; }
        .stTextInput > div > div > input { border-radius: 12px; border: 2px solid #E2E8F0; padding: 1rem; font-size: 1.1rem; }
        .badge-warranty { background-color: #DCFCE7; color: #166534; padding: 4px 12px; border-radius: 99px; font-weight: 600; font-size: 0.85rem; }
        .pricing-btn { display: inline-block; background-color: #2563EB; color: white !important; padding: 12px 24px; border-radius: 8px; text-decoration: none; font-weight: 600; margin-top: 1rem; transition: background 0.3s; }
        .pricing-btn:hover { background-color: #1E40AF; }
        .custom-footer { text-align: center; padding: 3rem 0; color: #64748B; font-size: 0.9rem; font-weight: bold; }
        </style>
        """, unsafe_allow_html=True)

    st.markdown("<h1 style='text-align: center; color: #1E293B; margin-bottom: 0;'>Triage Hub</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #64748B; font-size: 1.1rem;'>Watu Aftersales | Diagnostic Engine v2.5</p>", unsafe_allow_html=True)

    raw_input = st.text_input("", placeholder="Search: 'battery drain', 'lines', 'cannot update'...")
    query = raw_input.lower().strip()

    if query:
        found = False
        for category, data in hermes.SAMSUNG_TRIAGE_DATA.items():
            if any(word in query for word in data["triggers"]):
                found = True
                
                st.markdown(f"""
                <div class="main-card">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
                        <h3 style="margin: 0; color: #0F172A;">{category}</h3>
                        <span class="badge-warranty">{"In Warranty" if "In-Warranty" in data["warranty_status"] else "Out of Warranty"}</span>
                    </div>
                    <p style="color: #475569; font-weight: 600;">Routing: <span style="color: #2563EB;">{data["routing"]}</span></p>
                """, unsafe_allow_html=True)

                # DYNAMIC PRICING BUTTON FOR OUT-OF-WARRANTY
                if "Out of Warranty" in data["warranty_status"]:
                    st.markdown(f"""
                        <div style="background: #FFFBEB; padding: 1rem; border-radius: 8px; border: 1px solid #FDE68A; margin-bottom: 1.5rem;">
                            <p style="margin: 0; color: #92400E; font-weight: 700;">💰 REPAIR PRICING REQUIRED</p>
                            <p style="margin: 0; font-size: 0.85rem; color: #B45309;">Refer to the official Samsung Pricing Sheet for quotes.</p>
                            <a href="{hermes.PRICING_SHEET_URL}" target="_blank" class="pricing-btn">Open Pricing Sheet v3.1</a>
                        </div>
                    """, unsafe_allow_html=True)

                st.markdown("<p style='color: #1E293B; font-weight: 700; margin-bottom: 0.5rem;'>PROTOCOL STEPS:</p>", unsafe_allow_html=True)
                for step in data["action_plan"]:
                    st.markdown(f"<p style='color: #475569; margin: 0.3rem 0;'>• {step}</p>", unsafe_allow_html=True)
                
                st.markdown(f"""
                    <div style="background: #F8FAFC; padding: 1rem; border-radius: 8px; margin-top: 1.5rem; border-left: 4px solid #2563EB;">
                        <p style="margin: 0; font-size: 0.9rem; color: #1E293B;"><b>Staff Note:</b> {data['guidance']}</p>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                break

        if not found:
            st.error("⚠️ Symptom not recognized. Manual inspection required at Simu HQ.")

    st.markdown("<div class='custom-footer'>REPORT AN ISSUE: @SIMUREPAIRS</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
