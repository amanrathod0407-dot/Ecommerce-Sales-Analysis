import streamlit as st
import plotly.express as px
from utils.loader import load_data
from utils.helper import apply_custom_css, format_currency, display_footer

st.set_page_config(page_title="Product Analytics", layout="wide")
apply_custom_css()

st.markdown("""
<div class="hero-header">
    <h1>📦 Product & Portfolio Analytics</h1>
    <p>Hierarchy treemaps, top-performing catalog items, and profit margins.</p>
</div>
""", unsafe_allow_html=True)

df = load_data()

# Treemap Visual
subcat_sales = df.groupby(['Category', 'Sub-Category'])['Sales'].sum().reset_index()
fig_tree = px.treemap(subcat_sales, path=['Category', 'Sub-Category'], values='Sales', color='Sales', color_continuous_scale='Viridis')
fig_tree.update_layout(
    title=dict(text="🌳 Catalog Hierarchy & Revenue Treemap", font=dict(color='#ffffff')),
    paper_bgcolor='rgba(0,0,0,0)', font=dict(color='#94a3b8'), height=400
)
st.plotly_chart(fig_tree, use_container_width=True)

col1, col2 = st.columns(2)

with col1:
    if 'Product Name' in df.columns:
        top_prod = df.groupby('Product Name')['Sales'].sum().nlargest(10).reset_index()
        fig_prod = px.bar(top_prod, x='Sales', y='Product Name', orientation='h', color_discrete_sequence=['#00f2fe'])
        fig_prod.update_layout(
            title=dict(text="🏆 Top 10 Revenue Generating Products", font=dict(color='#ffffff')),
            paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font=dict(color='#94a3b8'), height=380,
            yaxis=dict(autorange="reversed")
        )
        st.plotly_chart(fig_prod, use_container_width=True)

with col2:
    margin_subcat = df.groupby('Sub-Category')[['Sales', 'Profit']].sum().reset_index()
    margin_subcat['Margin_%'] = (margin_subcat['Profit'] / margin_subcat['Sales'] * 100).round(1)
    fig_margin = px.bar(margin_subcat, x='Sub-Category', y='Margin_%', color='Margin_%', color_continuous_scale='RdYlGn')
    fig_margin.update_layout(
        title=dict(text="📊 Profit Margin Efficiency % by Sub-Category", font=dict(color='#ffffff')),
        paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font=dict(color='#94a3b8'), height=380
    )
    st.plotly_chart(fig_margin, use_container_width=True)

display_footer()