#!/usr/bin/python3

import sys
import MySQLdb

"""
    script that lists all states with a name starting
    with N (upper N) from the database hbtn_0e_0_usa
    Usage:
    ./1-filter_states.py <mysql username> <mysql password> <database name>
"""

if __name__ == "__main__":
    con = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = con.cursor()
    cur.execute("SELECT * FROM `states` ORDER BY `id`")
    [print(state) for state in cur.fetchall() if state[1][0] == "N"]
