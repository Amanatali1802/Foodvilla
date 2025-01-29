import mysql.connector
import pickle
import csv
import os
import sys

def main_menu():
    print("WELCOME TO FOODVILLA")
    print("Thanks for visiting our service!")
    print("""
    Our Terms and Conditions:
    1. We will deliver your order in 30 mins.
    2. Track your delivery guy with live location mapping.
    3. You can call him for updates.
    4. Visit our website: http://www.foodvilla.com
    5. You can order only one item at a time.
    6. For more details, contact us:
        Phone: 3344578
        Call: +91 9456790000
        Email: foodvilla@gmail.com
    """)
    print("PROJECT FOODVILLA")

    while True:
        print("\nMENU")
        print("1. Connectivity (Database Management)")
        print("2. Binary File Handling")
        print("3. CSV File Handling")
        print("4. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            connectivity()
        elif choice == 2:
            binary_menu()
        elif choice == 3:
            csv_menu()
        elif choice == 4:
            print("Thank you for your precious time!")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")


# ---------------- Database Management ----------------
def connectivity():
    def create_database():
        try:
            db = mysql.connector.connect(host="localhost", user="root", passwd="Password")
            cursor = db.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS FOODVILLA")
            print("Database Created or Already Exists")
            db.close()
        except Exception as e:
            print("Error:", e)

    def create_table():
        try:
            db = mysql.connector.connect(host="localhost", user="root", passwd="Password", database="FOODVILLA")
            cursor = db.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS MENU (
                    meal VARCHAR(50),
                    villa_number INT
                )
            """)
            print("Table Created")
            db.close()
        except Exception as e:
            print("Error:", e)

    def insert_data_dynamically():
        try:
            db = mysql.connector.connect(host="localhost", user="root", passwd="Password", database="FOODVILLA")
            cursor = db.cursor()

            while True:
                meal = input("Enter meal name (or type 'exit' to stop): ").strip()
                if meal.lower() == "exit":
                    break

                villa_number = input("Enter villa number: ").strip()
                if not villa_number.isdigit():
                    print("Invalid villa number. Please enter a valid number.")
                    continue

                cursor.execute("INSERT INTO MENU (meal, villa_number) VALUES (%s, %s)", (meal, int(villa_number)))
                db.commit()
                print("Data inserted successfully!")

            db.close()
        except Exception as e:
            print("Error:", e)

    def select_data():
        try:
            db = mysql.connector.connect(host="localhost", user="root", passwd="Password", database="FOODVILLA")
            cursor = db.cursor()
            cursor.execute("SELECT * FROM MENU")
            for row in cursor.fetchall():
                print(row)
            db.close()
        except Exception as e:
            print("Error:", e)

    while True:
        print("\nDatabase Menu")
        print("1. Create Database")
        print("2. Create Table")
        print("3. Insert Data Dynamically")
        print("4. Display Data")
        print("5. Back to Main Menu")
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                create_database()
            elif choice == 2:
                create_table()
            elif choice == 3:
                insert_data_dynamically()
            elif choice == 4:
                select_data()
            elif choice == 5:
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a valid number.")


# ---------------- Binary File Handling ----------------
def binary_menu():
    def write():
        with open("food.dat", "ab") as file:
            data = {
                "name": input("Enter your name: "),
                "address": input("Enter your address: "),
                "phone_number": input("Enter your phone number: ")
            }
            pickle.dump(data, file)
            print("Data Written Successfully")

    def display():
        try:
            with open("food.dat", "rb") as file:
                while True:
                    print(pickle.load(file))
        except EOFError:
            pass

    def update():
        name_to_update = input("Enter the name to update: ")
        updated_data = []
        with open("food.dat", "rb") as file:
            try:
                while True:
                    data = pickle.load(file)
                    if data["name"] == name_to_update:
                        print("1. Update Name\n2. Update Address\n3. Update Phone Number\n4. Exit")
                        choice = int(input("Enter your choice: "))
                        if choice == 1:
                            data["name"] = input("Enter new name: ")
                        elif choice == 2:
                            data["address"] = input("Enter new address: ")
                        elif choice == 3:
                            data["phone_number"] = input("Enter new phone number: ")
                        elif choice == 4:
                            break
                        else:
                            print("Invalid choice. Returning to update menu.")
                    updated_data.append(data)
            except EOFError:
                pass

        with open("food.dat", "wb") as file:
            for item in updated_data:
                pickle.dump(item, file)
        print("Data Updated Successfully")

    def delete():
        name_to_delete = input("Enter the name to delete: ")
        updated_data = []
        with open("food.dat", "rb") as file:
            try:
                while True:
                    data = pickle.load(file)
                    if data["name"] != name_to_delete:
                        updated_data.append(data)
            except EOFError:
                pass

        with open("food.dat", "wb") as file:
            for item in updated_data:
                pickle.dump(item, file)
        print("Data Deleted Successfully")

    while True:
        print("\nBinary File Menu")
        print("1. Write")
        print("2. Display")
        print("3. Update")
        print("4. Delete")
        print("5. Back to Main Menu")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            write()
        elif choice == 2:
            display()
        elif choice == 3:
            update()
        elif choice == 4:
            delete()
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please try again.")


# ---------------- CSV File Handling ----------------
def csv_menu():
    def write():
        with open("foodvilla.csv", "a", newline="") as file:
            writer = csv.writer(file)
            name = input("Enter your name: ")
            age = int(input("Enter your age: "))
            phone = input("Enter your phone number: ")
            if len(phone) == 10:
                writer.writerow([name, age, phone])
                print("Data Written Successfully")
            else:
                print("Invalid phone number. Please try again.")

    def display():
        with open("foodvilla.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)

    def update():
        name_to_update = input("Enter the name to update: ")
        updated_rows = []
        with open("foodvilla.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row and row[0] == name_to_update:
                    print("1. Update Name\n2. Update Age\n3. Update Phone Number")
                    choice = int(input("Enter your choice: "))
                    if choice == 1:
                        row[0] = input("Enter new name: ")
                    elif choice == 2:
                        row[1] = input("Enter new age: ")
                    elif choice == 3:
                        row[2] = input("Enter new phone number: ")
                updated_rows.append(row)

        with open("foodvilla.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(updated_rows)
        print("Data Updated Successfully")

    def delete():
        name_to_delete = input("Enter the name to delete: ")
        updated_rows = []
        with open("foodvilla.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row and row[0] != name_to_delete:
                    updated_rows.append(row)

        with open("foodvilla.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(updated_rows)
        print("Data Deleted Successfully")

    while True:
        print("\nCSV File Menu")
        print("1. Write")
        print("2. Display")
        print("3. Update")
        print("4. Delete")
        print("5. Back to Main Menu")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            write()
        elif choice == 2:
            display()
        elif choice == 3:
            update()
        elif choice == 4:
            delete()
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please try again.")


# Run the program
if __name__ == "__main__":
    main_menu()
