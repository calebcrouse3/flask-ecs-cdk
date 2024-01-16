from aws_cdk import (
    Stack,
    aws_ecs as ecs,
    aws_ec2 as ec2
)

from constructs import Construct


class EcsStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        vpc = ec2.Vpc(self, "flask-app-vpc", max_azs=2)

        cluster = ecs.Cluster(self, "flask-app-cluster", vpc=vpc)

        cluster.add_capacity(
            "DefaultAutoScalingGroup",
            instance_type=ec2.InstanceType("t2.micro"),
            desired_capacity=1
        )

        task_definition = ecs.Ec2TaskDefinition(
            self, "flask-app-task",
            network_mode=ecs.NetworkMode.AWS_VPC,
        )

        web_container = task_definition.add_container(
            "flask-app-container",
            image=ecs.ContainerImage.from_registry("flask-hello-world:latest"),
            cpu=100,
            memory_limit_mib=256,
            essential=True
        )

        port_mapping = ecs.PortMapping(
            container_port=5000,
            protocol=ecs.Protocol.TCP
        )

        web_container.add_port_mappings(port_mapping)

        security_group = ec2.SecurityGroup(
            self, "flask-app-scurity-group-1093827",
            vpc=vpc,
            allow_all_outbound=True
        )

        security_group.add_ingress_rule(
            ec2.Peer.any_ipv4(),
            ec2.Port.tcp(5000),
        )

        service = ecs.Ec2Service(
            self, "flask-app-service",
            cluster=cluster,
            task_definition=task_definition,
            security_groups=[security_group]
        )
