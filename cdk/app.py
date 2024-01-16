#!/usr/bin/env python3
import aws_cdk as cdk

from ecs_stack.ecs_stack import EcsStack

app = cdk.App()
EcsStack(app, "EcsStack", env=cdk.Environment(account='202571202047', region='us-east-2'))
app.synth()
