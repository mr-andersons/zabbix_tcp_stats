#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import json

def main(argv):
    """ main """

    data = [{"{#SERVICE}": service} for service in sys.argv[1:]]
    print(json.dumps({"data": data}, indent=4))

if __name__ == "__main__":
    main(sys.argv[1:])
