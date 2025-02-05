# AutoInsights-Python-Package
AutoInsights is a lightweight Python package designed for automatic dataset exploration and visualization. It helps data scientists and analysts quickly understand their datasets by providing summary statistics, detecting missing values, and generating insightful visualizations.

Dataset Exploration: 

    Displays dataset info, summary statistics, and missing values.
    
Visualizations: 

    Histograms for numerical distributions. 
    Boxplots to detect outliers. 
    Correlation Heatmap to understand feature relationships. 
    Pairplot for pairwise feature visualization. 
    Categorical Count Plots to analyze category distributions.

Installation:

    !pip install git+https://github.com/Akashdtech/AutoInsights-Python-Package.git

Usage:

    from autoinsights import AutoInsights
    import pandas as pd

    # Load dataset
    df = pd.read_csv("your_dataset.csv")

    # Initialize AutoInsights
    insights = AutoInsights(df)

    # Explore dataset
    insights.explore_dataset()

    # Generate visualizations
    insights.generate_plots()
