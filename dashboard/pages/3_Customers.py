import streamlit as st
import plotly.express as px
from utils.loader import load_data
from utils.helper import apply_custom_css, format_currency, display_footer

st.set_page_config(page_title="Customer Intelligence", layout="wide")
apply_custom_css()

st.markdown("""
<div class="hero-header">
    <h1>👥 Customer Intelligence & Segmentation</h1>
    <p>Analyze Customer Lifetime Value (CLV), purchasing behavior, and segment distribution.</p>
</div>
""", unsafe_allow_html=True)

df = load_data()

# Customer Top KPIs
c1, c2 = st.columns(2)

with c1:
    seg_sales = df.groupby('Segment')['Sales'].sum().reset_index()
    fig_donut = px.pie(seg_sales, values='Sales', names='Segment', hole=0.6, color_discrete_sequence=['#00f2fe', '#34d399', '#f59e0b'])
    fig_donut.update_layout(
        title=dict(text="🍩 Customer Segment Distribution", font=dict(color='#ffffff')),
        paper_bgcolor='rgba(0,0,0,0)', font=dict(color='#94a3b8'), height=350
    )
    st.plotly_chart(fig_donut, use_container_width=True)

with c2:
    if 'Customer Name' in df.columns:
        top_cust = df.groupby('Customer Name')['Sales'].sum().nlargest(10).reset_index()
        fig_cust = px.bar(top_cust, x='Sales', y='Customer Name', orientation='h', color='Sales', color_continuous_scale='Purples')
        fig_cust.update_layout(
            title=dict(text="⭐ Top 10 Customers by Revenue (CLV)", font=dict(color='#ffffff')),
            paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font=dict(color='#94a3b8'), height=350,
            yaxis=dict(autorange="reversed")
        )
        st.plotly_chart(fig_cust, use_container_width=True)

display_footer()