import sqlite3
conn = sqlite3.connect('database.db', check_same_thread=False)

# Получение данных персонажа
def user_data(id):
	user_data = []
	cursor = conn.execute("SELECT * FROM user")
	for i in cursor:
		if i[1] == id:
			user_data.append(i)
			return user_data



# Проверка пользователя в бд
def check_user(id):
	cursor = conn.execute("SELECT * FROM user")
	for i in cursor:
		if i[1] == id:
			print('Пользователь уже существует')
			return True

# Проверка чаров персонажа
def user_characters(id):
	user_char = []
	cursor = conn.execute("SELECT * FROM party")
	j=0
	for i in cursor:
		j+=1
		if (i[1] == id) and (user_data(id)[0][3] == 1):
			user_char.append(i)
	return user_char

# Добавление пользователя в бд
def add_user(id, name):
	if check_user(id) != True:
		query = ('INSERT INTO user (id_telegram,name_telegram,notice,vip_status) '
				'VALUES (:id_telegram, :name_telegram, :notice, :vip_status);')
		params = {
			'id_telegram': id,
			'name_telegram': name,
			'notice': 1,
			'vip_status' : 0
		}
		conn.execute(query, params)
		conn.commit()
		print('Пользователь добавлен в базу')

def notics_stat(id_telegram, notice):
	query = conn.execute("UPDATE user set notice = %s where id_telegram = %s" %(notice, id_telegram))
	conn.commit()

