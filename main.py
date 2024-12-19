import mysql.connector
from mysql.connector import Error

# MySQL connection configuration
def create_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",        # Change if you use a remote server
            user="root",             # MySQL username, usually 'root' or your own user
            password="password",     # MySQL password
            database="student_attendance"  # Ensure this database exists
        )
        if connection.is_connected():
            print("Connected to MySQL database")
            return connection
    except Error as e:
        print(f"Error: '{e}'")
        return None


def register_student():
    """Register a new student in the database."""
    connection = create_connection()
    if connection.is_connected():
        try:
            print("hello")
            student_id = int(input("Enter student ID: "))
            student_name = input("Enter student name: ")
            student_email = input("Enter student email: ")

            cursor = connection.cursor()
            query = "INSERT INTO students (student_id, student_name, student_email) VALUES (%s, %s, %s)"
            cursor.execute(query, (student_id, student_name, student_email))
            connection.commit()
            print(f"Student {student_name} registered successfully!")
        except Error as e:
            print(f"Error: '{e}'")
        finally:
            cursor.close()
            connection.close()

def add_course():
    """Add a new course to the database."""
    connection = create_connection()
    if connection:
        try:
            course_id = int(input("Enter course ID: "))
            course_name = input("Enter course name: ")

            cursor = connection.cursor()
            query = "INSERT INTO courses (course_id, course_name) VALUES (%s, %s)"
            cursor.execute(query, (course_id, course_name))
            connection.commit()
            print(f"Course {course_name} added successfully!")
        except Error as e:
            print(f"Error: '{e}'")
        finally:
            cursor.close()
            connection.close()

def add_class():
    """Add a class to a course in the database."""
    connection = create_connection()
    if connection:
        try:
            class_id = int(input("Enter class ID: "))
            course_id = int(input("Enter course ID: "))
            class_date = input("Enter class date (YYYY-MM-DD): ")

            cursor = connection.cursor()
            query = "INSERT INTO classes (class_id, course_id, class_date) VALUES (%s, %s, %s)"
            cursor.execute(query, (class_id, course_id, class_date))
            connection.commit()
            print(f"Class on {class_date} added successfully!")
        except Error as e:
            print(f"Error: '{e}'")
        finally:
            cursor.close()
            connection.close()

def record_attendance():
    """Record attendance for a class in the database."""
    connection = create_connection()
    if connection:
        try:
            class_id = int(input("Enter class ID: "))
            student_id = int(input("Enter student ID: "))
            status = input("Enter attendance status (present/absent): ").lower()

            cursor = connection.cursor()
            query = "INSERT INTO attendance (student_id, class_id, status) VALUES (%s, %s, %s)"
            cursor.execute(query, (student_id, class_id, status))
            connection.commit()
            print("Attendance recorded successfully!")
        except Error as e:
            print(f"Error: '{e}'")
        finally:
            cursor.close()
            connection.close()

def view_attendance():
    """View attendance for a class from the database."""
    connection = create_connection()
    if connection:
        try:
            class_id = int(input("Enter class ID to view attendance: "))
            cursor = connection.cursor()
            query = "SELECT student_id, status FROM attendance WHERE class_id = %s"
            cursor.execute(query, (class_id,))
            rows = cursor.fetchall()

            if rows:
                for row in rows:
                    print(f"Student ID: {row[0]}, Status: {row[1]}")
            else:
                print("No attendance records found.")
        except Error as e:
            print(f"Error: '{e}'")
        finally:
            cursor.close()
            connection.close()

def main_menu():
    """Main menu for the Student Attendance System."""
    print("\nStudent Attendance System (Using MySQL)")
    print("1. Register Student")
    print("2. Add Course")
    print("3. Add Class")
    print("4. Record Attendance")
    print("5. View Attendance")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        register_student()
    elif choice == '2':
        add_course()
    elif choice == '3':
        add_class()
    elif choice == '4':
        record_attendance()
    elif choice == '5':
        view_attendance()
    elif choice == '6':
        print("Exiting the system...")
        exit()
    else:
        print("Invalid choice! Please try again.")

if __name__ == '__main__':
    while True:
        main_menu()
