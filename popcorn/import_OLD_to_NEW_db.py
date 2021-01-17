#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Selfty
#
# Created:     16.01.2021
# Copyright:   (c) Selfty 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import sqlite3
conn_NEW = sqlite3.connect('E:\\popcorn\\popcorn\\db.sqlite3')
conn_OLD = sqlite3.connect('E:\\popcorn\\popcorn\\db_OLD.sqlite3')

for row in conn_OLD.execute("SELECT *, serials_serials.id FROM serials_post JOIN serials_serials ON serials_serials.name = serials_post.name"):
    serial = conn_OLD.execute("SELECT * FROM serials_serials WHERE serials_serials.name = ?",[row[2],]).fetchone()
    if conn_NEW.execute("SELECT count(*) FROM serials_serial WHERE title_en = ?", [row[1],]).fetchone()[0] == 0:
        print(serial[0])
        conn_NEW.execute("INSERT INTO serials_serial(id, title_en, title_cz,title_sk, popis, image, start_yr, end_yr, delka) VALUES(?,?,?,?,?,?,?,?,?)",[serial[0], serial[2], serial[7],"",serial[3], serial[6],serial[8],serial[9],serial[10]])
    conn_NEW.execute("INSERT INTO serials_epizoda(cislo_serie, cislo_epizoda, popis_epizody, url1, url1_cc, created_date, epizoda_serial_id) VALUES(?,?,?,?,?,?,?)",[row[3], row[4], row[7], row[5], row[6], row[11], serial[0]])
conn_NEW.commit()
conn_NEW.close()


