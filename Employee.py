class Employee:

    def __init__(self):
        print("The Employee has been created.")

    def __del__(self):
        print("Employee has been destructed.")

def Create_obj():
    print("Making object....")
    obj = Employee()
    print("Function has ended...")
    return obj

print("Calling the object...")
obj = Create_obj()
print("The program has ended...")



    