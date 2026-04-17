# AWS Serverless Event-Driven Application

## 📌 Overview
This project demonstrates a serverless event-driven architecture using AWS. When a file is uploaded to an S3 bucket, it triggers an AWS Lambda function which processes the event and logs output in CloudWatch.

## 🛠️ Technologies Used
- AWS S3
- AWS Lambda
- AWS IAM
- AWS CloudWatch

## ⚙️ Architecture
![Architecture](architecture.png)

## 🔄 Workflow
1. File uploaded to S3 bucket
2. S3 triggers Lambda function
3. Lambda processes event
4. Logs stored in CloudWatch

## 📸 Screenshots

### S3 Bucket
![S3](screenshots/s3.png)

### Lambda Function
![Lambda](screenshots/lambda.png)

### Trigger Configuration
![Trigger](screenshots/trigger.png)

### CloudWatch Logs
![Logs](screenshots/cloudwatch.png)

## 🚀 Key Features
- Event-driven architecture
- Serverless computing
- Auto scaling
- Cost efficient

## 👩‍💻 Author
Devaki

## 🧠 How It Works (Detailed)
When a file is uploaded to the S3 bucket, an event notification is generated. This event triggers the AWS Lambda function automatically. The Lambda function extracts the bucket name and file name from the event object and logs the information in CloudWatch for monitoring and debugging.

## 🔐 IAM & Security
The Lambda function uses an IAM role with AmazonS3ReadOnlyAccess policy to securely read S3 events and process data.

## 📊 Monitoring
All execution logs are captured in CloudWatch, allowing real-time monitoring and troubleshooting of the application.
