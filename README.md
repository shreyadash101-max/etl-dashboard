# ETL Data Pipeline Project

## Description

This project implements an automated ETL (Extract, Transform, Load) pipeline using Python. It reads sales data from a CSV file, cleans and transforms the data, stores the processed data in a SQLite database, generates analytical reports, uploads the reports to Google Drive using the Google Drive API, and sends the reports via email.

The project also includes a Streamlit dashboard for visualizing the processed data.

## Objectives

- Automate the ETL process for sales data
- Clean and transform raw data
- Store processed data in a structured SQLite database
- Generate analytical reports and visualizations
- Store generated reports in cloud storage
- Automate report delivery through email
- Provide a dashboard for data visualization

## Features

- Data extraction from CSV
- Data cleaning and transformation using Pandas
- Sales categorization
- Storage in SQLite database
- Sales trend visualization
- Sales category visualization
- HTML report generation
- Automated Google Drive cloud storage
- OAuth 2.0 authentication for Google Drive
- Automated email report delivery
- Streamlit dashboard
- Logging and error handling

## ETL Workflow

```text
CSV Data
   ↓
Extract
   ↓
Transform
   ↓
Load into SQLite
   ↓
Generate Reports
   ↓
Google Drive Cloud Storage
   ↓
Email Delivery
```

## Cloud Computing Component

Google Drive is integrated into the ETL pipeline using the Google Drive API.

After the reports are generated, the pipeline automatically uploads them to a designated Google Drive folder. OAuth 2.0 is used for secure authorization.

This provides cloud-based storage and remote accessibility for the generated reports.

## Technologies Used

- Python
- Pandas
- SQLite
- Matplotlib
- Streamlit
- Google Drive API
- OAuth 2.0
- Python-dotenv
- Git & GitHub

## Project Structure

```text
etl-dashboard/
│
├── data/
│   ├── dummy_data.csv
│   └── etl.db
│
├── etl/
│   ├── __init__.py
│   ├── extractor.py
│   ├── transformer.py
│   ├── loader.py
│   ├── viz.py
│   ├── emailer.py
│   └── drive_uploader.py
│
├── dashboard.py
├── run_etl.py
├── test_extract.py
├── check_db.py
├── test_drive.py
├── requirements.txt
├── .gitignore
└── README.md
```

## How to Run

1. Clone the repository.

2. Create and activate a Python virtual environment.

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. Configure the required environment variables in `.env`.

5. Configure Google Drive API credentials for cloud report storage.

6. Run the ETL pipeline:

```bash
python run_etl.py
```

## Output

The pipeline generates:

- SQLite database
- Sales trend chart
- Sales category chart
- HTML report
- Cloud-stored reports in Google Drive
- Email-delivered reports

## Future Scope

- Integration with a cloud-hosted database
- Scheduled ETL execution
- Real-time data sources
- Advanced analytics and predictive models
- Deployment on a cloud platform
- Role-based dashboard access
