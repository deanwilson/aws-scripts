# Historic Scripts

A collection of scripts I wrote a number of roles ago that I still had
on my local machine. I've pushed them up as small examples of `boto` usage
but not necessarily the best approach to scratching these itches.

## ami-usage-checker

A script to show both internal AMIs that are not being used and external AMIs
that are in use. This was used to keep an eye on the base images to ensure we
were not storing lots of unneeded ones or using unsupported third party images.

## iam-differ

A very basic way to show the difference between two AWS accounts IAM
resource lists. This was used to ensure all the required users and
policies were present in all the required regions.

## unused-security-groups

It's easy to lose track of detached security groups, especially
considering they don't cost anything! This script was an initial
prototype to help find no longer needed groups. It was written before
lots of things, such as RDS and VPCs had special groups, so it should
*not* be trusted.
