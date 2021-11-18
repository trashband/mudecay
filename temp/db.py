import sqlite3
import func



conn = sqlite3.connect('database.db')


def insertEvent():
    query = ('INSERT INTO event_timer (time,FullName,name, img) '
            'VALUES (:time, :FullName, :name, :img);')

    i = 0
    while i <= len(func.event):
        i += 1
        if (i<= 42):
            params = {
                'time': func.event[i]['time'],
                'FullName': func.event[i]['FullName'],
                'name': func.event[i]['name'],
                'img': func.event[i]['img'],
                }
            conn.execute(query, params)
        print(i)
    conn.commit()
    conn.close()

insertEvent()