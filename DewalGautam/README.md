## DewalGautam Web Health Monitoring
## Introduction

Ensuring websites remain reliable and responsive is critical for user experience and business continuity. This project implements an automated web health monitoring system built entirely on AWS serverless technologies. It checks the availability and latency of web resources, stores metrics, and triggers alerts when performance degrades or downtime occurs.

The project is packaged as an AWS CDK application, making deployment and infrastructure management simple and repeatable.

## Key Features

Automated and scheduled website health checks

Real-time metrics published to Amazon CloudWatch

Customizable alarms for downtime and latency thresholds

Email notifications using Amazon SNS

Infrastructure managed with AWS CDK (Infrastructure as Code)

Optional persistence of results in Amazon DynamoDB

## System Architecture

The monitoring system is composed of fully managed AWS services:

AWS Lambda → Performs health checks and reports results

Amazon CloudWatch → Stores metrics, creates dashboards, and triggers alarms

Amazon EventBridge → Runs the Lambda function on a fixed schedule

Amazon SNS → Sends alerts to configured email addresses

Amazon DynamoDB (optional) → Persists results for long-term tracking

AWS CDK → Provisions and manages the complete stack

(Insert your architecture diagram or system flow here)

## Setup Guide
## Prerequisites

AWS account with appropriate permissions

AWS CLI configured locally

Node.js and npm installed

Python 3.8+ installed

AWS CDK installed globally (npm install -g aws-cdk)

Verified email address for SNS notifications

## Installation Steps
# 1. Clone the repository
git clone https://github.com/DewalGautam/VU_July2025.git
cd VU_July2025/DewalGautam

# 2. Create and activate a Python virtual environment
python -m venv .venv
.venv\Scripts\activate  # On Windows
source .venv/bin/activate  # On Mac/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Synthesize the CDK application
cdk synth

# 5. Bootstrap CDK (first-time setup only)
cdk bootstrap

# 6. Deploy the stack
cdk deploy

## Configuration

Edit modules/constants.py → specify the target URL and metric namespace.

Update the SNS email address in the stack file to receive alerts.

## Usage

Monitoring → The Lambda function runs every minute and checks the configured URL.

Metrics → Results are published to CloudWatch for analysis and visualization.

Alarms → CloudWatch raises alarms on downtime or high latency.

Notifications → Alerts are delivered to the registered email address via SNS.

Dashboard → CloudWatch dashboards provide a live view of system health.

## Results & Screenshots






## Project Structure
DewalGautam/
├── app.py
├── cdk.json
├── requirements.txt
├── modules/
│   ├── WebHealthLambda.py
│   ├── HelloWorld.py
│   └── constants.py
├── dewal_gautam/
│   └── dewal_gautam_stack.py
└── tests/
    └── unit/
        └── test_dewal_gautam_stack.py

## Contribution

Contributions are encouraged. Please open issues for bugs or feature requests, and submit pull requests for proposed improvements.

## License

This project is distributed under the MIT License.

## Author

Dewal Gautam