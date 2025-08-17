import boto3
import pandas as pd


def delete_alarms_from_csv(csv_file):
    # Read the CSV file
    df = pd.read_csv(csv_file)

    # Ensure required columns exist
    required_columns = {"AccountName", "RegionName", "AlarmName"}
    if not required_columns.issubset(df.columns):
        raise ValueError(f"CSV must contain {required_columns}")

    # Add a new column 'DeletionStatus' to store the deletion status
    df['DeletionStatus'] = ''

    # Iterate over the DataFrame
    for index, row in df.iterrows():
        try:
            # Create a boto3 session with the region from the CSV file
            session = boto3.Session(region_name=row['RegionName'])
            cloudwatch = session.client('cloudwatch')

            # Delete the alarm
            cloudwatch.delete_alarms(
                AlarmNames=[row['AlarmName']]
            )
            print(f'[SUCCESS] Deleted alarm {row["AlarmName"]} in {row["RegionName"]}')
            df.at[index, 'DeletionStatus'] = 'Deleted'
        except Exception as e:
            print(f'[FAILED] Could not delete {row["AlarmName"]} in {row["RegionName"]}. Error: {str(e)}')
            df.at[index, 'DeletionStatus'] = f'Failed: {str(e)}'

    # Save results
    output_file = "deleted_alarms_output.csv"
    df.to_csv(output_file, index=False)
    print(f"\n✅ Results saved to {output_file}")


if __name__ == "__main__":
    delete_alarms_from_csv("alarms_input.csv")
