import sqlite3
conn = sqlite3.connect('database.db', check_same_thread=False)

# Добавление вопроса в бд
def push_to_base(id, answer):
	query = ('INSERT INTO answer (id_telegram,comment) '
			'VALUES (:id_telegram, :comment);')
	params = {
		'id_telegram': id,
		'comment': answer
	}
	conn.execute(query, params)
	conn.commit()
	print('Заgись добавленна')