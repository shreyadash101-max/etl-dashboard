import matplotlib.pyplot as plt

def create_report(df):
    # Chart 1: Sales Trend
    df.plot(x='date', y='sales', kind='line', marker='o', title='Sales Trend')
    plt.tight_layout()
    plt.savefig('reports/sales_trend.png')
    plt.close()

    # Chart 2: Sales Category Distribution
    df['sales_category'].value_counts().plot(kind='bar', title='Sales Category')
    plt.tight_layout()
    plt.savefig('reports/category.png')
    plt.close()

    # Create HTML report
    with open('reports/report.html', 'w') as f:
        f.write("<h1>ETL Report</h1>")

        f.write("<h2>Summary Statistics</h2>")
        f.write(df.describe().to_html())

        f.write("<h2>Data Preview</h2>")
        f.write(df.head().to_html())

        f.write("<h2>Sales Trend</h2>")
        f.write("<img src='sales_trend.png' width='600'>")

        f.write("<h2>Sales Category</h2>")
        f.write("<img src='category.png' width='600'>")