#! /usr/bin/env python
"""
Week 01 Exercise 07

Python module that reads both a YAML file and the JSON file  and pretty prints
the data structure that is returned.
"""

import yaml
import json
import pprint

yaml_file_name = "test_file.yml"
json_file_name = "test_file.json"

with open(yaml_file_name, 'r') as yaml_file:
    pprint.pprint(yaml.load(yaml_file))

with open(json_file_name, 'r') as json_file:
    pprint.pprint(json.load(json_file))
