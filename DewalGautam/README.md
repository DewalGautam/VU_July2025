# DewalGautam Web Health Monitoring

## Overview

This project provides an automated solution for monitoring the health of web resources using AWS Lambda, CloudWatch, and CDK. It checks website availability and latency, publishes metrics to CloudWatch, and triggers alarms and notifications for outages or performance issues.

## Features

- Automated Website Health Checks
- AWS Lambda Integration
- CloudWatch Metrics & Alarms
- EventBridge Scheduling
- SNS Notifications
- DynamoDB Integration (optional)
- CDK Infrastructure as Code

## Architecture

- Lambda Function: Executes health checks and publishes metrics
- CloudWatch: Stores metrics, triggers alarms, and provides dashboards
- EventBridge: Schedules Lambda invocations
- SNS: Sends notifications
- DynamoDB: Stores results (optional)
- CDK Stack: Manages all AWS resources

## Setup

### Prerequisites

- AWS account
- AWS CLI configured
- Node.js and npm
- Python 3.8+
- AWS CDK installed (`npm install -g aws-cdk`)
- Email address for notifications

### Installation

1. **Clone the repository:**
	```sh
	git clone https://github.com/yourusername/VU_July2025.git
	cd VU_July2025/DewalGautam
	```

2. **Set up Python environment:**
	```sh
	python -m venv .venv
	.venv\Scripts\activate  # On Windows
	pip install -r requirements.txt
	```

3. **Synthesize the CDK app:**
	```sh
	cdk synth
	```

4. **Bootstrap CDK (if first time):**
	```sh
	cdk bootstrap
	```

5. **Deploy the stack:**
	```sh
	cdk deploy
	```

## Configuration

- Edit `modules/constants.py` to set the URL to monitor and metric namespaces.
- Update the email address in the stack file for SNS notifications.

## Usage

- Monitoring: Lambda runs every minute, checks the target URL, and publishes metrics
- Alarms: CloudWatch triggers alarms for downtime or high latency
- Notifications: SNS sends email alerts when alarms are triggered
- Dashboard: View metrics and alarms in the CloudWatch dashboard

## File Structure

```
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
```

## Contributing

Contributions are welcome! Please open issues or submit pull requests for improvements.

## License

This project is licensed under the MIT License.

## Author

Dewal Gautam
