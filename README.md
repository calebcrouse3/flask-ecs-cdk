
# Welcome to your CDK Python project!

Project has a folder for all cdk stuff. It has a requirments file for virtual environment to
execute cdk stuff.

Project has a folder for all the application stuff. It has a separate requirements file for the 
docker container that will be deploy to the ecs cluster.

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Enjoy!
