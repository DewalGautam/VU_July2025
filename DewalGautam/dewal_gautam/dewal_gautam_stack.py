from aws_cdk import (
    Duration,
    Stack,
    aws_lambda as lambda_,
    aws_iam,
    # aws_sqs as sqs,
)
from constructs import Construct
class DewalGautamStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        # The code that defines your stack goes here
        # example resource
        # queue = sqs.Queue(
        #     self, "DewalGautamQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
        lambda_function = lambda_.Function(
            self, "WebHealthFunction",
            runtime=lambda_.Runtime.PYTHON_3_13,
            handler="WebHealthLambda.lambda_handler",
            # handler="HelloWorld.lambda_handler",
            code=lambda_.Code.from_asset("./modules"),
            timeout=Duration.seconds(20),
        )
        # Use a supported runtime constant (PYTHON_3_9 instead of invalid PYTHON_3_9_6)
        # lambda_function = lambda_.Function(
        #     self, "WebHealthLambda",
        #     runtime=lambda_.Runtime.PYTHON_3_9,
        #     handler="WebHealthLambda.lambda_handler",
        #     code=lambda_.Code.from_asset("./modules"),
        #     description="Lambda to check web health (placeholder logic)"
        # )

        # Add permission to publish metrics to CloudWatch
        lambda_function.add_to_role_policy(
            aws_iam.PolicyStatement(
                effect=aws_iam.Effect.ALLOW,
                actions=["cloudwatch:PutMetricData"],
                resources=["*"]
            )
        )