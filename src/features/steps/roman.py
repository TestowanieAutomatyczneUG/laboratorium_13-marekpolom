from behave import *
from src.sample.roman import roman
from assertpy import *

@given(u'Roman app is run')
def step_impl(context):
    context.roman = roman


@when(u'I input "1"')
def step_impl(context):
    context.result = context.roman(1)


@then(u'I get result "I"')
def step_impl(context):
    assert_that(context.result).is_equal_to('I')

@when(u'I input "4"')
def step_impl(context):
    context.result = context.roman(4)

@then(u'I get result "IV"')
def step_impl(context):
    assert_that(context.result).is_equal_to('IV')


@when(u'I input "5"')
def step_impl(context):
    context.result = context.roman(5)


@then(u'I get result "V"')
def step_impl(context):
    assert_that(context.result).is_equal_to('V')


@when(u'I input "27"')
def step_impl(context):
    context.result = context.roman(27)


@then(u'I get result "XXVII"')
def step_impl(context):
    assert_that(context.result).is_equal_to('XXVII')


@when(u'I input "93"')
def step_impl(context):
    context.result = context.roman(93)


@then(u'I get "XCIII"')
def step_impl(context):
    assert_that(context.result).is_equal_to('XCIII')


@when(u'I input "163"')
def step_impl(context):
    context.result = context.roman(163)


@then(u'I get "CLXIII"')
def step_impl(context):
    assert_that(context.result).is_equal_to('CLXIII')


@when(u'I input "575"')
def step_impl(context):
    context.result = context.roman(575)


@then(u'I get "DLXXV"')
def step_impl(context):
    assert_that(context.result).is_equal_to('DLXXV')


@when(u'I input "1024"')
def step_impl(context):
    context.result = context.roman(1024)


@then(u'I get "MXXIV"')
def step_impl(context):
    assert_that(context.result).is_equal_to('MXXIV')


@when(u'I input "3000"')
def step_impl(context):
    context.result = context.roman(3000)


@then(u'I get "MMM"')
def step_impl(context):
    assert_that(context.result).is_equal_to('MMM')