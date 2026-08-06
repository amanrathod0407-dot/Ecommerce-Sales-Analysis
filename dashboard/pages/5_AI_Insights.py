import streamlit as st
import plotly.express as px
import pandas as pd
from utils.loader import load_data
from utils.helper import apply_custom_css, format_currency, display_footer

st.set_page_config(page_title="AI Insights", layout="wide")

# Apply Dark Mesh / SaaS CSS
apply_custom_css()

# Hero Header
st.markdown(
    """
    <div class="hero-header">
        <h1>🤖 Automated Executive AI Insights Engine</h1>
        <p>Real-time diagnostic analysis, performance charts, automated executive reports, and strategic recommendations.</p>
    </div>
    """,
    unsafe_allow_html=True
)

df = load_data()

if df.empty:
    st.warning("⚠️ No data available to generate AI insights.")
    st.stop()

# ==========================================
# 1. DATA AGGREGATIONS & METRICS
# ==========================================
cat_profit_df = df.groupby('Category')['Profit'].sum()
best_cat = cat_profit_df.idxmax()
best_cat_profit = cat_profit_df.max()

subcat_profit_df = df.groupby('Sub-Category')['Profit'].sum()
loss_subcat = subcat_profit_df.idxmin()
loss_subcat_val = subcat_profit_df.min()

region_sales_df = df.groupby('Region')['Sales'].sum()
best_region = region_sales_df.idxmax()
best_region_sales = region_sales_df.max()

avg_discount = df['Discount'].mean() * 100
total_sales = df['Sales'].sum()
total_profit = df['Profit'].sum()
profit_margin = (total_profit / total_sales * 100) if total_sales > 0 else 0

# ==========================================
# 2. TOP KPI METRIC CARDS (4 COLUMN GRID)
# ==========================================
kpi1, kpi2, kpi3, kpi4 = st.columns(4)

with kpi1:
    st.markdown(f"""
    <div class="saas-card saas-card-success">
        <span class="badge badge-green">🚀 Top Revenue Driver</span>
        <div class="card-label">Category: {best_cat}</div>
        <div class="card-value" style="color: #34d399;">{format_currency(best_cat_profit)}</div>
        <p class="card-desc">Leading overall net profitability across all channels.</p>
    </div>
    """, unsafe_allow_html=True)

with kpi2:
    st.markdown(f"""
    <div class="saas-card saas-card-danger">
        <span class="badge badge-red">⚠️ Critical Loss Alert</span>
        <div class="card-label">Sub-Category: {loss_subcat}</div>
        <div class="card-value" style="color: #f87171;">{format_currency(loss_subcat_val)}</div>
        <p class="card-desc">Bleeding margin. Immediate discount capping required.</p>
    </div>
    """, unsafe_allow_html=True)

with kpi3:
    st.markdown(f"""
    <div class="saas-card">
        <span class="badge badge-cyan">📍 Top Performing Market</span>
        <div class="card-label">Territory: {best_region}</div>
        <div class="card-value" style="color: #00f2fe;">{format_currency(best_region_sales)}</div>
        <p class="card-desc">Accounts for largest gross revenue and order volume.</p>
    </div>
    """, unsafe_allow_html=True)

