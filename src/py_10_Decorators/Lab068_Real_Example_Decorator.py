import time     #time library is imported


def read_logs(func):

    def wrapper():
        print("Before adding the function1 logs\n ")
        func()
        print("After adding the function1 logs")
    return wrapper


def read_seconds(func):
    def wrapper():
        start_time = time.time()
        print(f"Start reading the seconds :\n {start_time}\n")
        func()
        end_time= time.time()
        print(f"Stop reading the seconds :\n {end_time}\n")
    return wrapper



@read_seconds
@read_logs
def ui_function1():
    print("Add a function1, this will take time \n")
    time.sleep(2)


@read_seconds
@read_logs
def ui_function2():
    print("Add a function2, this will take time")
    time.sleep(5)



ui_function1()
ui_function2()