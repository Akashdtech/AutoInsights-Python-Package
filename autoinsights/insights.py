import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class AutoInsights:
    def __init__(self, df):
        """Initialize with a Pandas DataFrame."""
        self.df = df

    def explore_dataset(self):
        """Perform initial dataset exploration."""
        print("Dataset Info")
        print(self.df.info())
        print("\n First 10 Rows")
        print(self.df.head(10))
        print("\n Last 10 Rows")
        print(self.df.tail(10))
        print("\n Summary Statistics")
        print(self.df.describe())
        print("\n Missing Values")
        print(self.df.isnull().sum())

    def plot_histograms(self):
        """Plot histograms for numerical columns."""
        self.df.hist(figsize = (12, 8), bins = 30, edgecolor = 'black')
        plt.suptitle("Histograms of Numerical Features")
        plt.show()

    def plot_histogram(self, column_name):  
        """Plot a histogram for a specific column."""
        plt.figure(figsize=(8, 6))  
        plt.hist(self.df[column_name], bins=30, edgecolor='black')  
        plt.title(f"Histogram of {column_name}")  
        plt.xlabel(column_name)  
        plt.ylabel("Frequency")  
        plt.show()  

    def plot_line_plots(self):
        """Plot line plots for numerical features against a suitable index."""
        numeric_cols = self.df.select_dtypes(include=["number"]).columns
        for col in numeric_cols:
            plt.figure(figsize=(10, 6))
            sns.lineplot(x=self.df.index, y=col, data=self.df)
            plt.title(f"Line Plot: {col} over Index")
            plt.show()

    def plot_line_plot(self, column_name):
        """Plot a line plot for a specific column against a suitable index."""
        plt.figure(figsize=(10, 6))
        sns.lineplot(x=self.df.index, y=column_name, data=self.df)
        plt.title(f"Line Plot: {column_name} over Index")
        plt.show()

    def plot_scatter_plots(self):
        """Plot scatter plots for all pairs of numerical features."""
        numeric_cols = self.df.select_dtypes(include=["number"]).columns
        for col1 in numeric_cols:
            for col2 in numeric_cols:
                if col1 != col2:
                    plt.figure(figsize=(8, 6))
                    sns.scatterplot(x=col1, y=col2, data=self.df)
                    plt.title(f"Scatter Plot: {col1} vs {col2}")
                    plt.xlabel(col1)
                    plt.ylabel(col2)
                    plt.show()

    def plot_scatter_plot(self, column_name1, column_name2):
        """Plot a scatter plot for two specific numerical columns."""
        plt.figure(figsize=(8, 6))
        sns.scatterplot(x=column_name1, y=column_name2, data=self.df)
        plt.title(f"Scatter Plot: {column_name1} vs {column_name2}")
        plt.xlabel(column_name1)
        plt.ylabel(column_name2)
        plt.show()

    def plot_correlation_heatmap(self):
        """Plot a heatmap of feature correlations."""
        numeric_cols = self.df.select_dtypes(include = ["number"]).columns
        plt.figure(figsize = (10, 6))
        sns.heatmap(self.df[numeric_cols].corr(), annot = True, cmap = "coolwarm", linewidths = 0.5)
        plt.title("Feature Correlation Heatmap")
        plt.show()

    def plot_pairplot(self):
        """Plot pairwise relationships for numerical columns."""
        sns.pairplot(self.df.select_dtypes(include = ["number"]))
        plt.suptitle("Pairwise Relationships", y=1.02)
        plt.show()

    def plot_categorical_counts(self):
        """Plot bar charts for categorical variables."""
        categorical_cols = self.df.select_dtypes(include = ["object", "category"]).columns
        for col in categorical_cols:
            plt.figure(figsize = (8, 4))
            sns.countplot(y = self.df[col], order = self.df[col].value_counts().index, hue = self.df[col], palette = "viridis", legend = False)
            plt.title("Count Plots of Categorical Features")
            plt.show()

    def plot_categorical_count(self, column_name):
        """Plot a bar chart for a specific categorical variable."""
        plt.figure(figsize=(8, 4))
        sns.countplot(y=self.df[column_name], order=self.df[column_name].value_counts().index, hue=self.df[column_name], palette="viridis", legend=False)
        plt.title(f"Count Plot of {column_name}")
        plt.show()

    def plot_bar_charts(self):
        """Plot bar charts for all categorical variables."""
        categorical_cols = self.df.select_dtypes(include=["object", "category"]).columns
        for col in categorical_cols:
            plt.figure(figsize=(10, 6))
            sns.countplot(x=col, data=self.df)
            plt.title(f"Bar Chart of {col}")
            plt.xlabel(col)
            plt.ylabel("Count")
            plt.xticks(rotation=45, ha='right')
            plt.show()

    def plot_bar_chart(self, column_name):
        """Plot a bar chart for a specific categorical variable."""
        plt.figure(figsize=(10, 6))
        sns.countplot(x=column_name, data=self.df)
        plt.title(f"Bar Chart of {column_name}")
        plt.xlabel(column_name)
        plt.ylabel("Count")
        plt.xticks(rotation=45, ha='right')
        plt.show()

    def plot_pie_charts(self):
        """Plot pie charts for all categorical variables."""
        categorical_cols = self.df.select_dtypes(include=["object", "category"]).columns
        for col in categorical_cols:
            plt.figure(figsize=(8, 6))
            self.df[col].value_counts().plot.pie(autopct='%1.1f%%', startangle=90)
            plt.title(f"Pie Chart of {col}")
            plt.ylabel('')
            plt.show()

    def plot_pie_chart(self, column_name):
        """Plot a pie chart for a specific categorical variable."""
        plt.figure(figsize=(8, 6))
        self.df[column_name].value_counts().plot.pie(autopct='%1.1f%%', startangle=90)
        plt.title(f"Pie Chart of {column_name}")
        plt.ylabel('')
        plt.show()

    def plot_boxplots(self):
        """Plot boxplots for numerical columns."""
        numeric_cols = self.df.select_dtypes(include = ["number"]).columns
        plt.figure(figsize = (12, 6))
        sns.boxplot(data = self.df[numeric_cols])
        plt.xticks(rotation = 45)
        plt.title("Boxplots of Numerical Features")
        plt.show()

    def plot_boxplot(self, column_name):
        """Plot a boxplot for a specific numerical column."""
        plt.figure(figsize=(8, 6))
        sns.boxplot(y=self.df[column_name])
        plt.title(f"Boxplot of {column_name}")
        plt.show() 

    def generate_all_plots(self):
        """Perform dataset exploration and generate all visualizations."""
        self.plot_histograms()
        self.plot_line_plots()
        self.plot_scatter_plots()
        self.plot_boxplots()
        self.plot_correlation_heatmap()
        self.plot_pairplot()
        self.plot_categorical_counts()
        self.plot_bar_charts()
        self.plot_pie_charts()
