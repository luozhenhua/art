#!/usr/bin/env pythin
#
# this is a test script for DB class
#

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(__file__)),
                                'lib'))

from db import *

def main():
    db = Mysql()
    db.connect()
    db.query()
    db.disconnect()


if __name__ == "__main__":
    main()

