#!/usr/bin/python3
""" displays all values in the states table of hbtn_0e_0_usa
    where name matches the argument.
    """
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute(
        "SELECT cities.id, cities.name, states.name FROM states \
            JOIN cities ON states.id = cities.state_id ORDER BY cities.id ASC")
    rows = cur.fetchall()
    for r in rows:
        print(r)
    cur.close()
    db.close()
