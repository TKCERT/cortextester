#!/usr/bin/env python
# encoding: utf-8

from cortextester.analyzer.schema import CONFIG_SCHEMA
from cortextester import pipe
import jsonschema
import texttable
import functools
import argparse
import pprint
import sys

def setup_argparser():
    argparser = argparse.ArgumentParser(description="""Render and verify Cortex-Analyzer config.
        Pass JSON-config via stdin for verification.""")
    argparser.add_argument("--all", "-A", action="store_true", help="Show all aspects")
    argparser.add_argument("--meta", "-m", action="store_true", help="Show meta data")
    argparser.add_argument("--config", "-c", action="store_true", help="Show configuration items")
    return argparser

def render_items(data):
    mapstr = functools.partial(map, str)
    for key, value in data.items():
        if key == "dataTypeList":
            value = ", ".join(value)
        elif key == "config":
            items = map(mapstr, value.items())
            value = "\n".join(map("=".join, items))
        elif key == "configurationItems":
            continue
        yield key, value

def render_header(data):
    return data.keys()

def render_values(data):
    return data.values()

def render_outputdata(data, args):
    if args.get("all", False) or args.get("meta", False):
        table = texttable.Texttable()
        table.header(("key", "value"))
        table.add_rows(render_items(data), header=False)
        print(table.draw())

    if args.get("all", False) or args.get("config", False):
        configItems = data.get("configurationItems", [])
        if configItems:
            table = texttable.Texttable()
            table.header(render_header(configItems[0]))
            table.add_rows(list(map(render_values, configItems)), header=False)
            print(table.draw())
        else:
            print("No configuration items available!")

def main():
    pipe.fix_encoding()
    if len(sys.argv) > 1:
        argparser = setup_argparser()
        args = argparser.parse_args()
    data = pipe.get_jsondata()
    jsonschema.validate(data, CONFIG_SCHEMA)
    if len(sys.argv) > 1:
        render_outputdata(data, vars(args))
    else:
        pprint.pprint(data)
        print("Everything ok, data validated successful!")

if __name__ == '__main__':
    main()
