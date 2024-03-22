def calculate_bonus(salary, grade):
    bonus = 0
    
    if grade == 'A':
        bonus = 0.05 * salary
    elif grade == 'B':
        bonus = 0.10 * salary
    
    if salary < 10000:
        bonus += 0.02 * salary
    
    return bonus

def calculate_total_salary(salary, bonus):
    return salary + bonus

def main():
    salary = float(input("Enter the salary of the employee: "))
    grade = input("Enter the grade of the employee (A or B): ").upper()
    
    bonus = calculate_bonus(salary, grade)
    total_salary = calculate_total_salary(salary, bonus)
    
    print("Bonus: ${:.2f}".format(bonus))
    print("Total Salary: ${:.2f}".format(total_salary))

if __name__ == "__main__":
    main()
