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


