import pandas as pd
import numpy as np

# -----------------------------
# 1. LOAD DATA
# -----------------------------

def load_data():
    user_referrals = pd.read_csv("data/user_referrals.csv")
    user_logs = pd.read_csv("data/user_logs.csv")
    referral_logs = pd.read_csv("data/user_referral_logs.csv")
    referral_status = pd.read_csv("data/user_referral_statuses.csv")
    rewards = pd.read_csv("data/referral_rewards.csv")
    transactions = pd.read_csv("data/paid_transactions.csv")
    leads = pd.read_csv("data/lead_log.csv")

    return user_referrals, user_logs, referral_logs, referral_status, rewards, transactions, leads


# -----------------------------
# 2. DATA CLEANING
# -----------------------------

def clean_data(user_referrals, transactions):

    user_referrals = user_referrals.drop_duplicates()

    user_referrals["referral_at"] = pd.to_datetime(user_referrals["referral_at"], errors='coerce')
    user_referrals["updated_at"] = pd.to_datetime(user_referrals["updated_at"], errors='coerce')

    transactions["transaction_at"] = pd.to_datetime(transactions["transaction_at"], errors='coerce')

    return user_referrals, transactions


# -----------------------------
# 3. DATA PROCESSING (JOINS)
# -----------------------------

def process_data(user_referrals, user_logs, referral_logs, referral_status, rewards, transactions):

    df = user_referrals.merge(
        referral_status,
        left_on="user_referral_status_id",
        right_on="id",
        how="left"
    )

    df = df.merge(
        rewards,
        left_on="referral_reward_id",
        right_on="id",
        how="left",
        suffixes=("","_reward")
    )

    df = df.merge(
        transactions,
        on="transaction_id",
        how="left"
    )

    df = df.merge(
        user_logs,
        left_on="referrer_id",
        right_on="user_id",
        how="left",
        suffixes=("","_referrer")
    )

    return df


# -----------------------------
# 4. FEATURE ENGINEERING
# -----------------------------

def add_source_category(df, leads):

    def get_category(row):

        if row["referral_source"] == "User Sign Up":
            return "Online"

        elif row["referral_source"] == "Draft Transaction":
            return "Offline"

        elif row["referral_source"] == "Lead":
            lead = leads[leads["lead_id"] == row["referee_id"]]
            if len(lead) > 0:
                return lead.iloc[0]["source_category"]

        return None

    df["referral_source_category"] = df.apply(get_category, axis=1)

    return df


# -----------------------------
# 5. BUSINESS LOGIC VALIDATION
# -----------------------------

def validate_business_logic(df):

    def check_logic(row):

        # VALID CASE (Successful referral)
        if (
            pd.notnull(row["reward_value"]) and row["reward_value"] > 0
            and row["description"] == "Berhasil"
            and pd.notnull(row["transaction_id"])
            and row["transaction_status"] == "PAID"
            and row["transaction_type"] == "NEW"
        ):
            if pd.notnull(row["transaction_at"]) and pd.notnull(row["referral_at"]):
                if row["transaction_at"] >= row["referral_at"]:
                    return True

        # VALID CASE (Pending / Failed without reward)
        if row["description"] in ["Menunggu", "Tidak Berhasil"]:
            if pd.isnull(row["reward_value"]) or row["reward_value"] == 0:
                return True

        return False

    df["is_business_logic_valid"] = df.apply(check_logic, axis=1)

    return df


# -----------------------------
# 6. GENERATE OUTPUT
# -----------------------------

def generate_report(df):

    report = df[[
        "referral_id",
        "referral_source",
        "referral_source_category",
        "referral_at",
        "referrer_id",
        "name",
        "phone_number",
        "referee_name",
        "referee_phone",
        "transaction_id",
        "transaction_status",
        "transaction_at",
        "transaction_location",
        "transaction_type",
        "updated_at",
        "is_business_logic_valid"
    ]]

    report.to_csv("output/referral_report.csv", index=False)

    print("✅ Report generated successfully!")
    print("📊 Total rows:", len(report))


# -----------------------------
# MAIN PIPELINE
# -----------------------------

def main():

    print("🚀 Starting Referral Data Pipeline...")

    user_referrals, user_logs, referral_logs, referral_status, rewards, transactions, leads = load_data()

    user_referrals, transactions = clean_data(user_referrals, transactions)

    df = process_data(user_referrals, user_logs, referral_logs, referral_status, rewards, transactions)

    df = add_source_category(df, leads)

    df = validate_business_logic(df)

    generate_report(df)

    print("🎉 Pipeline completed successfully!")


if __name__ == "__main__":
    main()
