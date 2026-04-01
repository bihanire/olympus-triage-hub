import streamlit as st
import hermes

st.set_page_config(page_title="Triage Hub", layout="wide", page_icon="📱")

def main():
    st.markdown("""
        <style>
        .stApp { background-color: #f7f9fc; }
        .main-card { background-color: #ffffff; border-radius: 12px; padding: 25px; border: 1px solid #e0e6ed; box-shadow: 0 4px 6px rgba(0,0,0,0.05); }
        .footer { text-align: center; color: #666; padding: 20px; border-top: 1px solid #ddd; margin-top: 50px; }
        </style>
        """, unsafe_allow_html=True)

    _, center, _ = st.columns([1, 2, 1])
    
    with center:
        st.title("Level-1 Triage, Warranty & Diagnosis Tool 🛠️ 😊")
        st.caption("Standardizing Aftersales Triage for Watu Branches")
        
        raw_input = st.text_input("", placeholder="Search: 'battery', 'unresponsive', 'lines', 'failed update'...")
        query = raw_input.lower().strip()

        if query:
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
                        st.write("**Routing Path**")
                        st.info(data["routing"])

                    st.write("---")
                    st.write("**Mandatory Triage Steps:**")
                    for step in data["action_plan"]: st.write(f"🔹 {step}")
                    
                    st.write("---")
                    st.info(f"**Care Note:** {data['guidance']}")
                    st.markdown("</div>", unsafe_allow_html=True)
                    break

            if not found:
                st.warning("Symptom not recognized. Manual physical inspection required.")

        # --- FEEDBACK & COMPLAINTS ---
        st.write("---")
        st.subheader("📬 Support & Feedback")
        col_a, col_b = st.columns(2)
        with col_a:
            st.write("**Report an Issue / Complaint:**")
            st.write(f"📧 [simurepairs@watu.africa](mailto:simurepairs@watu.africa)")
        with col_b:
            with st.expander("💡 Suggest an Improvement"):
                st.text_area("Missing a symptom? Let us know:")
                if st.button("Send Feedback"):
                    st.toast("Success! Feedback sent to Aftersales HQ.")

if __name__ == "__main__":
    main()
