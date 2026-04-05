# Customer Segmentation Project

This project aims to perform customer segmentation using data from the UCI Online Retail Dataset. The goal is to analyze customer behavior and generate insights that can inform marketing strategies.

## Project Structure

```
customer-segmentation-project
├── data
│   ├── raw
│   │   └── customers.csv          # Raw customer data
│   ├── processed                   # Processed data files after cleaning and feature engineering
│   └── external                    # External datasets if needed
├── notebooks
│   ├── 01-data-exploration.ipynb   # Exploratory Data Analysis (EDA)
│   ├── 02-data-cleaning.ipynb      # Data cleaning steps
│   ├── 03-feature-engineering.ipynb # Feature engineering process
│   ├── 04-modeling.ipynb           # Clustering models
│   └── 05-insights-generation.ipynb # Business insights generation
├── src
│   ├── data_preprocessing.py        # Functions for data loading and cleaning
│   ├── clustering.py                # Functions for clustering algorithms
│   ├── visualization.py              # Functions for creating visualizations
│   └── utils.py                     # Utility functions for reuse
├── reports
│   ├── figures                      # Directory for storing figures generated from analysis
│   └── customer_segmentation_report.md # Summary of findings and insights
├── requirements.txt                 # Necessary Python packages
├── README.md                        # Project overview and setup instructions
└── .gitignore                       # Files and directories to ignore in version control
```

## Installation

To set up the project, clone the repository and install the required packages:

```bash
pip install -r requirements.txt
```

## Data Sources

The raw customer data is sourced from the UCI Online Retail Dataset, which contains transactional data for a UK-based online retailer.

## Usage

1. **Data Exploration**: Start with `notebooks/01-data-exploration.ipynb` to understand the dataset and identify key business questions.
2. **Data Cleaning**: Proceed to `notebooks/02-data-cleaning.ipynb` to clean the data and prepare it for analysis.
3. **Feature Engineering**: Use `notebooks/03-feature-engineering.ipynb` to create relevant features for clustering.
4. **Modeling**: Implement clustering algorithms in `notebooks/04-modeling.ipynb` to segment customers.
5. **Insights Generation**: Finally, analyze the clusters and generate insights in `notebooks/05-insights-generation.ipynb`.

## Reporting

The findings and insights from the analysis will be documented in `reports/customer_segmentation_report.md`. Figures generated during the analysis will be stored in the `reports/figures` directory.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License.