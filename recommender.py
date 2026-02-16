
from collections import Counter
import datetime

SUBSTITUTES = {
    "milk": ["almond milk", "soy milk"],
    "sugar": ["brown sugar", "stevia"]
}


def frequency_suggestions(history):
    freq = Counter(history)
    return [item for item, count in freq.items() if count > 2]


def seasonal_suggestions():
    month = datetime.datetime.now().month

    if month in [4, 5, 6]:
        return ["mango", "cold drinks"]
    elif month in [12, 1]:
        return ["soup", "dry fruits"]

    return []


def substitute_suggestions(item):
    for key in SUBSTITUTES:
        if key in item:
            return SUBSTITUTES[key]
    return []
