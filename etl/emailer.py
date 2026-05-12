import smtplib
from email.message import EmailMessage
import os

def send_email():
    smtp_user = os.getenv("SMTP_USER")
    smtp_pass = os.getenv("SMTP_PASS")
    to_address = os.getenv("TO_ADDRESS")

    msg = EmailMessage()
    msg['From'] = smtp_user
    msg['To'] = to_address

    # CREATE SUMMARY CONTENT
    summary = "ETL Report Summary:\n\n"

    try:
        import sqlite3
        import pandas as pd

        conn = sqlite3.connect('data/etl.db')
        df = pd.read_sql('SELECT * FROM data', conn)
        conn.close()

        summary += f"Total Rows: {len(df)}\n"
        summary += f"Columns: {list(df.columns)}\n"

        if 'sales' in df.columns:
            summary += f"Total Sales: {df['sales'].sum()}\n"

        # Dynamic subject
        msg['Subject'] = f"ETL Report - {len(df)} records"

    except Exception as e:
        summary += f"Could not load summary: {e}\n"
        msg['Subject'] = "ETL Report"

    msg.set_content(summary)

    # ATTACH HTML REPORT
    try:
        with open('reports/report.html', 'rb') as f:
            msg.add_attachment(
                f.read(),
                maintype='text',
                subtype='html',
                filename='report.html'
            )
    except Exception as e:
        print(f"Could not attach HTML report: {e}")


    # ATTACH CHART
    try:
        with open('reports/sales_trend.png', 'rb') as f:
            msg.add_attachment(
                f.read(),
                maintype='image',
                subtype='png',
                filename='sales_trend.png'
            )
    except Exception as e:
        print(f"Could not attach chart: {e}")

    
    # SEND EMAIL
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(smtp_user, smtp_pass)
            smtp.send_message(msg)

        print("Email sent successfully!")

    except Exception as e:
        print(f"Failed to send email: {e}")