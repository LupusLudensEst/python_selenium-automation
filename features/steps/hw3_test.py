from behave import *

use_step_matcher("re")


@given("I am on google search page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print('1. I am on google search page')


@when("I type in text to search")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print('2. I type in text to search')


@step("I hit search button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print('3. I hit search button')


@then("I should be on the search results page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print('4. I should be on the search results page')