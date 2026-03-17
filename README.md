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

## ⚙️ Workflow

1. Load data from CSV files
2. Clean and preprocess data
3. Join datasets
4. Create derived features
5. Apply business logic validation
6. Generate final report

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
