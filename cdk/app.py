#!/usr/bin/env python3
import aws_cdk as cdk

from cdk.ecs_stack.ecs_stack import FlaskStack

app = cdk.App()
FlaskStack(app, "MyFlaskStack", env=cdk.Environment(account='202571202047', region='us-east-2'))
app.synth()
