#!/usr/bin/env python
# encoding: utf-8

from responder import OUTPUT_SCHEMA
import jsonschema
import texttable
import argparse
import pprint
import pipe
import sys

def setup_argparser():
    argparser = argparse.ArgumentParser(description="""Render and verify Cortex-Responder output.
        Pass JSON-output via stdin for verification.""")
    argparser.add_argument("--all", "-A", action="store_true", help="Show all aspects")
    argparser.add_argument("--operations", "-o", action="store_true", help="Show requested operations")
    argparser.add_argument("--full", "-f", action="store_true", help="Show full job report")
    return argparser

def render_header(data):
    return data.keys()

def render_values(data):
    return data.values()

def render_outputdata(data, args):
    if args.get("all", False) or args.get("operations", False):
        operations = data.get("operations", [])
        if operations:
            table = texttable.Texttable()
            table.header(render_header(operations[0]))
            table.add_rows(list(map(render_values, operations)), header=False)
            print(table.draw())
        else:
            print("No operations available!")

    if args.get("all", False) or args.get("full", False):
        full = data.get("full", {})
        if full:
            pprint.pprint(full)
        else:
            print("No full report available!")

def main():
    pipe.fix_encoding()
    if len(sys.argv) > 1:
        argparser = setup_argparser()
        args = argparser.parse_args()
    data = pipe.get_jsondata()
    jsonschema.validate(data, OUTPUT_SCHEMA)
    if len(sys.argv) > 1:
        render_outputdata(data, vars(args))
    else:
        pprint.pprint(data)
        print("Everything ok, data validated successful!")
    if not data.get("success", False):
        print("Job failed with error message: %s" % data.get("errorMessage", "n/a"))
        sys.exit(1)
    else:
        print("Job completed successful!")
        sys.exit(0)

if __name__ == '__main__':
    main()
