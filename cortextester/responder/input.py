#!/usr/bin/env python
# encoding: utf-8

from cortextester.responder.schema import INPUT_SCHEMA
from cortextester import pipe
import jsonschema
import argparse
import os.path
import pprint
import json
import sys

ALLOWED_PROXIES = ("http", "https")

def setup_argparser():
    argparser = argparse.ArgumentParser(description="""Create and verify Cortex-Responder input.
        Pass JSON-input via stdin for verification with specifying any argument.""")
    argparser.add_argument("--dataType", "-t", required=True, help="Input data type (not implemented)")
    argparser.add_argument("--data", "-v", required=True, help="Input data value (not implemented)")
    argparser.add_argument("--tlp", "-l", type=int, choices=range(0, 4), help="Input data TLP level")
    argparser.add_argument("--pap", "-a", type=int, choices=range(0, 4), help="Input data PAP level")
    argparser.add_argument("--config", "-c", nargs=2, action="append", help="Config key and value")
    argparser.add_argument("--proxy", "-p", nargs=2, action="append", help="Proxy key and value")
    return argparser

def build_inputdata(args):
    # TODO: implement support for Responder data types

    # Purge missing arguments
    for k, v in tuple(args.items()):
        if v is None:
            del args[k]

    # Handle multiple proxy arguments
    proxy = args.get("proxy", dict())
    if proxy:
        proxy = dict(filter(lambda i: i[0] in ALLOWED_PROXIES, proxy))
    if "proxy" in args:
        del args["proxy"]

    # Handle multiple config arguments
    config = args.get("config", dict())
    if config:
        config = dict(config)
    if "config" in args:
        del args["config"]

    # Build proxy and config parameters
    if proxy:
        config["proxy"] = proxy
    if config:
        args["config"] = config

    return args

def main():
    pipe.fix_encoding()
    if len(sys.argv) > 1:
        argparser = setup_argparser()
        args = argparser.parse_args()
        data = build_inputdata(vars(args))
        jsonschema.validate(data, INPUT_SCHEMA)
        json.dump(data, sys.stdout, indent=4, sort_keys=True)
    else:
        data = pipe.get_jsondata()
        jsonschema.validate(data, INPUT_SCHEMA)
        pprint.pprint(data)
        print("Everything ok, data validated successful!")

if __name__ == '__main__':
    main()
