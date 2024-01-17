# Flask Application Load Balanced Project

Setup:
- install poetry
- make build
- make tar
- run cdk stuff

# My notes

- Make sure stack name doesnt start with aws, ecs, or fargate.
- Make sure that if youre compiling the docker image on m1 you use ARM/Linux runtime environment for task
- Image is being pushed from "asset" where it builds locally and deploys the container. Not from ecr. Couldnt figure out permission to pull from ecr
- When building from asset, have to specify a directory that is not in the path of the cdk folder otherwise you get an infinite path error
    - This created trouble for the structure of having one poetry environment outside the scope of the docker container
    - work around is to copy the dependencies from poetry into a requirements file that is in the app folder alongside the dockerfile
    - could maybe use a tarball with an extra deployment step?
- To debug deploy problems, go into task and look at deploy logs and view a failed task instantiation, this is where the helpful error is
- When seeing an error like this `fail: No ECR repository named 'cdk-hnb659fds-container-assets-202571202047-us-east-2' in account 202571202047. Is this account bootstrapped?` can try delete cloudformation cdk stack and cdk s3 buckets then performing a boostrap again. Someone recommended cdk bootstrap --force but that didnt work

## TODO
make file commands for cdk?
build from asset not from tarball
certs
domain name

## CDK Ccommands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation
