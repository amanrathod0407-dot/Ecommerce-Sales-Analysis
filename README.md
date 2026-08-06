# 📊 E-Commerce Sales & Diagnostic Insights Engine

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Streamlit-1.30%2B-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
  <img src="https://img.shields.io/badge/Power_BI-Desktop-F2C811?style=for-the-badge&logo=powerbi&logoColor=black" />
  <img src="https://img.shields.io/badge/SQL-PostgreSQL%2FSQLite-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" />
</p>

An end-to-end Business Intelligence, Data Analytics, and Automated Executive Reporting System designed to analyze multi-territory e-commerce performance, pinpoint profit margin erosion drivers, and deliver real-time strategic recommendations.

---

## 🎯 Business Problem & Key Outcomes

Traditional dashboards only display raw static metrics without diagnostic context. This project solves that by combining **interactive visualization** with an **Automated Executive Insights Engine**:

- 📉 **Margin Loss Identification:** Pinpoints exact product sub-categories bleeding margins due to steep discounts (>20%).
- 🚀 **Territory Growth Acceleration:** Identifies top-revenue hubs and optimizes inventory allocation.
- 🤖 **Dynamic C-Suite Briefings:** Automatically updates real-time diagnostic bullet summaries on dataset reload.

---

## 🚀 Key Features & Functional Modules

### 1. 🏠 Executive Overview & KPI Scorecards
- Live metric cards tracking **Gross Revenue**, **Net Profit**, **Completed Orders**, and **Store Profit Margin Efficiency %**.
- Dynamic trend charts powered by Plotly with a custom Dark SaaS theme UI.

### 2. 🤖 Automated Executive Insights Engine
- Real-time diagnostic summary block summarizing business performance dynamically.
- Strategic **Margin Recovery Plan** and **Supply Chain Allocation** action items.

### 3. 👥 Customer & Product Deep-Dive
- Customer segmentation based on purchase history and average order value (AOV).
- Sub-category Profit & Loss spectrum visualization.

### 📊 Multi-Page SaaS Architecture
- Multi-page navigation (`Home`, `Sales`, `Customers`, `Products`, `AI Insights`, `PowerBI Dashboard`, `About`).

---

## 🛠️ Tech Stack & Architecture

| Layer | Tools & Technologies |
| :--- | :--- |
| **Primary Language** | Python 3.10+ |
| **Data Processing & Analytics** | Pandas, NumPy, SQL |
| **Visualization & UI** | Plotly Express, Streamlit, HTML5/CSS3 (Dark Mesh Theme) |
| **Business Intelligence** | Power BI Desktop, DAX |
| **Tools & Version Control** | VS Code, Git, GitHub |

---

## 📂 Repository Structure

```text
Ecommerce-Sales-Analysis/
│
├── dashboard/
│   ├── app.py                      # Multi-Page Navigation Entry Point
│   ├── pages/                      # Individual Application Views
│   │   ├── 1_Home.py               # Executive Scorecards & Trend Overview
│   │   ├── 2_Sales.py              # Revenue & Regional Breakdown
│   │   ├── 3_Customers.py          # Customer Purchasing Behavior
│   │   ├── 4_Products.py           # Inventory & Profit Spectrum
│   │   ├── 5_AI_Insights.py        # Dynamic Executive Summary Engine
│   │   ├── 6_PowerBI_Dashboard.py  # Embedded BI Reporting
│   │   └── 7_About.py              # Documentation & Architecture Info
│   ├── assets/                     # Custom CSS, Glassmorphism Styling & Logos
│   └── utils/                      # Loader Utility & Dynamic KPI Helpers
│
├── data/
│   ├── raw/                        # Original Dataset
│   └── cleaned/                    # Processed CSV Data Schema
│
├── images/                         # Project Preview Screenshots
├── powerbi/                        # Power BI (.pbix) File
├── python/                         # EDA & Cleaning Jupyter Notebooks
├── sql/                            # Business Aggregation Scripts
│
├── requirements.txt                # Python Dependencies
└── README.md                       # Master Documentation
```

---

## 📊 Analytics Workflow

1. **Data Ingestion & Cleaning:** Handled nulls, normalized schema, and parsed date features in Python/Jupyter Notebooks.
2. **Exploratory Analytics & SQL:** Wrote analytical queries to calculate customer LTV, RFM matrices, and discount impact.
3. **Interactive Frontend:** Built responsive Streamlit multi-page layout with custom UI modules.
4. **Automated Insights Logic:** Applied dynamic aggregation logic to generate bulleted C-suite business reports automatically.

---

## ⚙️ Local Installation & Execution

### 1. Clone the Repository
```bash
git clone [https://github.com/amanrathod0407-dot/Ecommerce-Sales-Analysis.git](https://github.com/amanrathod0407-dot/Ecommerce-Sales-Analysis.git)
cd Ecommerce-Sales-Analysis
```

### 2. Create & Activate Virtual Environment (Optional)
```bash
python -m venv venv

# On Windows:
venv\Scripts\activate

# On Mac/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Launch Streamlit Dashboard
```bash
streamlit run dashboard/app.py
```

---

## 👨‍💻 Author

**Aman Sanjay Rathod**  
*MCA Student | Data Analytics & BI Developer | Full Stack Developer*

- **GitHub:** [amanrathod0407-dot](https://github.com/amanrathod0407-dot)
- **Repository:** [Ecommerce-Sales-Analysis](https://github.com/amanrathod0407-dot/Ecommerce-Sales-Analysis)