#! /usr/bin/env python
"""
Week 01 Exercise 06

Python script that creates a list. One of the elements of the list is a
dictionary with three keys.

The list is written to files using both YAML and JSON formats. The YAML file
is in the expanded form.
"""

import yaml
import json

test_list = [x+1 for x in range(5)]
test_dict = {"key01": "value01", "key02": "value02", "key03": "value03"}
test_list.append(test_dict)

with open("test_file.yml", 'w') as yml_file:
    # yml_file.write(yaml.dump(test_list))
    yaml.dump(test_list, yml_file, default_flow_style=False)

with open("test_file.json", 'w') as json_file:
    json_file.write(json.dumps(test_list, sort_keys=True))
