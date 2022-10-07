#!/usr/bin/python3
"""
Displays all values in the states table of the database hbtn_0e_0_usa
whose name matches that supplied as argument.
Usage: ./2-my_filter_states.py <mysql usr> <mysql pwd> <db name> <state name>
"""
import sys
import MySQLdb

if __name__ == "__main__":
    con = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name = '{:s}' ORDER BY \
        id ASC".format(sys.argv[4]))
    [print(state) for state in c.fetchall()]
