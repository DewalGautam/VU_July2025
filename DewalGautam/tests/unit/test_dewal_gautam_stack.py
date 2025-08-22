import aws_cdk as core
import aws_cdk.assertions as assertions

from dewal_gautam.dewal_gautam_stack import DewalGautamStack

# example tests. To run these tests, uncomment this file along with the example
# resource in dewal_gautam/dewal_gautam_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = DewalGautamStack(app, "dewal-gautam")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
