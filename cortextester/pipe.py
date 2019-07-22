#!/usr/bin/env python
# encoding: utf-8

import codecs
import select
import json
import sys

# Copied from cortexutils/worker.py:Worker.__set_encoding()
def fix_encoding():
    try:
        if sys.stdout.encoding != 'UTF-8':
            if sys.version_info[0] == 3:
                sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
            else:
                sys.stdout = codecs.getwriter('utf-8')(sys.stdout, 'strict')
        if sys.stderr.encoding != 'UTF-8':
            if sys.version_info[0] == 3:
                sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')
            else:
                sys.stderr = codecs.getwriter('utf-8')(sys.stderr, 'strict')
    except Exception:
        pass

# Copied from cortexutils/worker.py:Worker.__init__()
def get_jsondata():
    r, _, _ = select.select([sys.stdin], [], [])
    if sys.stdin in r:
        return json.load(sys.stdin)
    else:
        raise RuntimeError("No data passed via stdin")
