# Referral Data Pipeline – Data Engineer Take-Home Test

## 📌 Overview

This project implements a data pipeline to process referral program data and detect invalid or fraudulent referral rewards.

The pipeline is built using Python (Pandas) and follows a modular data engineering workflow.

---

## 📁 Project Structure

referral-data-pipeline
│
├ data/                        # input CSV files
├ output/                      # generated reports
├ src/                         # pipeline code
│   └ main.py
├ profiling/                   # data profiling
│   └ profiling.py
│
├ Dockerfile
├ requirements.txt
├ README.md
├ data_dictionary.xlsx
└ referral_data_pipeline_documentation.pdf

---

## ⚙️ Pipeline Workflow

The data pipeline follows a structured workflow:

### 1. Data Loading

* Load all CSV files from the `data/` folder using Pandas.

### 2. Data Cleaning

* Remove duplicate records
* Convert timestamp columns to datetime
* Handle missing values

### 3. Data Processing

* Join multiple tables:

  * user_referrals
  * user_logs
  * referral_rewards
  * user_referral_statuses
  * paid_transactions

### 4. Feature Engineering

* Create new column:

  * `referral_source_category`

Logic:

* User Sign Up → Online
* Draft Transaction → Offline
* Lead → From lead_logs

### 5. Business Logic Validation

* Create:

  * `is_business_logic_valid`

Rules:

* Valid if reward + successful + valid transaction
* Invalid if mismatch in reward, status, or transaction

### 6. Output Generation

* Generate final report:

  * `output/referral_report.csv`
* Contains 46 rows with validation results

---

## ▶️ How to Run

Install dependencies:

pip install -r requirements.txt

Run pipeline:

python src/main.py

Run profiling:

python profiling/profiling.py

---

## 🐳 Docker

Build image:

docker build -t referral_pipeline .

Run container:

docker run referral_pipeline

---

## 📊 Output

Generated files:

output/referral_report.csv
output/profile_*.csv

---

## 📌 Author

Moumita Das
Data Engineer Intern Candidate
