from . import (
    Chef,
    Continents,
    Ingredients,
    Introduction,
    Recipes,
    Techniques
)

global units
units = None

valid_metric_input = [
    'm', 'i', 'metric', 'imperial'
]

def set_units(system):
    global units
    """Set flag for units. 1 == Imperial, 0 == Metric"""
    if system.lower() in ['m', 'metric']:
        print("Setting units type to metric")
        units = 0
        return
    if system.lower() in ['i', 'imperial']:
        print("Setting units type to imperial")
        units = 1


def get_units_system():
    global units
    while True:
        try:
            metric_in = input("Please set your preferred units method (imperial | metric): ")
        except (NameError, SyntaxError) as err:
            print(err)
            continue
        if metric_in in valid_metric_input:
            set_units(metric_in)
            break
        print("Invalid inputs\n")

import os
if os.environ.get("Cooking"):
    get_units_system()