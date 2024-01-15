import aws_cdk as core
import aws_cdk.assertions as assertions

from aws_ecs_cdk_template.aws_ecs_cdk_template_stack import AwsEcsCdkTemplateStack

# example tests. To run these tests, uncomment this file along with the example
# resource in aws_ecs_cdk_template/aws_ecs_cdk_template_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = AwsEcsCdkTemplateStack(app, "aws-ecs-cdk-template")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
