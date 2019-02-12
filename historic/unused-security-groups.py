#!/usr/bin/env python
import sys
import os
import argparse
import ConfigParser
import boto.ec2

#####################################

def script_name():
    return os.path.basename(sys.argv[0] )

#####################################

def get_regions(region ):

    regions = []
    all_regions = [ r.name for r in sorted(boto.ec2.regions()) ]

    if region == 'all':
        regions = all_regions
    elif region not in all_regions:
        region_msg = '{}: region must be one of {}'.format(
            script_name(), ', '.join(all_regions)
        )
        sys.stderr.write(region_msg)
        sys.exit(1)
    else:
        regions.append(region)

    return regions

#####################################

def get_connection(region, config, verbose):

    if not config.has_section(region):
        if verbose == True:
            sys.stderr.write("{}: no config for region [{}] found\n".format(
                script_name(), region
            ))
        return False

    access_key_id     = config.get(region, 'aws_access_key_id')
    secret_access_key = config.get(region, 'aws_secret_access_key')

    connection = boto.ec2.connect_to_region(
        region,
        aws_access_key_id     = access_key_id,
        aws_secret_access_key = secret_access_key
    )

    return connection

#####################################

def active_security_groups(connection):

    instances = connection.get_all_instances()

    security_groups = []
    for instance in instances:
        named_groups = [ sg.name for sg in instance.groups ]
        security_groups.extend(named_groups)

    return set(security_groups)

#####################################

def ignored_security_groups(region, config):
    ignored = []

    if config.has_option(region, 'ignored_security_groups'):
        ignored = config.get(region, 'ignored_security_groups')
        ignored = [sg.strip() for sg in ignored.split(',')]

    return set(ignored)

#####################################

parser = argparse.ArgumentParser()

parser.add_argument('-r', '--region', action='store', help='The AWS region to check', default='all')
parser.add_argument('--verbose', action='store_true', default=False)
parser.add_argument('-f', '--config-file', dest='configfile', action='store',
    help='The config file to use'
)

args = parser.parse_args()

config = ConfigParser.ConfigParser()
config.read(args.configfile)

#########################################

regions = get_regions(args.region)


# loop through the regions and check each given one
for region in regions:
    conn = get_connection(region, config, args.verbose)

    if conn == False:
        continue

    security_groups = [ sg.name for sg in conn.get_all_security_groups() ]
    ignored_groups  = ignored_security_groups(region, config)

    active_groups = active_security_groups(conn)

    unused_groups = set(security_groups) - active_groups
    unused_groups = unused_groups - ignored_groups
    unused_groups = ', '.join(unused_groups)

    if unused_groups:
        print("Region: {} unused security groups: {}").format(region, unused_groups )
    else:
        print("Region: {} no unused security groups").format(region)
