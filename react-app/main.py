import mysql.connector


def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",          # Unga MySQL username (default: root)
        password="admin123",  # Unga MySQL password-ah inge podunga
        database="student_db"
    )


def add_student():
    name = input("Enter Name: ")
    roll_no = input("Enter Roll No: ")
    dept = input("Enter Department: ")
    email = input("Enter Email: ")
    phone = input("Enter Phone: ")

    try:
        db = connect_db()
        cursor = db.cursor()
        query = "INSERT INTO students (name, roll_no, department, email, phone) VALUES (%s, %s, %s, %s, %s)"
        values = (name, roll_no, dept, email, phone)
        
        cursor.execute(query, values)
        db.commit()
        print("\n✅ Student added successfully!\n")
    except Exception as e:
        print(f"\n❌ Error: {e}\n")
    finally:
        db.close()
# Student விவரங்களை அப்டேட் செய்ய (Update)
def update_student():
    roll_no = input("Enter Roll No of the student to update: ")
    new_email = input("Enter New Email: ")
    new_phone = input("Enter New Phone: ")

    try:
        db = connect_db()
        cursor = db.cursor()
        query = "UPDATE students SET email = %s, phone = %s WHERE roll_no = %s"
        cursor.execute(query, (new_email, new_phone, roll_no))
        db.commit()
        if cursor.rowcount > 0:
            print("\n✅ Student updated successfully!\n")
        else:
            print("\n⚠️ Roll No not found!\n")
    except Exception as e:
        print(f"\n❌ Error: {e}\n")
    finally:
        db.close()   

def delete_student():
    roll_no = input("Enter Roll No of the student to delete: ")

    try:
        db = connect_db()
        cursor = db.cursor()
        query = "DELETE FROM students WHERE roll_no = %s"
        cursor.execute(query, (roll_no,))
        db.commit()
        if cursor.rowcount > 0:
            print("\n✅ Student record deleted successfully!\n")
        else:
            print("\n⚠️ Roll No not found!\n")
    except Exception as e:
        print(f"\n❌ Error: {e}\n")
    finally:
        db.close()     

def view_students():
    try:
        db = connect_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM students")
        records = cursor.fetchall()

        print("\n--- Student Records ---")
        if not records:
            print("No student records found.")
        else:
            for row in records:
                print(f"ID: {row[0]} | Name: {row[1]} | Roll No: {row[2]} | Dept: {row[3]} | Email: {row[4]} | Phone: {row[5]}")
        print("-----------------------\n")
    except Exception as e:
        print(f"\n❌ Error: {e}\n")
    finally:
        db.close()


def main():
    while True:
        print("=== Student Management System ===")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Exit")
        print("4. Delete")
        print("5. Update")
        choice = input("Enter your choice : ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            print("Exiting Program. Good Luck!")
            break
        else:
            print("Invalid choice, try again.\n")

if __name__ == "__main__":
    main()  