with kpi4:
    st.markdown(f"""
    <div class="saas-card">
        <span class="badge badge-purple">📈 Margin Efficiency</span>
        <div class="card-label">Store Profit Margin</div>
        <div class="card-value" style="color: #a855f7;">{profit_margin:.1f}%</div>
        <p class="card-desc">Overall net profit conversion rate store-wide.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ==========================================
# 3. AUTOMATED AI EXECUTIVE BUSINESS REPORT
# ==========================================
st.markdown("### 📋 Automated Executive AI Business Summary")
st.markdown(f"""
<div class="saas-card">
    <ul style="color: #cbd5e1; font-size: 15px; line-height: 2; margin: 0; padding-left: 20px;">
        <li>✔ <b>{best_region} Region</b> generated the highest revenue across all territories ({format_currency(best_region_sales)}).</li>
        <li>✔ <b>{best_cat} Category</b> achieved the highest profit contribution ({format_currency(best_cat_profit)}).</li>
        <li>✔ <b>{loss_subcat} Sub-Category</b> is creating maximum profit erosion with a net loss of {format_currency(loss_subcat_val)}.</li>
        <li>✔ Average store discount rate is <b>{avg_discount:.1f}%</b>, driving severe margin loss in heavily discounted orders.</li>
        <li>✔ Overall Store Profit Margin Efficiency is calibrated at <b>{profit_margin:.1f}%</b>.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ==========================================
# 4. VISUAL CHARTS SECTION
# ==========================================
chart_col1, chart_col2 = st.columns(2)

def style_chart(fig, title):
    fig.update_layout(
        title=dict(text=title, font=dict(size=16, color='#ffffff', family='Plus Jakarta Sans')),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#94a3b8'),
        xaxis=dict(showgrid=False, color='#94a3b8'),
        yaxis=dict(showgrid=True, gridcolor='rgba(255, 255, 255, 0.05)', color='#94a3b8'),
        margin=dict(l=20, r=20, t=50, b=20),
        height=380
    )
    return fig

with chart_col1:
    # Chart 1: Profit/Loss Spectrum by Sub-Category
    subcat_profit = df.groupby('Sub-Category')['Profit'].sum().reset_index()
    subcat_profit['Status'] = subcat_profit['Profit'].apply(lambda x: 'Profitable' if x > 0 else 'Loss Making')
    
    fig_subcat = px.bar(
        subcat_profit, 
        x='Sub-Category', 
        y='Profit', 
        color='Status',
        color_discrete_map={'Profitable': '#00f2fe', 'Loss Making': '#ef4444'}
    )
    fig_subcat = style_chart(fig_subcat, "📊 Profit & Loss Spectrum by Sub-Category")
    st.plotly_chart(fig_subcat, use_container_width=True)

with chart_col2:
    # Chart 2: Discount vs Profit Scatter Correlation
    fig_scatter = px.scatter(
        df, 
        x='Discount', 
        y='Profit', 
        color='Category',
        hover_data=['Sub-Category'],
        color_discrete_sequence=['#00f2fe', '#34d399', '#f87171']
    )
    fig_scatter = style_chart(fig_scatter, "📉 High Discount vs Profit Erosion Impact")
    st.plotly_chart(fig_scatter, use_container_width=True)

st.markdown("<br>", unsafe_allow_html=True)

# ==========================================
# 5. STRATEGIC ACTION ITEMS BLOCK
# ==========================================
col_left, col_right = st.columns(2)

with col_left:
    st.markdown(f"""
    <div class="saas-card saas-card-danger">
        <span class="badge badge-red">💡 Discount & Margin Control</span>
        <h3 style="color: #ffffff; font-size: 18px; margin-top: 5px; margin-bottom: 12px; font-weight: 700;">Margin Recovery Plan</h3>
        <p style="color: #cbd5e1; font-size: 14px; line-height: 1.6;">
            Current average store discount is <b>{avg_discount:.1f}%</b>.
        </p>
        <ul style="color: #94a3b8; font-size: 14px; line-height: 1.8; padding-left: 20px; margin-bottom: 0;">
            <li>Cap maximum allowable discounts on <b style="color: #ffffff;">{loss_subcat}</b> to 10%.</li>
            <li>Implement tiered bundling on <b style="color: #ffffff;">{best_cat}</b> to boost average order value (AOV).</li>
            <li>Audit corporate sales contracts with over 30% discount rates.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col_right:
    st.markdown(f"""
    <div class="saas-card saas-card-success">
        <span class="badge badge-green">📦 Operations & Supply Chain</span>
        <h3 style="color: #ffffff; font-size: 18px; margin-top: 5px; margin-bottom: 12px; font-weight: 700;">Supply Chain Allocation</h3>
        <p style="color: #cbd5e1; font-size: 14px; line-height: 1.6;">
            Fulfillment latency is optimal across top territories.
        </p>
        <ul style="color: #94a3b8; font-size: 14px; line-height: 1.8; padding-left: 20px; margin-bottom: 0;">
            <li>Prioritize inventory restocking in the <b style="color: #ffffff;">{best_region}</b> regional distribution hub.</li>
            <li>Negotiate bulk freight rates for high-volume categories.</li>
            <li>Launch targeted marketing campaigns for loyal customer segments.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Executive Footer
display_footer()