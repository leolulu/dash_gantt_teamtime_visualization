import sqlite3


def sqllite_operator(sql, param=None):
    conn = sqlite3.connect('db.db')
    cur = conn.cursor()
    if param is None:
        cur.execute(sql)
    else:
        cur.execute(sql, param)
    print(sql, "result:", cur.rowcount)
    conn.commit()
    cur.close()
    conn.close()


def sqllite_selector(sql, param=None):
    conn = sqlite3.connect('db.db')
    cur = conn.cursor()
    if param is None:
        cur.execute(sql)
    else:
        cur.execute(sql, param)
    result = cur.fetchall()
    cur.close()
    conn.close()
    return result

if __name__ == "__main__":
    print(sqllite_selector('PRAGMA table_info(result_log)'))