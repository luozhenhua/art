#!/usr/bin/env pythin
#
# this is a test script
#

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(__file__)),
                                'lib'))

from target import *

def main():
    t1 = Target("127.0.0.1", "test", "test")
    t1.connect()


if __name__ == "__main__":
    main()

