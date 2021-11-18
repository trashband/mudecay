import sqlite3
conn = sqlite3.connect('database.db', check_same_thread=False)

# Добавление персонажа
def add_char1(id, slot, race, lvl, reset):
	query = ('INSERT INTO party (id_telegram,slot_1,race,lvl,reset) '
			'VALUES (:id_telegram, :slot_1, :race, :lvl, :reset);')
	params = {
		'id_telegram': id,
		'slot_1': slot,
		'race': race,
		'lvl' : lvl,
		'reset' : reset

	}
	conn.execute(query, params)
	conn.commit()
	print('Персонаж добавлен')

# Получение ника чара персонажа
def char_name(id):
	cursor = conn.execute("SELECT * FROM party")
	for i in cursor:
		if i[1] == id:
			return i
def char_name1(id):
	cursor = conn.execute("SELECT * FROM party")
	arr = []
	for i in cursor:
		if i[1] == id:
			arr.append(i)
	return arr

# Список персонажей
def char_list():
	user_char = []
	cursor = conn.execute("SELECT * FROM party")
	j=0
	for i in cursor:
		j+=1
		user_char.append(i)
	return user_char

# UPDATE стату 400 лвл
def upd_flag(char, flag):
    data = (flag, char)

    sql_update = ''' UPDATE party 
    SET notice_send=?
    WHERE slot_1=?
    '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql_update, data)
        conn.commit()
    except Exception as e:
        print(e)
    finally: 
        print('Статус персонажа изменен на ' + str(flag))	

# Delete char by ID
def delete_char(id, user_id):
    data = (id, user_id)

    sql_update = ''' DELETE FROM party
    WHERE id=? and id_telegram=?
    '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql_update, data)
        conn.commit()
    except Exception as e:
        print(e)