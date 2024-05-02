import psycopg2
import csv

# Функция подключения к базе данных PostgreSQL
def connect_to_database():
    try:
        conn = psycopg2.connect(
            dbname="databaseforlabs",
            user="postgres",
            password="123",
            host="localhost",
            port="5432"
        )
        return conn
    except psycopg2.Error as e:
        print("Ошибка при подключении к базе данных:", e)
        return None

# Функция вставки данных в таблицу PHONEBOOK из CSV файла
def insert_from_csv(filename):
    try:
        conn = connect_to_database()
        if conn:
            cur = conn.cursor()
            with open(filename, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                header = next(reader, None)  # Пропуск заголовка
                if header is not None:  # Проверка наличия строк в файле
                    for row in reader:
                        cur.execute("""
                        INSERT INTO PHONEBOOK (HUMAN_ID, HUMAN_NAME, HUMAN_LAST_NAME, PHONENUMBER, ATRIBUTES) 
                        VALUES (%s, %s, %s, %s, %s);
                        """, row)
                    conn.commit()
                    conn.close()
                    print("Данные успешно добавлены из файла", filename)
                else:
                    print("Файл пустой.")
    except psycopg2.Error as e:
        print("Ошибка при добавлении данных из файла:", e)

# Функция вставки данных в таблицу PHONEBOOK через консоль
def insert_from_console():
    try:
        conn = connect_to_database()
        if conn:
            cur = conn.cursor()
            print("Введите данные нового контакта:")
            human_id = int(input("ID: "))
            human_name = input("Имя: ")
            human_last_name = input("Фамилия: ")
            phone_number = int(input("Номер телефона: "))
            attributes = input("Атрибуты: ")
            cur.execute("""
            INSERT INTO PHONEBOOK (HUMAN_ID, HUMAN_NAME, HUMAN_LAST_NAME, PHONENUMBER, ATRIBUTES) 
            VALUES (%s, %s, %s, %s, %s);
            """, (human_id, human_name, human_last_name, phone_number, attributes))
            conn.commit()
            conn.close()
            print("Данные успешно добавлены.")
    except psycopg2.Error as e:
        print("Ошибка при добавлении данных через консоль:", e)

# Функция обновления данных в таблице PHONEBOOK

# Функция запроса данных из таблицы PHONEBOOK с различными фильтрами
def query_data(filter_name=None, filter_phone=None):
    try:
        conn = connect_to_database()
        if conn:
            cur = conn.cursor()
            if filter_name and filter_phone:
                cur.execute("SELECT * FROM PHONEBOOK WHERE HUMAN_NAME = %s AND PHONENUMBER = %s;", (filter_name, filter_phone))
            elif filter_name:
                cur.execute("SELECT * FROM PHONEBOOK WHERE HUMAN_NAME = %s;", (filter_name,))
            elif filter_phone:
                cur.execute("SELECT * FROM PHONEBOOK WHERE PHONENUMBER = %s;", (filter_phone,))
            else:
                cur.execute("SELECT * FROM PHONEBOOK;")
            rows = cur.fetchall()
            for row in rows:
                print(row)
            conn.close()
    except psycopg2.Error as e:
        print("Ошибка при запросе данных:", e)

# Функция удаления данных из таблицы PHONEBOOK по имени пользователя или номеру телефона

# Вызов функции вставки данных из CSV файла
insert_from_csv('C:/Users/Админ/Desktop/pp2/pp2_22B031119-1/TSIS10/phonebook_data.csv')

# Вызов функции вставки данных через консоль
insert_from_console()
