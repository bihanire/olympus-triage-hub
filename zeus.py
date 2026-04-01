import streamlit as st
import hermes

st.set_page_config(page_title="Triage Hub", layout="wide", page_icon="📱")

def main():
    st.markdown("""
        <style>
        .stApp { background-color: #f7f9fc; }
        .main-card { background-color: #ffffff; border-radius: 12px; padding: 25px; border: 1px solid #e0e6ed; box-shadow: 0 4px 6px rgba(0,0,0,0.05); }
        .link-card { background-color: #e3f2fd; padding: 10px; border-radius: 8px; border-left: 5px solid #034EA2; margin-bottom: 10px; }
        </style>
        """, unsafe_allow_html=True)

    _, center, _ = st.columns([1, 2, 1])
    
    with center:
        st.title("Level-1 Triage & Diagnosis Tool 🛠️ 😊")
        st.caption("Updated with Transtel 30-Day Analysis Data")
        
        raw_input = st.text_input("", placeholder="Search: 'screen lines', 'update failed', 'forgot password'...")
        query = raw_input.lower().strip()

        if raw_input:
            found = False
            for category, data in hermes.SAMSUNG_TRIAGE_DATA.items():
                if any(word in query for word in data["triggers"]):
                    found = True
                    st.markdown("<div class='main-card'>", unsafe_allow_html=True)
                    st.subheader(f"Assessment: {category}")
                    
                    c1, c2 = st.columns(2)
                    with c1:
                        st.write("**Warranty Status**")
                        if "Out" in data["warranty_status"]: st.error(data["warranty_status"])
                        else: st.success(data["warranty_status"])
                    with c2:
                        st.write("**Routing**")
                        st.info(data["routing"])

                    st.divider()
                    st.write("**Mandatory Triage Steps:**")
                    for step in data["action_plan"]: st.write(f"🔹 {step}")
                    
                    st.divider()
                    st.info(f"**Customer Care:** {data['guidance']}")
                    st.markdown("</div>", unsafe_allow_html=True)
                    break

            if not found:
                st.warning("⚠️ Symptom not recognized. Refer to Senior Tech at Simu HQ.")

        # --- THE RESOURCE CENTER ---
        st.write("---")
        st.subheader("🔗 Assistance Links & Resources")
        l1, l2 = st.columns(2)
        with l1:
            st.markdown(f"<div class='link-card'>[Samsung Global Support]({hermes.RESOURCES['Samsung Support']})</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='link-card'>[Google Account Recovery]({hermes.RESOURCES['G-Mail Recovery']})</div>", unsafe_allow_html=True)
        with l2:
            st.write("📞 **Aftersales HQ Escalations:**")
            st.write("+256 700 000 000")
            st.caption("Suggest an update? [Click here to submit feedback]")

if __name__ == "__main__":
    main()
