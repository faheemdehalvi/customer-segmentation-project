# Customer Segmentation Project

A comprehensive data science project that segments customers using the Kaggle Online Retail Dataset. This project analyzes 541,909 transactions from 3,949 unique customers and identifies 4 distinct customer segments using RFM (Recency, Frequency, Monetary) analysis and K-means clustering.

## Project Overview

This project leverages advanced data analytics and machine learning to understand customer purchasing behavior and identify actionable segments for targeted marketing strategies.

**Key Metrics:**
- Total Transactions: 541,909
- Unique Customers: 3,949 (after removing incomplete records)
- Customer Segments: 4 clusters identified
- Time Period: December 2010 - December 2011
- Geographic Coverage: 37 countries (UK-based retailer)
- Variance Explained: 88% (in 2D PCA space)

## Dataset Overview

The dataset contains transactional data from an online UK-based retailer, including:
- 8 features: InvoiceNo, StockCode, Description, Quantity, InvoiceDate, UnitPrice, CustomerID, Country
- Key observations:
  - Total Spent ranges from -£4,287.63 to +£279,489.02 (negative values represent net returns after refunds)
  - Average transaction value: £1,898.46
  - Customers span 37 countries globally

## Project Structure

```
customer-segmentation-project
├── data
│   ├── raw                         # Raw data (download from Kaggle)
│   ├── processed                   # Processed data files after feature engineering
│   └── external                    # External datasets if needed
├── notebooks
│   ├── 01-data-exploration.ipynb   # Exploratory Data Analysis (EDA)
│   ├── 02-data-cleaning.ipynb      # Data cleaning steps
│   ├── 03-feature-engineering.ipynb # Feature engineering and RFM creation
│   ├── 04-modeling.ipynb           # K-means and DBSCAN clustering
│   └── 05-insights-generation.ipynb # Customer segment analysis and recommendations
├── src
│   ├── data_preprocessing.py        # Data loading and cleaning functions
│   ├── clustering.py                # Clustering algorithm implementations
│   ├── visualization.py             # Visualization utilities
│   └── utils.py                     # Utility functions
├── reports
│   ├── figures                      # Generated analysis visualizations
│   └── customer_segmentation_report.md # Summary of findings
├── requirements.txt                 # Python dependencies
├── README.md                        # This file
└── .gitignore                       # Git ignore rules
```

## Installation

To set up the project, clone the repository and install the required packages:

```bash
# Clone repository
git clone https://github.com/faheemdehalvi/customer-segmentation-project.git
cd customer-segmentation-project

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Download dataset
# 1. Go to https://www.kaggle.com/datasets/vijayuv/onlineretail
# 2. Download OnlineRetail.csv to data/raw/

# Start Jupyter
jupyter notebook
```

## Analysis Workflow

### 1. Data Exploration (01-data-exploration.ipynb)

Understand the structure, quality, and characteristics of the dataset.

Key Findings:
- 541,909 transactions with 8 columns
- 135,080 missing CustomerIDs (24.9% of data)
- 1,454 missing product descriptions
- Right-skewed distribution in transaction values

### 2. Feature Engineering (03-feature-engineering.ipynb)

Create RFM (Recency, Frequency, Monetary) metrics for customer segmentation:
- **Recency**: Days since last purchase (snapshot: Dec 2, 2011)
- **Frequency**: Number of transactions per customer
- **Monetary**: Total spending per customer

Results:
- 3,949 unique customers after cleaning
- Recency: mean=92 days, range=1-374 days
- Frequency: mean=93 transactions, range=1-7,983
- Monetary: mean=£1,898.46, range=-£4,287.63 to +£279,489.02
- Features scaled using StandardScaler for clustering

### 3. Clustering & Modeling (04-modeling.ipynb)

Identify optimal number of clusters and segment customers.

Methods Applied:
- Elbow Method: Shows optimal k=4
- K-means Clustering: Primary algorithm
- DBSCAN: Alternative approach (78 outliers)
- PCA: 2D visualization (88% variance explained)

Cluster Distribution:
```
Cluster 0 (At-Risk):     1,002 customers (25.4%)
Cluster 1 (Valuable):      778 customers (19.7%)
Cluster 2 (Loyal):       2,046 customers (51.8%)
Cluster 3 (VIP):           123 customers (3.1%)
```

### 4. Insights & Recommendations (05-insights-generation.ipynb)

Profile each segment and develop actionable marketing strategies.

#### Cluster 0: At-Risk Customers (25.4%)

Characteristics:
- High Recency: Haven't purchased in 100+ days
- Low Frequency: 1-2 transactions average
- Low Monetary Value: £100-200 average

Recommendations:
- Launch re-engagement campaigns with win-back discounts
- Send personalized outreach emails
- Conduct surveys to understand churn reasons
- Offer incentives to encourage return purchases

#### Cluster 1: Valuable Customers (19.7%)

