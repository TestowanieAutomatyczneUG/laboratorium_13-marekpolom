from behave import *
from src.sample.fizzBuzz import FizzBuzz
from assertpy import *

@given(u'Fizzbuzz app is run')
def step_impl(context):
    context.fizzbuzz = FizzBuzz


@when(u'I input "6"')
def step_impl(context):
    context.result = context.fizzbuzz.game(6)


@then(u'I get result "Fizz"')
def step_impl(context):
    assert_that(context.result).is_equal_to("Fizz")


@when(u'I input "10"')
def step_impl(context):
    context.result = context.fizzbuzz.game(10)


@then(u'I get result "Buzz"')
def step_impl(context):
    assert_that(context.result).is_equal_to("Buzz")


@when(u'I input "15"')
def step_impl(context):
    context.result = context.fizzbuzz.game(15)


@then(u'I get result "FizzBuzz"')
def step_impl(context):
    assert_that(context.result).is_equal_to("FizzBuzz")


@when(u'I input "2"')
def step_impl(context):
    context.result = context.fizzbuzz.game(2)


@then(u'I get result "None"')
def step_impl(context):
    assert_that(context.result).is_equal_to("None")


@when(u'I input "fizz"')
def step_impl(context):
    context.result = context.fizzbuzz.game("fizz")


@then(u'I get "ValueError"')
def step_impl(context):
    assert_that(context.result).is_equal_to("ValueError")