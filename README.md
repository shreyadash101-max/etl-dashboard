# ETL Data Pipeline Project

## Description
This project implements an ETL (Extract, Transform, Load) pipeline using Python. 
It reads data from a CSV file, cleans and processes it, stores it in a SQLite database, 
generates reports, and sends them via email.

## Features
- Data extraction from CSV
- Data cleaning and transformation
- Storage in SQLite database
- HTML and PNG report generation
- Automated email sending

## Technologies Used
- Python
- pandas
- SQLite
- matplotlib
- smtplib
- python-dotenv

## How to Run
1. Install dependencies:
   pip install -r requirements.txt

2. Configure `.env` file

3. Run:
   python run_etl.py

## Output
- Database: `data/etl.db`
- Reports: `reports/report.html`, `reports/sales_trend.png`