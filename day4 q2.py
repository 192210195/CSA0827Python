def calculate_non_teaching_staff(staff_users):
    return staff_users // 3

def main():
    student_users = int(input("Enter the number of student users: "))

    total_users = int(input("Enter the total number of users: "))

    staff_users = int(input("Enter the number of staff users: "))

    non_teaching_staff_users = calculate_non_teaching_staff(staff_users)


    print("Number of student users:", student_users)
    print("Total users:", total_users)
    print("Number of staff users:", staff_users)
    print("Number of non-teaching staff users:", non_teaching_staff_users)

if __name__ == "__main__":
    main()
