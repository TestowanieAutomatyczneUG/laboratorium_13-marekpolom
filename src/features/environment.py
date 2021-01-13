from behave import *
from src.sample.roman import Roman

def before_scenario(context, scenario):
    context.c = Roman

def after_scenario(context, scenario):
    context.c = None