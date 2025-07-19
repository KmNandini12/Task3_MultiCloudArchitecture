# Task3_MultiCloudArchitecture

**Company**: CODTECH IT SOLUTIONS

**Name**: Kumari Nandini

**Intern ID**: CT08DL671

**Domain**: Cloud Computing

**Duration**: 8 Weeks

**Mentor**: NEELA SANTOSH 

# Task 3 – Design a `Multi-Cloud` architecture where services are distributed across two cloud providers

## Objective

The goal of this task is to access an AWS S3 bucket programmatically from Google CloudShell using Python and the Boto3 library.
The script lists the objects stored in the S3 bucket using secure IAM user credentials and appropriate permissions. 

---

## Tools & Technologies Used

- **AWS S3** – Simple Storage Service used to store files.
- **IAM (Identity and Access Management)** – Used to securely control access to AWS services.
- **Google CloudShell** – Online terminal to run code from a Linux environment.
- **Python 3.12** – Programming language used to write the access script.
- **Boto3** – Official AWS SDK for Python to interact with AWS services such as S3.

---

## Step-by-Step Implementation

### 1. IAM User Creation and Policy Setup
-Created an IAM user (nandiniemp) with programmatic access.
-Generated Access Key & Secret Access Key securely from the IAM section.

### 2. Python Script for S3 Access
-Installed Boto3 in Google Cloud Shell using pip install boto3.`pip install boto3`
-Wrote a Python script (s3_fetch.py) using Boto3 to access and list objects from the S3 bucket.
- The credentials (`aws_access_key_id`, `aws_secret_access_key`) and region were passed to the boto3 client.

### 3. Running the Script in Google CloudShell
- Google CloudShell was opened.
- Boto3 was installed using:

```bash
pip install boto3
```
- Used the `nano` command to create and edit the Python script directly in the terminal:
  
```bash
nano s3_fetch.py
```

- It was executed using:

```bash
python s3_fetch.py
```
-Ran the script from Cloud Shell and successfully fetched the list of uploaded files in the `codetech-internship-bucket`.
- Output successfully displayed:
  ```
  hello-codetech.txt
  category_image.jpg
  CLOUD COMPUTING.pdf
  ```

---

## Problems Faced and Resolution

### Access Denied Error

When the script was initially run, the following error was encountered:

```
ClientError: An error occurred (AccessDenied) when calling the ListObjectsV2 operation:
User is not authorized to perform: s3:ListBucket
```

**Resolution:**
- The IAM policy was updated to explicitly allow `s3:ListBucket`, `s3:GetObject`, and `s3:PutObject` permissions on the target bucket.
- After attaching the updated policy to the IAM user, the script executed successfully and returned the expected results.

### Credential Safety

Hardcoding credentials is unsafe for public repositories. To address this:
- The actual script `s3_fetch.py` was excluded from upload.
- A redacted placeholder version (`s3_fetch.json`) was uploaded instead.

---

## Uploaded Files
`s3bucketpolicy.json` -
 IAM policy document allowing required S3 actions.
 
`s3_fetch.json` -
Placeholder version of the Python script.

---

## Screenshots

- `policy-editor.png` –  
  IAM policy editor where `s3:ListBucket`, `s3:GetObject`, and `s3:PutObject` permissions were configured.

- `pip-install-boto3.png` –  
  Shows successful installation of the boto3 library in Google CloudShell.

- `access-key.png` –  
  Screenshot showing generated IAM access key credentials used in the Python script.

- `script-output.png` –  
  Output from the Python script that lists the S3 objects stored in the bucket.

---

## Summary

This task demonstrated how to:
- Install and use the `boto3` SDK from Google CloudShell.
- Programmatically access and list S3 bucket contents.
- Troubleshoot IAM permission issues and fix them by editing policy.
- Protect access credentials by sharing only placeholder code.

**OUTPUT**:

<img width="963" height="130" alt="Image" src="https://github.com/user-attachments/assets/78a2a6e1-f1c2-49e6-8b4f-528fe82dbf31" />

<img width="2880" height="1800" alt="Image" src="https://github.com/user-attachments/assets/e4d47727-4dd0-4446-b5a4-9fce137c64c7" />
