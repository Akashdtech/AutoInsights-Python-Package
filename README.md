# AutoInsights-Python-Package
AutoInsights is a lightweight and powerful Python package designed to automate dataset exploration and visualization. It provides data scientists, analysts, and machine learning practitioners with an intuitive way to quickly analyze datasets, identify key patterns, and uncover insights. By leveraging Pandas, Matplotlib, and Seaborn, AutoInsights simplifies data exploration by offering built-in functions for summarizing dataset characteristics and generating various visualizations. This package eliminates the need for writing repetitive exploratory data analysis (EDA) code, enabling users to focus on deeper analysis and decision-making.

Dataset Exploration:

    AutoInsights helps users quickly assess the structure and quality of their datasets.

    Dataset Information: Provides an overview of column data types and memory usage.
    Summary Statistics: Displays essential descriptive statistics for numerical columns.
    First and Last Records: Quickly checks the first and last 10 rows of the dataset.
    Missing Values Report: Identifies missing data to assist in preprocessing.

Comprehensive Visualizations:

    AutoInsights includes a wide range of visualization functions to help users better understand data distributions and relationships.
    Numerical Data Visualizations.

    Histograms: Displays the distribution of numerical columns.
    Boxplots: Identifies outliers and data spread.
    Line Plots: Tracks numerical feature trends over index values.
    Scatter Plots: Shows relationships between numerical variables.

Categorical Data Visualizations:

    Count Plots: Displays the frequency of different categories.
    Bar Charts: Visualizes categorical distributions.
    Pie Charts: Represents categorical proportions.

Advanced Visualizations:

    Correlation Heatmap: Displays the relationships between numerical features using a heatmap.
    Pairplot: Generates scatter plots between all numerical variables for pairwise comparison.

Installation:

    To install AutoInsights directly from GitHub, run: pip install git+https://github.com/Akashdtech/AutoInsights-Python-Package.git

Usage:

    1. Initial Dataset Exploration:

    from autoinsights import AutoInsights
    import pandas as pd

    # Load dataset
    df = pd.read_csv("your_dataset.csv")

    # Initialize AutoInsights
    insights = AutoInsights(df)

    # Explore dataset (prints summary statistics, missing values, and sample records)
    insights.explore_dataset()

    2. Generate All Visualizations at once:

    insights.generate_all_plots()  # Creates all available visualizations for the entire dataset at once

    3. Generate Visualization for all the respective columns in the entire dataset:

    insights.plot_histograms()
    insights.plot_line_plots()
    insights.plot_scatter_plots()
    insights.plot_boxplots()
    
    insights.plot_correlation_heatmap()
    insights.plot_pairplot()
    
    insights.plot_categorical_counts()
    insights.plot_bar_charts()
    insights.plot_pie_charts()

    4. Generate Visualizations for Specific Columns:
    
    i. <For Numerical Columns>

    insights.plot_histogram("column_name")
    insights.plot_line_plot("column_name")
    insights.plot_scatter_plot("column1", "column2")
    insights.plot_boxplot("column_name")

    ii. <For Categorical Columns>

    insights.plot_categorical_count("column_name")
    insights.plot_bar_chart("column_name")
    insights.plot_pie_chart("column_name")

Why Use AutoInsights?

    Time-Saving: Automates dataset exploration and visualization.
    Easy-to-Use: Simple function calls with minimal configuration.
    Comprehensive: Covers both numerical and categorical data insights.
    Customizable: Allows visualization of specific columns.
