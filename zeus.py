import streamlit as st
import hermes

# Final Clean, Professional Layout
st.set_page_config(page_title="Triage Hub", layout="wide")

def main():
    # minimalist Industrial CSS (The "Efficient Kid" Look)
    st.markdown("""
        <style>
        .stApp { background-color: #fafafa; }
        .main-card {
            background-color: #ffffff;
            border-radius: 8px;
            padding: 30px;
            border: 1px solid #ddd;
            box-shadow: 0 4px 6px rgba(0,0,0,0.05);
            margin-bottom: 25px;
        }
        .stTextInput > div > div > input { border-radius: 8px; border: 1px solid #c0c0c0; }
        h2 { color: #333333; font-family: 'Segoe UI', sans-serif; text-align: center; margin-bottom: 30px; }
        h3 { color: #1e3a8a; }
        </style>
        """, unsafe_allow_html=True)

    # Use columns to center the input hub
    _, center, _ = st.columns([1, 2, 1])
    
    with center:
        # --- HUMBLE PITCH TITLE ---
        st.markdown("<h2>Level-1 Triage, Warranty & Diagnosis Tool 🛠️ 😊</h2>", unsafe_allow_html=True)
        
        # --- Simplified Intake Area ---
        st.write("Technical Support Protocol | Standardized Triage")
        raw_input = st.text_input("", placeholder="Enter symptom (e.g. 'cracked screen' or 'forgot pattern')")
        complaint = raw_input.lower().strip()

        if raw_input:
            st.write("---")
            found = False
            for category, data in hermes.SAMSUNG_TRIAGE_DATA.items():
                if any(word in complaint for word in data["triggers"]):
                    found = True
                    
                    st.markdown("<div class='main-card'>", unsafe_allow_html=True)
                    st.subheader(f"🛠️ Assessment: {category}")
                    
                    col1, col2 = st.columns(2)
                    with col1:
                        st.markdown("**Warranty Status**")
                        if "Out" in data["warranty_status"]:
                            st.error(data["warranty_status"])
                        else:
                            st.success(data["warranty_status"])
                    
                    with col2:
                        st.markdown("**Primary Routing**")
                        st.info(data["routing"])

                    st.markdown("---")
                    
                    # Steps & Communication
                    t_col, c_col = st.columns([3, 2])
                    with t_col:
                        st.markdown("**Mandatory Triage Steps:**")
                        for step in data["action_plan"]:
                            st.write(f"🔹 {step}")
                        
                        if "TRANSTEL" in data["routing"] and "Out" in data["warranty_status"]:
                            st.warning("📣 **Note:** Consult the Repair Pricing Chart for cost estimation.")
                    
                    with c_col:
                        st.markdown("**Customer Service Note:**")
                        st.info(data["guidance"])
                    
                    st.markdown("---")
                    
                    # Quick Procedures
                    with st.expander("Technical Reference Guides"):
                        p1, p2 = st.columns(2)
                        with p1:
                            st.write("**LDI Check:**", hermes.PROCEDURES["LDI Check"])
                        with p2:
                            st.write("**Hardware Test:**", hermes.PROCEDURES["Hardware Test"])
                    
                    st.markdown("</div>", unsafe_allow_html=True)
                    break

            if not found:
                st.warning("⚠️ Symptom not recognized. Manual physical inspection required. Contact HQ.")

if __name__ == "__main__":
    main()