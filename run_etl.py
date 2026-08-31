import os
import logging
from dotenv import load_dotenv

from etl.extractor import extract
from etl.transformer import transform
from etl.loader import load
from etl.viz import create_report
from etl.emailer import send_email
from etl.drive_uploader import upload_reports

print("DEBUG: extract function from ->", extract.__module__)

# Load environment variables
load_dotenv()

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    try:
        logger.info("Starting ETL pipeline")

        # Get CSV path from .env
        csv_path = os.getenv("CSV_PATH")

        logger.info("Extracting data")
        df = extract(csv_path)

        print(type(df))

        logger.info("Transforming data")
        df_clean = transform(df)

        print(df_clean.columns)

        print("DEBUG: columns =", df_clean.columns)

        logger.info("Loading data")
        load(df_clean)

        logger.info("Generating reports")
        create_report(df_clean)

        logger.info("Uploading reports to Google Drive")
        upload_reports()

        # Email step
        if os.getenv("SEND_EMAIL") == "true":
            logger.info("Sending email...")
            send_email()

        logger.info("ETL pipeline completed successfully")

    except Exception as e:
        logger.error(f"Pipeline failed: {e}")


# CRITICAL
if __name__ == "__main__":
    main()