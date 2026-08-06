import streamlit as st
import plotly.express as px
import pandas as pd
from utils.loader import load_data
from utils.helper import apply_custom_css, format_currency

st.set_page_config(page_title="PowerBI Executive View", layout="wide")

# Apply Dark SaaS Theme
apply_custom_css()

# Header
st.markdown(
    """
    <div class="hero-header">
        <h1>📊 PowerBI Interactive Workspace</h1>
        <p>Slice, dice, and dynamically filter store-wide performance metrics.</p>
    </div>
    """,
    unsafe_allow_html=True
)

df = load_data()

# ==========================================
# 1. POWER BI SLICER / FILTER PANEL
# ==========================================
st.markdown("### 🔍 Slicers & Filters")
f_col1, f_col2, f_col3 = st.columns(3)

with f_col1:
    selected_region = st.multiselect(
        "Select Region:",
        options=df['Region'].unique(),
        default=df['Region'].unique()
    )

with f_col2:
    selected_category = st.multiselect(
        "Select Category:",
        options=df['Category'].unique(),
        default=df['Category'].unique()
    )

with f_col3:
    selected_segment = st.multiselect(
        "Select Segment:",
        options=df['Segment'].unique(),
        default=df['Segment'].unique()
    )

# Apply Dynamic Filters
filtered_df = df[
    (df['Region'].isin(selected_region)) &
    (df['Category'].isin(selected_category)) &
    (df['Segment'].isin(selected_segment))
]

if filtered_df.empty:
    st.warning("⚠️ No data available for the selected slicer filters.")
    st.stop()

st.markdown("<br>", unsafe_allow_html=True)

# ==========================================
# 2. POWER BI KPI SCORECARD TILES
# ==========================================
total_sales = filtered_df['Sales'].sum()
total_profit = filtered_df['Profit'].sum()
total_orders = filtered_df['Order ID'].nunique() if 'Order ID' in filtered_df.columns else len(filtered_df)
profit_margin = (total_profit / total_sales * 100) if total_sales > 0 else 0

k1, k2, k3, k4 = st.columns(4)

with k1:
    st.markdown(f"""
    <div class="saas-card">
        <div class="card-label">Total Sales</div>
        <div class="card-value" style="color: #00f2fe;">{format_currency(total_sales)}</div>
        <p class="card-desc">Gross Revenue Generated</p>
    </div>
    """, unsafe_allow_html=True)

with k2:
    profit_color = "#34d399" if total_profit >= 0 else "#f87171"
    st.markdown(f"""
    <div class="saas-card">
        <div class="card-label">Net Profit</div>
        <div class="card-value" style="color: {profit_color};">{format_currency(total_profit)}</div>
        <p class="card-desc">Total Profit / Loss Impact</p>
    </div>
    """, unsafe_allow_html=True)

with k3:
    st.markdown(f"""
    <div class="saas-card">
        <div class="card-label">Total Orders</div>
        <div class="card-value" style="color: #a855f7;">{total_orders:,}</div>
        <p class="card-desc">Unique Transactions</p>
    </div>
    """, unsafe_allow_html=True)

with k4:
    st.markdown(f"""
    <div class="saas-card">
        <div class="card-label">Profit Margin %</div>
        <div class="card-value" style="color: #f59e0b;">{profit_margin:.1f}%</div>
        <p class="card-desc">Margin Efficiency Rate</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ==========================================
# 3. CORE VISUAL GRID (POWER BI STYLE)
# ==========================================
def style_pbi_chart(fig, title):
    fig.update_layout(
        title=dict(text=title, font=dict(size=15, color='#ffffff', family='Plus Jakarta Sans')),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#94a3b8'),
        xaxis=dict(showgrid=False, color='#94a3b8'),
        yaxis=dict(showgrid=True, gridcolor='rgba(255, 255, 255, 0.05)', color='#94a3b8'),
        margin=dict(l=15, r=15, t=45, b=15),
        height=350
    )
    return fig

r1_c1, r1_c2 = st.columns(2)

with r1_c1:
    cat_sales = filtered_df.groupby('Category')['Sales'].sum().reset_index()
    fig_donut = px.pie(
        cat_sales, values='Sales', names='Category', hole=0.5,
        color_discrete_sequence=['#00f2fe', '#3b82f6', '#34d399']
    )
    fig_donut = style_pbi_chart(fig_donut, "🍩 Sales Distribution by Category")
    st.plotly_chart(fig_donut, use_container_width=True)

with r1_c2:
    subcat_sales = filtered_df.groupby(['Category', 'Sub-Category'])['Sales'].sum().reset_index()
    fig_tree = px.treemap(
        subcat_sales, path=['Category', 'Sub-Category'], values='Sales',
        color='Sales', color_continuous_scale='Blugrn'
    )
    fig_tree = style_pbi_chart(fig_tree, "🌳 Sub-Category Revenue Tree")
    st.plotly_chart(fig_tree, use_container_width=True)

r2_c1, r2_c2 = st.columns(2)

with r2_c1:
    reg_seg = filtered_df.groupby(['Region', 'Segment'])['Sales'].sum().reset_index()
    fig_stack = px.bar(
        reg_seg, x='Region', y='Sales', color='Segment', barmode='stack',
        color_discrete_sequence=['#00f2fe', '#a855f7', '#f59e0b']
    )
    fig_stack = style_pbi_chart(fig_stack, "📊 Regional Sales by Customer Segment")
    st.plotly_chart(fig_stack, use_container_width=True)

with r2_c2:
    if 'Month_Year' in filtered_df.columns:
        trend_data = filtered_df.groupby('Month_Year')['Sales'].sum().reset_index()
        fig_line = px.line(trend_data, x='Month_Year', y='Sales', markers=True)
        fig_line.update_traces(line_color='#34d399', line_width=3)
        fig_line = style_pbi_chart(fig_line, "📈 Revenue Trendline")
        st.plotly_chart(fig_line, use_container_width=True)

st.markdown("<br>", unsafe_allow_html=True)

# ==========================================
# 4. POWER BI DATA MATRIX VIEW
# ==========================================
with st.expander("📋 View Underlying Data Matrix (PowerBI Table View)", expanded=False):
    summary_matrix = filtered_df.groupby(['Category', 'Sub-Category']).agg(
        Total_Sales=('Sales', 'sum'),
        Total_Profit=('Profit', 'sum'),
        Avg_Discount=('Discount', 'mean')
    ).reset_index()
    
    summary_matrix['Avg_Discount'] = (summary_matrix['Avg_Discount'] * 100).round(1).astype(str) + '%'
    summary_matrix['Total_Sales'] = summary_matrix['Total_Sales'].apply(format_currency)
    summary_matrix['Total_Profit'] = summary_matrix['Total_Profit'].apply(format_currency)
    
    st.dataframe(summary_matrix, use_container_width=True)