from models import UniService
from pprint import pprint

data = "dbname=uni user=mohammadi password=shir8844 host=localhost port=5432"

service = UniService(data)
service.create_tables()

def menu():
    print("\n Welcome! Here are your options:")
    print("1. Create tables")
    print("2. Add email column to student")
    print("3. Show all students")
    print("4. Show all majors")
    print("5. Show students ordered by age (oldest to youngest)")
    print("6. Count students per major")
    print("7. Show majors with more than 3 students")
    print("8. Make major title column NOT NULL")
    print("9. Set default value for master field")
    print("10. Show oldest and youngest student (UNION)")
    print("11. Count majors per master")
    print("12. Remove relation between major and department")
    print("13. Create index on master name")
    print("14. Show students with their majors")
    print("15. Show masters, departments, and majors")
    print("16. Show majors each student is enrolled in")
    print("17. Show major with the most students")
    print("18. Show department offering the most majors")
    print("19. Show student name, major title, and master name")
    print("0. Exit")

    choice = input("\nEnter your choice: ")
    return choice


while True:
    user_choice = menu()

    try:
        if user_choice == "1":
            service.create_tables()
        elif user_choice == "2":
            service.add_email()
        elif user_choice == "3":
            pprint(service.list("student"))
        elif user_choice == "4":
            pprint(service.list_majors())
        elif user_choice == "5":
            pprint(service.list_students_by_age())
        elif user_choice == "6":
            pprint(service.count_students_per_major())
        elif user_choice == "7":
            pprint(service.majors_with_more_than_3_students())
        elif user_choice == "8":
            service.make_major_title_not_null()
            print("Done")
        elif user_choice == "9":
            service.set_default_master_field()
            print("Done")
        elif user_choice == "10":
            pprint(service.oldest_and_youngest_student_union())
        elif user_choice == "11":
            pprint(service.count_majors_per_master())
        elif user_choice == "12":
            service.remove_major_department_relation()
            print("Done")
        elif user_choice == "13":
            service.create_index_on_master_name()
            print("Done")
        elif user_choice == "14":
            pprint(service.list_students_with_majors())
        elif user_choice == "15":
            pprint(service.list_master_department_major())
        elif user_choice == "16":
            pprint(service.list_majors_per_student())
        elif user_choice == "17":
            pprint(service.major_with_most_students())
        elif user_choice == "18":
            pprint(service.department_with_most_majors())
        elif user_choice == "19":
            pprint(service.list_student_major_master())
        elif user_choice == "0":
            print("Goodbye")
            break
        else:
            print("not valid choice. Please try again.")
    except Exception as e:
        print(f"error: {e}")
