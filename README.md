
# Healthcare Data Pipeline Project

## Overview
This project processes messy healthcare data, cleans it, transforms it into normalized tables, and saves it into a MySQL database.

## Deliverables
- Python Scripts: 
  - `bronze_layer.py`: Handles raw data ingestion into the Bronze layer.
  - `silver_layer.py`: Cleans and validates data in the Silver layer.
  - `gold_layer.py`: Transforms data into normalized tables for the Gold layer.
  - `load_to_mysql.py`: Loads Gold layer data into a MySQL database.
- SQL Schema: `schema.sql` defines tables for Patients, Doctors, and Appointments.

## Instructions
1. **Setup MySQL**:
   - Create a database named `healthcare`.
   - Execute `schema.sql` to create the required tables.

2. **Run the Pipeline**:
   - Ensure Python is installed with `pandas` and `mysql-connector-python` libraries.
   - Update MySQL credentials in `load_to_mysql.py`.
   - Run scripts in order:
     - `bronze_layer.py`
     - `silver_layer.py`
     - `gold_layer.py`
     - `load_to_mysql.py`

3. **Dependencies**:
   ```bash
   pip install pandas mysql-connector-python
   ```

## Outputs
- Bronze Layer: `bronze_raw_data.csv`
- Silver Layer: `silver_cleaned_data.csv`
- Gold Layer: 
  - `gold_patients.csv`
  - `gold_doctors.csv`
  - `gold_appointments.csv`
