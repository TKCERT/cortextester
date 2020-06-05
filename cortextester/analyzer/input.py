#!/usr/bin/env python
# encoding: utf-8

from cortextester.analyzer.schema import INPUT_SCHEMA, CONFIG_SCHEMA
from cortextester import pipe, schema
import jsonschema
import argparse
import os.path
import pprint
import json
import sys

ALLOWED_PROXIES = ("http", "https")

def setup_argparser():
    argparser = argparse.ArgumentParser(description="""Create and verify Cortex-Analyzer input.
        Pass JSON-input via stdin for verification with specifying any argument.""")
    argparser.add_argument("--dataType", "-t", required=True, help="Input data type",
                           choices=INPUT_SCHEMA["properties"]["dataType"]["enum"])
    argparser.add_argument("--data", "-v", required=True, help="Input data value")
    argparser.add_argument("--tlp", "-l", type=int, choices=range(0, 4), help="Input data TLP level")
    argparser.add_argument("--pap", "-a", type=int, choices=range(0, 4), help="Input data PAP level")
    argparser.add_argument("--config", "-c", nargs=2, action="append", help="Config key and value")
    argparser.add_argument("--proxy", "-p", nargs=2, action="append", help="Proxy key and value")
    argparser.add_argument("-C", help="Configuration file", type=argparse.FileType("r"))
    return argparser

def build_inputdata(args):
    data = args.get("data")
    dataType = args.get("dataType")

    # Handle special file data type
    if dataType == "file":
        args["file"] = data
        args["filename"] = os.path.basename(data)
        del args["data"]

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

    # Handle configuration file defaults
    if "C" in args:
        configFile = json.load(args["C"])
        jsonschema.validate(configFile, CONFIG_SCHEMA)
        del args["C"]

        defaults = configFile.get("config", dict())
        if defaults:
            config = defaults
            if "config" in args:
                config.update(args["config"])
            args["config"] = config

        configItems = configFile.get("configurationItems", list())
        if configItems:
            defaults = schema.defaults_from_configuration_items(configItems)
            if defaults:
                config = defaults
                if "config" in args:
                    config.update(args["config"])
                args["config"] = config

            configSchema = schema.schema_from_configuration_items(configItems)
            jsonschema.validate(config, configSchema)

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
