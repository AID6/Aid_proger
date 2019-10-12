import sqlite3
import datetime
conn = sqlite3.connect('data.db')
c = conn.cursor()
c.execute("SELECT * FROM tab_veg WHERE veg == 'Картофель'")
data = c.fetchall()
print(data)
'''
c.execute("SELECT * FROM tab_veg WHERE veg == 'Чилли'")
data = c.fetchall()
print(data)
'''
'''
c.execute("INSERT INTO tab_veg "
          "(process, state, time_min, time_max, veg)"
          " VALUES ('СВЧ-печь', 'Целиком', 4, 5, 'Шпинат')")
conn.commit()
print(datetime.datetime.now())
'''
'''
c.execute("UPDATE tab_veg SET state = 'Початок'  WHERE process == 'СВЧ-печь' and veg == 'Кукуруза свежая'")
conn.commit()
'''
'''
c.execute("CREATE TABLE IF NOT EXISTS tab_veg (id INTEGER PRIMARY KEY AUTOINCREMENT, veg varchar, process varchar, state varchar, time_min integer, time_max integer, state_process varchar)")
conn.commit()
'''
'''
c.execute("INSERT INTO tab_veg "
          "(process, state, time_min, time_max, veg)"
          " VALUES ('Жарение во фритюре', 'Целиком', 60, 60, 'Артишок')")
conn.commit()
'''
'''
c.execute("INSERT INTO tab_meet_finish(meet, process, part, mass_4_min, mass_4_max, time_4_min, time_4_max) SELECT meet, process, part, mass_4_min, mass_4_max, time_4_min, time_4_max FROM tab_meet_baking")
conn.commit()
'''
'''
c.execute("DROP TABLE tab_veg")
conn.commit()
'''
'''
c.execute("CREATE TABLE IF NOT EXISTS tab_meet_finish (id INTEGER PRIMARY KEY AUTOINCREMENT, meet varchar, process varchar, part varchar, mass_4_min integer, mass_4_max integer, time_4_min integer, time_4_max integer)")
conn.commit()
'''
'''
c.execute("INSERT INTO tab_meet_cooking "
          "(part, mass_4_min, mass_4_max, time_4_min, time_4_max, meet, process)"
          " VALUES ('Поперечное сечение', 1200, 1400, 150, 180, 'Говядина', 'Варка')")
conn.commit()
'''
'''
c.execute("SELECT part FROM tab_meet_cooking WHERE meet == ? ",('Говядина',))
data = c.fetchall()
print(data)
'''
'''
c.execute("DELETE FROM tab_meet_cooking WHERE id == 5")
conn.commit()
'''
c.close()
conn.close()
'''
c.execute("INSERT INTO tab_meet "
          "(meet)"
          " VALUES ('Ягнятина')")
conn.commit()
c.execute("CREATE TABLE IF NOT EXISTS tab_meet (id INTEGER PRIMARY KEY AUTOINCREMENT, meet varchar )")
conn.commit()
c.execute("INSERT INTO tab_meet "
          "(part, mass_4_min, mass_4_max, time_4_min, time_4_max, meet, process)"
          " VALUES ('Отбивная с рёбер', 150, 180, 5, 7, 'Ягнятина', 'Варка')")
conn.commit()
c.execute("UPDATE tab_meet SET part = 'Ножки (маринованные)'  WHERE mass_4_max == 2000")
conn.commit()
c.execute("SELECT meet, part FROM tab_meet WHERE part == 'Ножки (маринованные)' and meet == 'Свинина'")
row = c.fetchone()
print(row)
INSERT INTO tab_1 (product, servings_min, servings_max, process, time_process_min, time_process_max) VALUES ('Поперечные',350,380,'Варка',38,45)
c.execute("SELECT product, process FROM tab_1 WHERE servings_max == 350")
row = c.fetchone()
c.execute("CREATE TABLE IF NOT EXISTS tab_1 (id INTEGER PRIMARY KEY AUTOINCREMENT, product varchar, process varchar, state varchar, time_min integer, time_max integer)")
conn.commit()
c.execute("CREATE TABLE IF NOT EXISTS tab_meet_1 (id INTEGER PRIMARY KEY AUTOINCREMENT, meet varchar, part varchar, process varchar, coefficient float)")
conn.commit()
import sqlite3
conn = sqlite3.connect('data.db')
c = conn.cursor()
c.execute("INSERT INTO tab_meet_1 (meet, part, process, coefficient) VALUES ('Ягнятина', 'Язык', 'Варка', 13.155)")
conn.commit()
c.execute("SELECT meet, part, process, coefficient FROM tab_meet_1 WHERE part == 'Язык' and meet == 'Ягнятина'")
row = c.fetchone()
print(row)
c.close()
conn.close()
c.execute("SELECT part, mass_4_min, mass_4_max, time_4_min, time_4_max, meet, process FROM tab_meet WHERE part == 'Лопатка'")
row = c.fetchone()
print(row)
'''