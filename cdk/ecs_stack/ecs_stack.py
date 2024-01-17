from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    aws_ecs as ecs,
    aws_ecs_patterns as ecs_patterns,
    aws_elasticloadbalancingv2 as elb_v2,
    aws_certificatemanager as cert_manager,
    aws_route53 as r53,
    CfnOutput
)
from constructs import Construct
import os

class FlaskStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Retrieve VPC information
        vpc = ec2.Vpc.from_lookup(
            self, 'VPC',
            # This imports the default VPC but you can also
            # specify a 'vpcName' or 'tags'.
            is_default=True)

        # ECS cluster
        cluster = ecs.Cluster(self, 'MyCluster', vpc=vpc)

        # SSL Certificate (replace with your certificate arn)
        # certificate_arn = 'arn:aws:acm:REGION:ACCOUNT:certificate/CERTIFICATE'


        tar_path = os.path.join(os.path.dirname(__file__), '../../image-target/flask-app-hello-world.tar')

        # Use ALB + Fargate from ECS patterns
        service = ecs_patterns.ApplicationLoadBalancedFargateService(
            self, 'MyFlaskApiWithFargate',
            cluster=cluster,
            cpu=512,
            memory_limit_mib=1024,
            desired_count=1,
            assign_public_ip=True,
            # Container image
            task_image_options=ecs_patterns.ApplicationLoadBalancedTaskImageOptions(
                # use GLOB pattern matching to exclude cdk folder
                image=ecs.ContainerImage.from_tarball(tar_path),
                container_port=5000),
            # Setting this to ARM64/Linux since this is how the container is built
            runtime_platform=ecs.RuntimePlatform(
                cpu_architecture=ecs.CpuArchitecture.ARM64,
                operating_system_family=ecs.OperatingSystemFamily.LINUX
            ),
            # Routing
            public_load_balancer=True,
            protocol=elb_v2.ApplicationProtocol.HTTP,
            #redirect_http=True,
            # certificate=cert_manager.Certificate.from_certificate_arn(self, 'cert', certificate_arn),
            # Replace with your domain
            #domain_name='cdk-flask-api.example.com.',
            #domain_zone=r53.HostedZone.from_lookup(self, "MyHostedZone", domain_name="example.com.")
            )

        service.target_group.configure_health_check(path='/health')

        # Output the DNS where you can access your service
        CfnOutput(
            self, "LoadBalancerDNS",
            value=service.load_balancer.load_balancer_dns_name
        )