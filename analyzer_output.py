#!/usr/bin/env python
# encoding: utf-8

from analyzer import OUTPUT_SCHEMA
import jsonschema
import texttable
import argparse
import pprint
import pipe
import sys

def setup_argparser():
    argparser = argparse.ArgumentParser(description="""Render and verify Cortex-Analyzer output.
        Pass JSON-output via stdin for verification.""")
    argparser.add_argument("--all", "-A", action="store_true", help="Show all aspects")
    argparser.add_argument("--artifacts", "-a", action="store_true", help="Show job artifacts")
    argparser.add_argument("--taxonomies", "-t", action="store_true", help="Show job taxonomies")
    argparser.add_argument("--full", "-f", action="store_true", help="Show full job report")
    return argparser

def render_header(data):
    return data.keys()

def render_values(data):
    return data.values()

def render_outputdata(data, args):
    if args.get("all", False) or args.get("artifacts", False):
        artifacts = data.get("artifacts", [])
        if artifacts:
            table = texttable.Texttable()
            table.header(render_header(artifacts[0]))
            table.add_rows(list(map(render_values, artifacts)), header=False)
            print(table.draw())
        else:
            print("No artifacts available!")

    if args.get("all", False) or args.get("taxonomies", False):
        summary = data.get("summary", {})
        taxonomies = summary.get("taxonomies", [])
        if taxonomies:
            table = texttable.Texttable()
            table.header(render_header(taxonomies[0]))
            table.add_rows(list(map(render_values, taxonomies)), header=False)
            print(table.draw())
        else:
            print("No taxonomies available!")

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
