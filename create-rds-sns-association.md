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
