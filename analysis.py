import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import os

def main():
    # Load the dataset
    file_path = 'data.csv'
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found.")
        return

    df = pd.read_csv(file_path)

    # Basic Analysis
    print("--- Basic Analysis ---")
    print(df.head())
    print("\n")
    
    # Calculate average Sales
    avg_sales = df['Sales'].mean()
    print(f"Average Sales: ${avg_sales:.2f}")

    # Insights
    total_sales = df['Sales'].sum()
    total_profit = df['Profit'].sum()
    print(f"Total Sales: ${total_sales:.2f}")
    print(f"Total Profit: ${total_profit:.2f}")
    
    best_selling_product = df.loc[df['Sales'].idxmax()]
    print(f"Best Selling Product: {best_selling_product['Product']} with Sales: ${best_selling_product['Sales']}")

    # Visualizations
    # Set style
    sns.set_theme(style="whitegrid")
    
    # 1. Bar Chart: Total Sales by Category
    plt.figure(figsize=(8, 5))
    category_sales = df.groupby('Category')['Sales'].sum().reset_index()
    sns.barplot(x='Category', y='Sales', data=category_sales, palette='viridis')
    plt.title('Total Sales by Category')
    plt.savefig('sales_by_category.png')
    print("Saved bar chart to sales_by_category.png")
    # plt.show() # Uncomment to display window

    # 2. Scatter Plot: Sales vs Profit
    plt.figure(figsize=(8, 5))
    sns.scatterplot(x='Sales', y='Profit', data=df, hue='Category', s=100)
    plt.title('Sales vs Profit')
    plt.savefig('sales_vs_profit.png')
    print("Saved scatter plot to sales_vs_profit.png")
    # plt.show() # Uncomment to display window

    # 3. Heatmap: Correlation Matrix
    plt.figure(figsize=(6, 5))
    # Select only numeric columns for correlation
    numeric_df = df.select_dtypes(include=['float64', 'int64'])
    corr = numeric_df.corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation Matrix')
    plt.savefig('correlation_heatmap.png')
    print("Saved heatmap to correlation_heatmap.png")
    # plt.show() # Uncomment to display window

    print("\nAnalysis Complete.")

if __name__ == "__main__":
    main()
