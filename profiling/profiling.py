import pandas as pd
import os

DATA_PATH = "data"

def profile_table(file_path):

    df = pd.read_csv(file_path)

    profile = pd.DataFrame({
        "column_name": df.columns,
        "data_type": df.dtypes.values,
        "null_count": df.isnull().sum().values,
        "distinct_count": df.nunique().values
    })

    return profile


def main():

    print("📊 Running Data Profiling...\n")

    for file in os.listdir(DATA_PATH):

        file_path = os.path.join(DATA_PATH, file)

        if file.endswith(".csv"):

            print(f"\n🔍 Profiling: {file}")

            profile = profile_table(file_path)

            print(profile)

            # Save profiling output
            output_file = f"output/profile_{file.replace('.csv','')}.csv"
            profile.to_csv(output_file, index=False)

    print("\n✅ Profiling completed!")


if __name__ == "__main__":
    main()
