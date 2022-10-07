#!/usr/bin/python3
"""
    script that lists all states with a name starting
    with N (upper N) from the database hbtn_0e_0_usa
    Usage:
    ./1-filter_states.py <mysql username> <mysql password> <database name>
"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM `states` ORDER BY `id`")
    [print(state) for state in cur.fetchall() if state[1][0] == "N"]
