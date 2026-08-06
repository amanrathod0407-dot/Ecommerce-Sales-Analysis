import plotly.express as px

def apply_chart_theme(fig, title=""):
    fig.update_layout(
        title=dict(text=title, font=dict(size=16, color='#1f2937', family='Inter')),
        template='plotly_white',
        paper_bgcolor='rgba(0, 0, 0, 0)',
        plot_bgcolor='rgba(0, 0, 0, 0)',
        font=dict(color='#4b5563'),
        margin=dict(l=20, r=20, t=40, b=20),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    return fig

def plot_sales_trend(df):
    trend_df = df.groupby('Month_Year')['Sales'].sum().reset_index()
    fig = px.line(trend_df, x='Month_Year', y='Sales', markers=True)
    fig.update_traces(line_color='#2563eb', line_width=3)
    return apply_chart_theme(fig, '📈 Monthly Sales Trend')

def plot_category_sales(df):
    cat_df = df.groupby('Category')['Sales'].sum().reset_index()
    fig = px.bar(cat_df, x='Category', y='Sales', color='Category', text_auto='.2s', color_discrete_sequence=['#2563eb', '#3b82f6', '#60a5fa'])
    fig.update_layout(showlegend=False)
    return apply_chart_theme(fig, '📦 Sales by Category')

def plot_region_performance(df):
    reg_df = df.groupby('Region')[['Sales', 'Profit']].sum().reset_index()
    fig = px.bar(reg_df, x='Region', y=['Sales', 'Profit'], barmode='group', color_discrete_sequence=['#2563eb', '#10b981'])
    return apply_chart_theme(fig, '🗺️ Regional Sales vs Profit')

def plot_top_customers(df, top_n=10):
    cust_df = df.groupby('Customer Name')['Sales'].sum().nlargest(top_n).reset_index()
    fig = px.bar(cust_df, x='Sales', y='Customer Name', orientation='h', color='Sales', color_continuous_scale='Blues')
    fig.update_layout(yaxis={'categoryorder':'total ascending'}, coloraxis_showscale=False)
    return apply_chart_theme(fig, f'👑 Top {top_n} Customers')

def plot_top_products(df, top_n=10):
    prod_df = df.groupby('Product Name')['Sales'].sum().nlargest(top_n).reset_index()
    fig = px.bar(prod_df, x='Sales', y='Product Name', orientation='h', color='Sales', color_continuous_scale='Teal')
    fig.update_layout(yaxis={'categoryorder':'total ascending'}, coloraxis_showscale=False)
    return apply_chart_theme(fig, f'🏷️ Top {top_n} Products')

def plot_discount_vs_profit(df):
    fig = px.scatter(df, x='Discount', y='Profit', color='Category', size='Sales', hover_data=['Sub-Category'])
    return apply_chart_theme(fig, '📉 Discount vs Profit Impact')