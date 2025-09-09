import boto3

class CloudWatchMetricPublisher:
    """
CloudWatch Metric Publisher for Dewal Gautam's Web Health Project
Author: Dewal Gautam
"""

class DewalCloudWatchPublisher:
    """Publishes custom metrics to AWS CloudWatch for Dewal Gautam's project."""
    def __init__(self):
        self.client = boto3.client('cloudwatch')

    def __init__(self):
        self.client = boto3.client('cloudwatch')

    def put_metric_data(self, namespace, metric_name, dimensions, value):
        """Publishes a single metric data point to CloudWatch."""
        response = self.client.put_metric_data(
            Namespace=namespace,
            MetricData=[
                {
                    'MetricName': metric_name,
                    'Dimensions': dimensions,
                    'Value': value,
                }
            ]
        )
        response = self.client.put_metric_data(
            Namespace=namespace,
            MetricData=[
                {
                    'MetricName': metric_name,
                    'Dimensions': dimensions,
                    'Value': value,
                }
            ]
        )