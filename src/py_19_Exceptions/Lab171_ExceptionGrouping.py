eg = ExceptionGroup("Exception Multiple",[
    ValueError("ValueError"),
    TypeError("TypeError"),
    ZeroDivisionError("ZeroDivisionError")
])

def check_division(a):
    if a==0:
        raise eg

print(eg)