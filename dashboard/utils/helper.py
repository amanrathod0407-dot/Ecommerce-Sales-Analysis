import streamlit as st
import pandas as pd
import os

def apply_custom_css():
    """Reads assets/style.css and injects it into Streamlit"""
    css_path = os.path.join("assets", "style.css")
    if os.path.exists(css_path):
        with open(css_path, "r", encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def format_currency(value):
    """Formats raw numbers into currency strings ($1.23M, $12.3K, $123.45)"""
    if value is None:
        return "$0.00"
    if abs(value) >= 1_000_000:
        return f"${value/1_000_000:.2f}M"
    elif abs(value) >= 1_000:
        return f"${value/1_000:.1f}K"
    return f"${value:,.2f}"

def format_number(value):
    """Formats numbers with comma separators (1,234)"""
    if value is None:
        return "0"
    return f"{value:,}"

def render_kpi(title_or_df, value=None, description="", color="#00f2fe"):
    """
    Renders KPI cards.
    Handles both single KPI values AND full DataFrame input.
    """
    if isinstance(title_or_df, pd.DataFrame):
        df = title_or_df
        total_sales = df['Sales'].sum() if 'Sales' in df.columns else 0
        total_profit = df['Profit'].sum() if 'Profit' in df.columns else 0
        total_orders = df['Order ID'].nunique() if 'Order ID' in df.columns else len(df)
        margin = (total_profit / total_sales * 100) if total_sales > 0 else 0

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
            st.markdown(f"""
            <div class="saas-card">
                <div class="card-label">Total Profit</div>
                <div class="card-value" style="color: #34d399;">{format_currency(total_profit)}</div>
                <p class="card-desc">Net Profit Margin</p>
            </div>
            """, unsafe_allow_html=True)
        with k3:
            st.markdown(f"""
            <div class="saas-card">
                <div class="card-label">Total Orders</div>
                <div class="card-value" style="color: #fbbf24;">{format_number(total_orders)}</div>
                <p class="card-desc">Completed Orders</p>
            </div>
            """, unsafe_allow_html=True)
        with k4:
            st.markdown(f"""
            <div class="saas-card">
                <div class="card-label">Profit Margin</div>
                <div class="card-value" style="color: #a855f7;">{margin:.1f}%</div>
                <p class="card-desc">Overall Conversion Efficiency</p>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="saas-card">
            <div class="card-label">{title_or_df}</div>
            <div class="card-value" style="color: {color};">{value if value is not None else ''}</div>
            <p class="card-desc">{description}</p>
        </div>
        """, unsafe_allow_html=True)

def display_footer():
    """Displays portfolio executive footer across all pages"""
    st.markdown("""
    <hr style="border: 0; height: 1px; background: rgba(255,255,255,0.1); margin-top: 40px; margin-bottom: 20px;">
    <div style="text-align: center; color: #64748b; font-size: 13px; font-weight: 500;">
        Developed by <b style="color: #00f2fe;">Aman Rathod</b> | Built with <b>Python • Pandas • Plotly • Streamlit • SQL • Power BI</b>
    </div>
    """, unsafe_allow_html=True)