import streamlit as st
import plotly.express as px
from utils.loader import load_data
from utils.helper import apply_custom_css, format_currency, format_number, display_footer

st.set_page_config(
    page_title="E-Commerce BI Engine",
    page_icon="📊",
    layout="wide"
)

apply_custom_css()

# Hero Banner
st.markdown(
    """
    <div class="hero-header">
        <h1>📊 E-Commerce Business Intelligence Engine</h1>
        <p>Interactive Sales Analytics Dashboard • Built using <b>Python, SQL, Streamlit, Plotly & Power BI</b></p>
    </div>
    """,
    unsafe_allow_html=True
)

df = load_data()

# 1. Top KPI Scorecards
kpi1, kpi2, kpi3, kpi4 = st.columns(4)

total_sales = df['Sales'].sum()
total_profit = df['Profit'].sum()
total_orders = df['Order ID'].nunique() if 'Order ID' in df.columns else len(df)
total_customers = df['Customer ID'].nunique() if 'Customer ID' in df.columns else 0

with kpi1:
    st.markdown(f"""
    <div class="saas-card">
        <div class="card-label">💰 Total Sales</div>
        <div class="card-value" style="color: #00f2fe;">{format_currency(total_sales)}</div>
        <p class="card-desc">Gross Revenue Generated</p>
    </div>
    """, unsafe_allow_html=True)

with kpi2:
    st.markdown(f"""
    <div class="saas-card">
        <div class="card-label">💵 Total Profit</div>
        <div class="card-value" style="color: #34d399;">{format_currency(total_profit)}</div>
        <p class="card-desc">Net Returns Post Discounts</p>
    </div>
    """, unsafe_allow_html=True)

with kpi3:
    st.markdown(f"""
    <div class="saas-card">
        <div class="card-label">📦 Total Orders</div>
        <div class="card-value" style="color: #a855f7;">{format_number(total_orders)}</div>
        <p class="card-desc">Completed Transactions</p>
    </div>
    """, unsafe_allow_html=True)

with kpi4:
    st.markdown(f"""
    <div class="saas-card">
        <div class="card-label">👥 Unique Customers</div>
        <div class="card-value" style="color: #f59e0b;">{format_number(total_customers)}</div>
        <p class="card-desc">Active Account Base</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# 2. Executive Summaries (Quick Snapshot Grid)
col_left, col_right = st.columns(2)

top_region = df.groupby('Region')['Sales'].sum().idxmax()
top_category = df.groupby('Category')['Sales'].sum().idxmax()
top_segment = df.groupby('Segment')['Sales'].sum().idxmax()

with col_left:
    st.markdown("### 🚀 Strategic Highlights")
    st.markdown(f"""
    <div class="saas-card">
        <ul style="color: #cbd5e1; font-size: 15px; line-height: 2; margin: 0; padding-left: 20px;">
            <li>📍 <b>Top Region:</b> <span style="color: #00f2fe;">{top_region}</span> (Highest revenue driver)</li>
            <li>🏷️ <b>Top Category:</b> <span style="color: #34d399;">{top_category}</span> (Maximum margin share)</li>
            <li>🏢 <b>Top Segment:</b> <span style="color: #a855f7;">{top_segment}</span> (Largest purchasing volume)</li>
            <li>📊 <b>Profit Margin Rate:</b> <span style="color: #f59e0b;">{(total_profit/total_sales*100):.1f}%</span> store-wide efficiency</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col_right:
    st.markdown("### ⚡ Quick Navigation")
    st.markdown("""
    <div class="saas-card">
        <p style="color: #94a3b8; margin-bottom: 10px;">Select any analytics module from the left sidebar:</p>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
            <div style="background: rgba(255,255,255,0.05); padding: 10px; border-radius: 8px;"><b>📈 Sales:</b> Trends & Regional Analysis</div>
            <div style="background: rgba(255,255,255,0.05); padding: 10px; border-radius: 8px;"><b>👥 Customers:</b> LTV & Segmentation</div>
            <div style="background: rgba(255,255,255,0.05); padding: 10px; border-radius: 8px;"><b>📦 Products:</b> Treemap & Profitability</div>
            <div style="background: rgba(255,255,255,0.05); padding: 10px; border-radius: 8px;"><b>🤖 AI Insights:</b> Auto Business Reports</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

display_footer()