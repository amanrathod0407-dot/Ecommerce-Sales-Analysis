import streamlit as st
import plotly.express as px
import pandas as pd
from utils.loader import load_data
from utils.helper import apply_custom_css, render_kpi, format_currency, format_number, display_footer

st.set_page_config(page_title="Executive Overview", layout="wide")

# Apply Dark SaaS Theme CSS
apply_custom_css()

st.markdown("""
<div class="hero-header">
    <h1>🏠 Executive Overview</h1>
    <p>Real-time enterprise sales performance, operational metrics, and business trends.</p>
</div>
""", unsafe_allow_html=True)

df = load_data()

if df.empty:
    st.warning("⚠️ No data available to display.")
    st.stop()

# Sidebar Filters
st.sidebar.header("Filter Options")

if "Region" in df.columns:
    selected_region = st.sidebar.multiselect(
        "Select Region",
        options=df["Region"].unique(),
        default=df["Region"].unique()
    )
    filtered_df = df[df["Region"].isin(selected_region)] if selected_region else df
else:
    filtered_df = df

# ==========================================
# KPI METRICS CALCULATION
# ==========================================
total_sales = filtered_df['Sales'].sum() if 'Sales' in filtered_df.columns else 0
total_profit = filtered_df['Profit'].sum() if 'Profit' in filtered_df.columns else 0
total_orders = filtered_df['Order ID'].nunique() if 'Order ID' in filtered_df.columns else len(filtered_df)
margin = (total_profit / total_sales * 100) if total_sales > 0 else 0

# RENDER KPI CARDS (4 COLUMN GRID)
k1, k2, k3, k4 = st.columns(4)

with k1:
    render_kpi("Total Sales", format_currency(total_sales), "Gross Revenue Generated", "#00f2fe")

with k2:
    render_kpi("Total Profit", format_currency(total_profit), "Net Profit Margin", "#34d399")

with k3:
    render_kpi("Total Orders", format_number(total_orders), "Completed Orders", "#fbbf24")

with k4:
    render_kpi("Profit Margin", f"{margin:.1f}%", "Overall Conversion Efficiency", "#a855f7")

st.markdown("<br>", unsafe_allow_html=True)

# ==========================================
# INTERACTIVE CHARTS
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
    if "Order Date" in filtered_df.columns and "Sales" in filtered_df.columns:
        trend_df = filtered_df.copy()
        trend_df['Order Date'] = pd.to_datetime(trend_df['Order Date'])
        monthly_sales = trend_df.resample('ME', on='Order Date')['Sales'].sum().reset_index()
        
        fig_trend = px.line(
            monthly_sales, 
            x='Order Date', 
            y='Sales',
            markers=True,
            line_shape='spline'
        )
        fig_trend.update_traces(line_color='#00f2fe', line_width=3)
        fig_trend = style_chart(fig_trend, "📈 Monthly Revenue Trend")
        st.plotly_chart(fig_trend, use_container_width=True)

with chart_col2:
    if "Category" in filtered_df.columns and "Sales" in filtered_df.columns:
        cat_sales = filtered_df.groupby('Category')['Sales'].sum().reset_index()
        fig_cat = px.bar(
            cat_sales, 
            x='Category', 
            y='Sales',
            color='Category',
            color_discrete_sequence=['#00f2fe', '#34d399', '#f87171']
        )
        fig_cat = style_chart(fig_cat, "📦 Revenue Contribution by Category")
        st.plotly_chart(fig_cat, use_container_width=True)

# Executive Footer
display_footer()