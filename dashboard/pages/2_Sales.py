import streamlit as st
import plotly.express as px
from utils.loader import load_data
from utils.helper import apply_custom_css, format_currency, display_footer

st.set_page_config(page_title="Sales Analytics", layout="wide")
apply_custom_css()

st.markdown("""
<div class="hero-header">
    <h1>📈 Sales Performance & Revenue Dynamics</h1>
    <p>Comprehensive breakdown of revenue streams, discounting risks, and regional performance.</p>
</div>
""", unsafe_allow_html=True)

df = load_data()

# Filter Bar at Top
st.markdown("### 🔍 Global Slicers")
c1, c2, c3 = st.columns(3)

with c1:
    selected_region = st.multiselect("Region:", options=df['Region'].unique(), default=df['Region'].unique())
with c2:
    selected_category = st.multiselect("Category:", options=df['Category'].unique(), default=df['Category'].unique())
with c3:
    selected_segment = st.multiselect("Segment:", options=df['Segment'].unique(), default=df['Segment'].unique())

filtered = df[(df['Region'].isin(selected_region)) & (df['Category'].isin(selected_category)) & (df['Segment'].isin(selected_segment))]

if filtered.empty:
    st.warning("No data found for selected filters.")
    st.stop()

# Helper Chart Style
def style_chart(fig, title):
    fig.update_layout(
        title=dict(text=title, font=dict(size=15, color='#ffffff')),
        paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#94a3b8'),
        margin=dict(l=15, r=15, t=45, b=15), height=350
    )
    return fig

# Grid Row 1
r1c1, r1c2 = st.columns(2)

with r1c1:
    reg_sales = filtered.groupby('Region')['Sales'].sum().reset_index()
    fig1 = px.bar(reg_sales, x='Region', y='Sales', color='Sales', color_continuous_scale='Blues')
    st.plotly_chart(style_chart(fig1, "📍 Regional Sales Breakdown"), use_container_width=True)

with r1c2:
    if 'Month_Year' in filtered.columns:
        trend = filtered.groupby('Month_Year')['Sales'].sum().reset_index()
        fig2 = px.line(trend, x='Month_Year', y='Sales', markers=True)
        fig2.update_traces(line_color='#00f2fe', line_width=3)
        st.plotly_chart(style_chart(fig2, "📈 Monthly Revenue Trendline"), use_container_width=True)

# Grid Row 2
r2c1, r2c2 = st.columns(2)

with r2c1:
    fig3 = px.scatter(filtered, x='Discount', y='Profit', color='Category', hover_data=['Sub-Category'])
    st.plotly_chart(style_chart(fig3, "📉 Discount vs. Profit Erosion Impact"), use_container_width=True)

with r2c2:
    cat_profit = filtered.groupby('Category')['Profit'].sum().reset_index()
    fig4 = px.bar(cat_profit, x='Category', y='Profit', color='Profit', color_continuous_scale='Tealgrn')
    st.plotly_chart(style_chart(fig4, "💵 Net Profit Distribution by Category"), use_container_width=True)

display_footer()