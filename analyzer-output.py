#!/usr/bin/env python
# encoding: utf-8

from analyzer import OUTPUT_SCHEMA
import jsonschema
import pprint
import pipe

if __name__ == '__main__':
    pipe.fix_encoding()
    data = pipe.get_jsondata()
    jsonschema.validate(data, OUTPUT_SCHEMA)
    pprint.pprint(data)
    print("Everything ok, data validated successful!")
