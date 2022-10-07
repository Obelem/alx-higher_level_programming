#!/usr/bin/python3
"""
    Aim: to write a script that is free from SQL injections
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC",
                (argv[4],))
    [print(state) for state in cur.fetchall()]
