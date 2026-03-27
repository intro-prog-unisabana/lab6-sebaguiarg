# Write your code here!

def employee_print(employee_info):
    name = employee_info.get("name", "N/A")
    salary = employee_info.get("salary", "N/A")
    role = employee_info.get("role", "N/A")


    print(f"""Name: {name}
        Salary: {salary}
        Role: {role}""")
    
    other = employee_info.copy()
    for key in ["name", "salary", "role"]:
        if key in other:
            other.pop(key)
        
    if not other:
        print("No other info!")
    else:
        for key, value in other.items():
            print(f"{key}, {value}")

employee_info = {}
employee_print(employee_info)