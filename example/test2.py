#!/usr/bin/env pythin
#
# this is a test script for DB class
#

import os
import sys
import random

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(__file__)),
                                'lib'))
import db
import sql

def main():
    # test for db.py
    db1 = db.Mysql()
    db1.connect()
    db1.query()
    db1.disconnect()

    # test for sql.py
    sql1 = sql.Mysql()
    res= sql1.query(sql.Testtb1, 'id', 1)
    print(res)

    names = ("apple", "banana", "orange")
    name = random.choice(names)
    print ("the random choice is %s" % name)
    res.name = name
    sql1.session.commit()
    res= sql1.query(sql.Testtb1, 'id', 1)
    print(res)

    items = sql1.queryall(sql.Testtb1)
    for res in items:
        print(res)
    sql1.queryall();


if __name__ == "__main__":
    main()

