import os
import json


def calculate_total(items, cache=[]):
    result = 0
    unused_counter = 0
    for item in items:
        if item:
            if isinstance(item, dict):
                if "price" in item:
                    if item["price"] > 0:
                        result += item["price"]
    return result
