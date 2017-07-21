#! /usr/bin/env python
"""
Week 10 Exercise 10
Python module that uses ciscoconfparse to parses config file
and finds all of the crypto map entries in the file, that aren't using AES

i.e.
configuration lines that begin with:

    'crypto map CRYPTO'

and don't use AES (determined based on the transform-set name)

    'tansform-set AES*'

ciscoconfparse documentation:
    http://www.pennington.net/py/ciscoconfparse/index.html
"""
import ciscoconfparse

conf_file = "./cisco_conf"


def get_cisco_crypto_maps_wo_attr(conf_file, map_attr):
    """
    Get all the crypto maps from the configuration with children that don't
    match the map_attr
    """
    parsed_config = ciscoconfparse.CiscoConfParse(conf_file)
    crypto_maps = parsed_config.find_objects_wo_child(
                    parentspec=r"^crypto map CRYPTO",
                    childspec=map_attr)
    return crypto_maps


def print_crypto_maps(crypto_maps):
    """
    Print passed list of crypto maps (list of IOSCfgLine Objests)
    including all child attributes of each map
    """
    for crypto_map in crypto_maps:
        print(crypto_map.text)
        for crypto_item in crypto_map.children:
            print(crypto_item.text)
        print("\n")


if __name__ == "__main__":

    # use of raw string literal "de-magics" \ unless it directly preceds a
    # quote which would terminate the string e.g. it doesn't interpret \n as a
    # newline - usefull for input things like regex
    print_crypto_maps(get_cisco_crypto_maps_wo_attr(
                        conf_file,
                        r"transform-set\s+\w*AES\w*"))
