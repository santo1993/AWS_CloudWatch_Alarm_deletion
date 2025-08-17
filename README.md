# AWS_CloudWatch_Alarm_deletion

# AWS CloudWatch Alarm Deletion Script

This Python script automates the deletion of **AWS CloudWatch Alarms** from a list provided in a CSV file.  
It uses **boto3** (AWS SDK for Python) to connect to CloudWatch and delete the alarms based on their `AlarmName` and `Region`.

---

## 🚀 Features
- Reads alarms and regions from a CSV file
- Deletes specified CloudWatch alarms
- Logs success/failure for each alarm
- Saves results with a `DeletionStatus` column

---

## 📋 Prerequisites

1. **AWS Credentials**:  
   Ensure you have AWS credentials configured.  
   Supported methods:
   - AWS CLI (`aws configure`)
   - Environment variables (`AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_SESSION_TOKEN`)
   - IAM role (if running on EC2/CloudShell)

2. **Dependencies**:
   Install dependencies using:

    pip install boto3 pandas


---

## 📂 CSV Input Format

The script expects an input CSV file (e.g., `alarms_input.csv`) with the following columns:

| AccountName | RegionName   | AlarmName                |
|-------------|--------------|--------------------------|
| DevAccount  | us-east-1    | CPUHighAlarm             |
| TestAccount | ap-south-1   | MemoryUtilizationAlarm   |

---

## ▶️ Usage

1. Save your alarm details in `alarms_input.csv`
2. Run the script:
3. python delete_alarms.py


3. After execution, check the file `deleted_alarms_output.csv` for results.

---

## 📊 Output

The output CSV will look like this:

| AccountName | RegionName   | AlarmName                | DeletionStatus     |
|-------------|--------------|--------------------------|--------------------|
| DevAccount  | us-east-1    | CPUHighAlarm             | Deleted            |
| TestAccount | ap-south-1   | MemoryUtilizationAlarm   | Failed: AccessDenied |

---

## ⚠️ Notes
- Deleted alarms **cannot be recovered**; proceed carefully.
- Ensure your IAM permissions allow `cloudwatch:DeleteAlarms`.

---

## 📜 License
MIT License – Feel free to use and modify.

