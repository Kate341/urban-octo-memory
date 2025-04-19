import psycopg2
import csv

#connect to database
def connect():
    return psycopg2.connect(
        host="localhost",
        port=5433,
        dbname="phonebook1",
        user="postgres",
        password="1111"
    )

def insert_or_update_user(name, phone):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM phonebook WHERE name = %s", (name,))
            existing = cur.fetchone()
            if existing:
                cur.execute("UPDATE phonebook SET phone = %s WHERE name = %s", (phone, name))
                print("User updated.")
            else:
                cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name, phone))
                print("User inserted.")

#insert from console
def insert_from_console():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    insert_or_update_user(name, phone)

#insert from csv
def insert_from_csv(path):
    with connect() as conn:
        with conn.cursor() as cur:
            with open(path, 'r') as f:
                reader = csv.reader(f)
                for row in reader:
                    insert_or_update_user(row[0], row[1])
    print("CSV imported!")

#update user
def update_user(name, new_phone):
    insert_or_update_user(name, new_phone)

#query by pattern
def query_by_pattern(pattern):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM phonebook WHERE name ILIKE %s OR phone ILIKE %s", (f"%{pattern}%", f"%{pattern}%"))
            for row in cur.fetchall():
                print(row)

#query with pagination
def query_with_pagination(limit, offset):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM phonebook LIMIT %s OFFSET %s", (limit, offset))
            for row in cur.fetchall():
                print(row)

#delete user
def delete_user_by_name_or_phone(name_or_phone):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM phonebook WHERE name = %s OR phone = %s", (name_or_phone, name_or_phone))
    print(f"Deleted records with name or phone: {name_or_phone}")

#main menu
def menu():
    while True:
        print("\n1. Insert (console)")
        print("2. Insert (CSV)")
        print("3. Update user")
        print("4. View all by pattern")
        print("5. View with pagination")
        print("6. Delete user")
        print("7. Exit")

        choice = input("Choose: ")

        if choice == '1':
            insert_from_console()
        elif choice == '2':
            insert_from_csv(input("Enter CSV path: "))
        elif choice == '3':
            update_user(input("Name to update: "), input("New phone: "))
        elif choice == '4':
            query_by_pattern(input("Pattern to search: "))
        elif choice == '5':
            limit = int(input("Limit: "))
            offset = int(input("Offset: "))
            query_with_pagination(limit, offset)
        elif choice == '6':
            delete_user_by_name_or_phone(input("Name or phone to delete: "))
        elif choice == '7':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    menu()