#!/usr/bin/env python
# encoding: utf-8

from analyzer import OUTPUT_SCHEMA
import jsonschema
import pprint
import pipe

def main():
    pipe.fix_encoding()
    data = pipe.get_jsondata()
    jsonschema.validate(data, OUTPUT_SCHEMA)
    pprint.pprint(data)
    print("Everything ok, data validated successful!")

if __name__ == '__main__':
    main()
