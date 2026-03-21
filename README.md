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

## 📊 Datasets Description

The pipeline processes the following datasets:

| Dataset                | Description                                             |
| ---------------------- | ------------------------------------------------------- |
| user_referrals         | Contains referral information between users             |
| user_referral_logs     | Logs related to referral reward events                  |
| user_logs              | Stores user information such as name and phone          |
| referral_rewards       | Contains reward values for referrals                    |
| user_referral_statuses | Status of referral (Berhasil, Menunggu, Tidak Berhasil) |
| paid_transactions      | Contains transaction details                            |
| lead_log               | Stores lead source information                          |

All datasets are stored in the `data/` folder and loaded using Pandas.

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

## 🔄 Data Transformation Logic

The pipeline performs the following transformations:

* Convert timestamp columns to datetime format
* Remove duplicate records
* Join multiple datasets to create a unified referral dataset
* Handle missing values appropriately
* Create derived column:

  * `referral_source_category`
* Apply business validation rules to detect valid and invalid referrals

---

## ▶️ How to Run

### Install dependencies

pip install -r requirements.txt

### Run pipeline

python src/main.py

### Run profiling

python profiling/profiling.py

---

## ✅ Execution Proof

### Running the pipeline locally

```bash
python src/main.py
```

### Output:

```
🚀 Starting Referral Data Pipeline...
✅ Report generated successfully!
📊 Total rows: 46
🎉 Pipeline completed successfully!
```

### Generated Output File:

```
output/referral_report.csv
```

This confirms that the pipeline runs successfully and processes all referral records.

---

### Running Data Profiling

```bash
python profiling/profiling.py
```

### Output:

* Profiling results are generated for each dataset
* Files saved in:

```
output/profile_*.csv
```

---

## 🐳 Docker Execution Proof

### Build Docker Image

```bash
docker build -t referral_pipeline .
```

### Run Docker Container

```bash
docker run referral_pipeline
```

### Output:

```
🚀 Starting Referral Data Pipeline...
✅ Report generated successfully!
📊 Total rows: 46
🎉 Pipeline completed successfully!
```

This confirms that the pipeline runs successfully inside a Docker container.

---

## 📊 Output Validation

The final report contains:

* 46 rows (as expected)
* Cleaned and transformed data
* Business logic validation column:

  * `is_business_logic_valid`

Example:

| referral_id | transaction_status | is_business_logic_valid |
| ----------- | ------------------ | ----------------------- |
| 12345       | PAID               | TRUE                    |
| 67890       | FAILED             | FALSE                   |

---

## 📌 Author

Moumita Das
Data Engineer Intern Candidate
