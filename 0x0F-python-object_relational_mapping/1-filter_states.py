#!/usr/bin/python3

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM `states` ORDER BY `id`")
    for state in c.fetchall():
        print(f"({state[0]}, '{state[1]}')") if state[1][0] == "N" else ""
