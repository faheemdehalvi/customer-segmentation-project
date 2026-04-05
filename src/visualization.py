import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_histogram(data, column, bins=30, title=None, xlabel=None, ylabel='Frequency'):
    plt.figure(figsize=(10, 6))
    sns.histplot(data[column], bins=bins, kde=True)
    plt.title(title if title else f'Histogram of {column}')
    plt.xlabel(xlabel if xlabel else column)
    plt.ylabel(ylabel)
    plt.grid()
    plt.show()

def plot_boxplot(data, column, title=None, xlabel=None, ylabel='Value'):
    plt.figure(figsize=(10, 6))
    sns.boxplot(x=data[column])
    plt.title(title if title else f'Boxplot of {column}')
    plt.xlabel(xlabel if xlabel else column)
    plt.ylabel(ylabel)
    plt.grid()
    plt.show()

def plot_scatter(data, x_column, y_column, title=None, xlabel=None, ylabel=None):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=data, x=x_column, y=y_column)
    plt.title(title if title else f'Scatter plot of {y_column} vs {x_column}')
    plt.xlabel(xlabel if xlabel else x_column)
    plt.ylabel(ylabel if ylabel else y_column)
    plt.grid()
    plt.show()

def save_figure(fig, filename, dpi=300):
    fig.savefig(filename, dpi=dpi, bbox_inches='tight')