# Write your code here!

def employee_print(employee_info):
    name = employee_info.get("Name", "N/A")
    salary = employee_info.get("Salary", "N/A")
    role = employee_info.get("Role", "N/A")


    print(f"""Name: {name}
    Salary: {salary}
    Role: {role}""")
    
    other = employee_info.copy()
    for key in ["Name", "Salary", "Role"]:
        if key in other:
            other.pop(key)
        
    if not other:
        print("'No other info!'")
    else:
        for key, value in other.items():
            print(f"{key}: {value}")

employee_info = {}
employee_print(employee_info)