from behave import *
from src.sample.friendships import FriendShips
from assertpy import *

@given(u'Friendships app is run')
def step_impl(context):
    context.fs = FriendShips
    context.data = context.text.split(",")

@when(u'I input "Kowalski" and "Nowak"')
def step_impl(context):
    context.temp = context.fs()
    context.temp.makeFriends(context.data[0], context.data[1])


@then(u'I get result "Kowalski" is friend of "Nowak"')
def step_impl(context):
    assert_that(context.temp.data[context.data[0]]).is_equal_to([context.data[1]])


@then(u'And "Nowak" is friend of "Kowalski"')
def step_impl(context): 
    assert_that(context.temp.data[context.data[1]]).is_equal_to([context.data[0]])

@when(u'I input "Kowalski" and "Andrzejewicz"')
def step_impl(context):
    context.temp = context.fs()
    context.temp.makeFriends(context.data[0], context.data[1])

@when(u'I input "Kowalski" and "Kwiatkowski"')
def step_impl(context):
    context.temp.makeFriends(context.data[0], context.data[2])


@then(u'I get result "Kowalski" is friend of "Andrzejewicz"')
def step_impl(context):
    assert_that(context.temp.data[context.data[0]]).is_equal_to([context.data[1], context.data[2]])


@then(u'And "Andrzejewicz" is friend of "Kowalski"')
def step_impl(context): 
    assert_that(context.temp.data[context.data[1]]).is_equal_to([context.data[0]])

@then(u'I get result "Kowalski" is friend of "Kwiatkowski"')
def step_impl(context):
    assert_that(context.temp.data[context.data[0]]).is_equal_to([context.data[1], context.data[2]])

@then(u'And "Kwiatkowski" is friend of "Kowalski"')
def step_impl(context): 
    assert_that(context.temp.data[context.data[2]]).is_equal_to([context.data[0]])


@when(u'I input "Jakub" and "Marek"')
def step_impl(context):
    context.temp = context.fs()
    context.temp.makeFriends(context.data[0], context.data[1])


@when(u'I again input "Jakub" and "Marek"')
def step_impl(context):
    context.result = context.temp.makeFriends(context.data[0], context.data[1])


@then(u'I get result "Already friends!"')
def step_impl(context):
    assert_that(context.result).is_equal_to("Already friends!")


@when(u'I input "Jakub" and "Ola"')
def step_impl(context):
    context.temp = context.fs()
    context.temp.makeFriends(context.data[0], context.data[1])


@when(u'And I input "Jakub" and "Marek"')
def step_impl(context):
    context.temp.makeFriends(context.data[0], context.data[2])


@when(u'I get friends list of "Jakub"')
def step_impl(context):
    context.result = context.temp.getFriendsList(context.data[0])


@then(u'I get result "Marek, Ola"')
def step_impl(context):
    assert_that(context.result).is_equal_to([context.data[1], context.data[2]])


@when(u'I input "Ola" and "Marek"')
def step_impl(context):
    context.temp = context.fs()
    context.temp.makeFriends(context.data[0], context.data[1])


@when(u'I check if "Ola" and "Marek" are friends')
def step_impl(context):
    context.result = context.temp.areFriends(context.data[0], context.data[1])

@then(u'I get result "True"')
def step_impl(context):
    assert_that(context.result).is_true()


@when(u'I input "Ola" and "Jakub"')
def step_impl(context):
    context.temp = context.fs()
    context.temp.makeFriends(context.data[0], context.data[1])


@when(u'I check if "Marek" and "Jakub" are friends')
def step_impl(context):
    context.result = context.temp.areFriends(context.data[1], context.data[2])


@then(u'I get result "False"')
def step_impl(context):
    assert_that(context.result).is_false()


@when(u'I input "Adam" and "Jan"')
def step_impl(context):
    context.temp = context.fs()
    context.temp.makeFriends(context.data[0], context.data[1])


@when(u'I input "Tomek" and "Adam"')
def step_impl(context):
    context.temp.makeFriends(context.data[2], context.data[0])


@when(u'I check friends list of "Adam"')
def step_impl(context):
    context.result = context.temp.getFriendsList(context.data[0])


@then(u'I get result "Jan, Tomek"')
def step_impl(context):
    assert_that(context.result).is_equal_to([context.data[1], context.data[2]])


@when(u'I input "Jan" and "Tomek"')
def step_impl(context):
    context.temp = context.fs()
    context.temp.makeFriends(context.data[1], context.data[2])


@when(u'I input "Jan" and "Adam"')
def step_impl(context):
    context.temp.makeFriends(context.data[1], context.data[0])

@when(u'I check friends list of "Kasia"')
def step_impl(context):
    context.result = context.temp.getFriendsList(context.data[2])


@then(u'I get result ""')
def step_impl(context):
    assert_that(context.result).is_equal_to([context.data[1]])