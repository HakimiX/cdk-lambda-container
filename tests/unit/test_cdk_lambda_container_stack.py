import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_lambda_container.cdk_lambda_container_stack import CdkLambdaContainerStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_lambda_container/cdk_lambda_container_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkLambdaContainerStack(app, "cdk-lambda-container")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
