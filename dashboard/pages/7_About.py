import streamlit as st
from utils.helper import apply_custom_css, display_footer

st.set_page_config(page_title="About Project", layout="wide")
apply_custom_css()

st.markdown("""
<div class="hero-header">
    <h1>📄 About This Project & Developer</h1>
    <p>Architecture details, technology stack, and developer profile.</p>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    <div class="saas-card">
        <h3 style="color: #00f2fe; margin-top: 0;">📊 E-Commerce Business Intelligence Engine</h3>
        <p style="color: #cbd5e1; line-height: 1.6;">
            This project is an end-to-end Data Analytics & Business Intelligence Dashboard designed to transform raw e-commerce transaction logs into actionable executive insights. 
            It features multi-dimensional filtering, interactive charts, automated AI business reporting, and dynamic KPI tracking.
        </p>
        <h4 style="color: #ffffff; margin-top: 20px;">🛠️ Technology Stack</h4>
        <div style="display: flex; gap: 10px; flex-wrap: wrap; margin-top: 10px;">
            <span class="badge badge-cyan">Python</span>
            <span class="badge badge-cyan">Pandas</span>
            <span class="badge badge-cyan">Streamlit</span>
            <span class="badge badge-cyan">Plotly</span>
            <span class="badge badge-cyan">SQL</span>
            <span class="badge badge-cyan">Power BI</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="saas-card">
        <h3 style="color: #34d399; margin-top: 0;">👨‍💻 Developer Profile</h3>
        <p style="color: #ffffff; font-size: 18px; font-weight: 700; margin-bottom: 4px;">Aman Rathod</p>
        <p style="color: #94a3b8; font-size: 14px; margin-top: 0;">Full-Stack Developer & Data Analytics Enthusiast</p>
        <hr style="border-color: rgba(255,255,255,0.1);">
        <p style="color: #cbd5e1; font-size: 13px; line-height: 1.8;">
            <b>Focus:</b> Data Analytics, Business Intelligence, Full-Stack Web App Development<br>
            <b>Portfolio Goal:</b> Building high-impact, production-ready SaaS dashboards and intelligent tools.
        </p>
    </div>
    """, unsafe_allow_html=True)

display_footer()