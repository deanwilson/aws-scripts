# aws-regions #

A simple command line tool to print the AWS region code and description.
Written to stop people asking 'Is that one Virginia?'

    $ aws-regions
    ap-northeast-1                 Asia Pacific (Tokyo)
    ... snip ...
    us-west-2                      US West (Oregon)

    $ aws-regions ap-
    ap-northeast-1                 Asia Pacific (Tokyo)
    ap-southeast-1                 Asia Pacific (Singapore)
    ap-southeast-2                 Asia Pacific (Sydney)

    $ aws-regions eu-central-1
    EU (Frankfurt)

# cfn-show #

The cfn-show command provides a number of different views of a CloudFormation json
templates contents.

The basic command will display all the names of all resources in a given
section, defaulting to 'Resources'.

    $ cfn-show templates/web-app.json

    LocationAppServerELB
    AWS::ElasticLoadBalancing::LoadBalancer

    LocationAppServerFleet
    AWS::AutoScaling::AutoScalingGroup

    LocationAppServerFleetLaunchConfig
    AWS::AutoScaling::LaunchConfiguration


You can also specify an alternate section to display.

    $ cfn-show templates/web-app.json outputs

    HTTPSURL
    Outputs


If you are unsure of which sections a template contains you can run

    $ cfn-show templates/web-app.json sections

    Conditions
    Mappings
    Outputs
    Parameters
    Resources


Once you've found the section and resource you're interested in
you can expand it -


    $ cfn-show templates/web-app.json resources IAMRolesStack

    {
        "Type": "AWS::CloudFormation::Stack",
        "Properties": {
            "TemplateURL": {
                "Ref": "IAMRolesURL"
            },
            "Parameters": {
                "App": "location",
                "Type": "webapp",
                "Stack": {
                    "Ref": "CommonStackName"
                },
                "Env": {
                    "Ref": "DeploymentEnvironment"
                }
            }
        }
    }
    

You can alter the format of this display with the 'indent' and 'show name'
options:

    $ cfn-show templates/web-app.json resources IAMRolesStack -n -i 2

    "IAMRolesStack" :  {
      "Type": "AWS::CloudFormation::Stack",
      "Properties": {
        "TemplateURL": {
          "Ref": "IAMRolesURL"
        },
      ... snip ...



# cfn-summary #

The cfn-summary command provides an overview of a CloudFormation json
templates contents.

    $ cfn-summary templates/web-app.json

    Conditions has 2 resources
    Mappings has 1 resources
    Outputs has 2 resources
    Parameters has 20 resources
    Resources has 10 resources

You can also specify sections to summarise. In this example we check the
number of inputs and outputs for a stack.

    $ cfn-summary templates/web-app.json parameters,outputs

    Outputs has 2 resources
    Parameters has 20 resources


# unused-iam-profiles #

The unused-iam-profiles command attempts to list any IAM instance profiles
that have been created but are not in use by any running EC2 instances.

    unused-iam-profiles

    23 of 100 IAM Profiles are unused ## BETA!
    =============
    ....
    dwilson-edda-test
    stage-ice-profile
    ....

It is written in ruby and uses the AWS Ruby SDK, available via 'gem install
aws-sdk'


# create-rds-sns-association #

This script creates an association between an RDS instance and an SNS
topic. Both of which should already exist. This subscription places
events from categories like 'failover' and 'configuration changes' from
the RDS instance on to the given SNS topic. Something you unfortunately
can not currently do from Ansible or CloudFormation.

    Create a new event subscription for all events
    create-rds-sns-association -n event_sub_name -i rds-inst-phy-id -t arn:snip:snip -r eu-west-1

    Create a new event subscription and show boto debug
    create-rds-sns-association -n event_sub_name -i rds-inst-phy-id -t arn:snip:snip -r eu-west-1 --debug

Notes
 - this does not use the environment variables for setting region yet.
 - it currently adds -all- the event types for a given source.

