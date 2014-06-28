# cfn-summary #

The cfn summary command provides an overview of a CloudFormation json
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