Characteristics:
- Low Recency: Regular recent purchasers (30-60 days)
- Moderate-High Frequency: Consistent repeat buying
- High Monetary Value: £2,000-4,000+ average

Recommendations:
- Premium loyalty programs and VIP treatment
- Exclusive early access to new products
- VIP events and special invitations
- Dedicated customer support

#### Cluster 2: Loyal Customers (51.8% - LARGEST)

Characteristics:
- Moderate Recency: Regular purchasers (30-90 days)
- Moderate Frequency: Consistent purchase history (20-80 transactions)
- Moderate Monetary Value: £400-800 average

Recommendations:
- Mid-tier rewards program
- Cross-sell and upsell opportunities
- Seasonal promotions and recommendations
- Regular engagement through email and social media
- Tier-based discounts

#### Cluster 3: VIP Customers (3.1% - HIGHEST VALUE)

Characteristics:
- Very Recent Activity: Most frequent purchasers
- Extremely High Frequency: 100-800+ transactions
- Highest Monetary Value: £2,000-10,000+ lifetime value

Recommendations:
- Dedicated account managers
- Exclusive VIP tier with premium benefits
- Involve in product development
- Premium customer support
- Partnership and co-creation opportunities

## Business Impact

Revenue Potential by Segment:
- At-Risk: £500K+ (with 20% win-back rate)
- Valuable: £1.5M+ (maintain and grow)
- Loyal: £2M+ (upsell opportunities)
- VIP: £500K+ (retention critical)

Expected Outcomes:
- Improved customer retention through targeted re-engagement
- Personalized marketing leading to higher conversion rates
- Optimized marketing spend by segment
- Increased customer lifetime value through strategic nurturing
- Better resource allocation based on segment profitability

## Key Visualizations

### Elbow Method for Optimal Clustering
![Elbow Curve](reports/figures/elbow_curve.png)

Shows optimal k=4 with significant inertia reduction from k=1 to k=4, then diminishing returns.

### PCA of Customer Segments
![PCA Clusters](reports/figures/pca_clusters.png)

2D visualization showing clear separation of 4 customer clusters with 88% variance explained:
- Cluster 0 (Purple): Old, infrequent customers
- Cluster 1 (Blue): Valuable, recent customers
- Cluster 2 (Green): Loyal moderate customers
- Cluster 3 (Yellow): VIP ultra-active customers

### Cluster Profiles Heatmap
![Cluster Heatmap](reports/figures/cluster_heatmap.png)

Scaled feature values showing RFM characteristics by segment:
- Red zones: High frequency and monetary (Clusters 1 & 3)
- Blue zones: Low frequency and monetary (Clusters 0 & 2)

### Customer Distribution
![Customer Distribution](reports/figures/cluster_distribution.png)

Segment composition showing Loyal as majority (51.8%) and VIP as critical segment (3.1%).

### Total Spent Distribution
![Total Spent Distribution](reports/figures/total_spent_distribution.png)

Transaction value distribution showing right-skewed pattern with peak in £1,500-2,500 range.

## Technical Stack

- Data Processing: Pandas, NumPy
- Visualization: Matplotlib, Seaborn
- Machine Learning: Scikit-learn (KMeans, DBSCAN, PCA, StandardScaler)
- Analysis: RFM segmentation, K-means clustering, Dimensionality reduction
- Tools: Jupyter Notebooks, Git, GitHub

## Usage

1. Data Exploration: `notebooks/01-data-exploration.ipynb`
2. Data Cleaning: `notebooks/02-data-cleaning.ipynb`
3. Feature Engineering: `notebooks/03-feature-engineering.ipynb`
4. Modeling: `notebooks/04-modeling.ipynb`
5. Insights: `notebooks/05-insights-generation.ipynb`

Execute all cells in each notebook to see analysis and visualizations.

## Key Findings

- 4 distinct customer segments with clear behavioral patterns
- 88% variance captured in 2D PCA space
- 51.8% of customers in Loyal segment (growth potential)
- 3.1% VIP customers drive disproportionate revenue (retention critical)
- 25.4% At-Risk customers need proactive re-engagement
- Actionable insights enabling targeted marketing strategies

## Reporting

Findings and insights documented in the notebooks. Figures saved to `reports/figures/` for presentations and reports.

## Contributing

Contributions welcome! Please:
1. Submit a pull request for improvements
2. Open an issue for bug reports or feature requests
3. Update notebooks with new analyses

## Next Steps

- Implement automated re-engagement campaigns for At-Risk segment
- A/B test marketing strategies by segment
- Monitor segment migration over time
- Build predictive churn models
- Develop customer lifetime value (CLV) models

## Author

Faheem Dehalvi - Master of Data Science, RMIT Melbourne

[LinkedIn](https://linkedin.com/in/faheem-dehalvi) | [GitHub](https://github.com/faheemdehalvi)

## License

This project is licensed under the MIT License.

---

Last Updated: April 6, 2026  
Status: Complete with full analysis and actionable insights
