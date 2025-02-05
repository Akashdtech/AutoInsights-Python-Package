import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class AutoInsights:
    def __init__(self, df):
        """Initialize with a Pandas DataFrame."""
        self.df = df

    def explore_data(self):
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

    def plot_boxplots(self):
        """Plot boxplots for numerical columns."""
        numeric_cols = self.df.select_dtypes(include = ["number"]).columns
        plt.figure(figsize = (12, 6))
        sns.boxplot(data = self.df[numeric_cols])
        plt.xticks(rotation = 45)
        plt.title("Boxplots of Numerical Features")
        plt.show()

    def plot_correlation_heatmap(self):
        """Plot a heatmap of feature correlations."""
        plt.figure(figsize = (10, 6))
        sns.heatmap(self.df.corr(), annot = True, cmap = "coolwarm", linewidths = 0.5)
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
            sns.countplot(y = self.df[col], order = self.df[col].value_counts().index, palette = "viridis")
            plt.title("Count Plots of Categorical Features")
            plt.show()

    def explore_dataset(self):
        self.explore_data()
    
    def generate_plots(self):
        """Perform dataset exploration and generate all visualizations."""
        self.plot_histograms()
        self.plot_boxplots()
        self.plot_correlation_heatmap()
        self.plot_pairplot()
        self.plot_categorical_counts()
