class employee:
    def __init__(self):
        print('Employee created')#3
    def __del__(self):
            print("Destructor called")#6
def create_odj():
    print("Making Object ...")#2
    obj = employee()
    print("function end ...")#4
    return obj
print("call ctreate_obj() function...")#1
obj = create_odj()
print("Program end...")#5