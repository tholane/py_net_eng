#! /usr/bin/env python
"""
Week 01 Exercise 08

Python module that uses ciscoconfparse to parse cisco config file
and find all of the crypto map entries in the file, i.e. lines that begin with:

'crypto map CRYPTO'

for each crypto map entry print out its children.

ciscoconfparse documentation:
    http://www.pennington.net/py/ciscoconfparse/index.html
"""
import ciscoconfparse

conf_file = "./cisco_conf"


def print_cisco_crypto_maps(conf_file):
    """
    Parse the configuration file conf_file and print all crypto map entries and
    all of their child attributes
    """
    parsed_config = ciscoconfparse.CiscoConfParse(conf_file)
    crypto_maps = parsed_config.find_objects("^crypto map CRYPTO")
    for crypto_map in crypto_maps:
        print(crypto_map.text)
        for crypto_item in crypto_map.children:
            print(crypto_item.text)
        print("\n")


if __name__ == "__main__":
    print_cisco_crypto_maps(conf_file)
