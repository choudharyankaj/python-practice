x = 50  # Global

def local_test():
    x = 10  # Local
    print("Local x inside function:", x)

def global_test():
    global x
    x = 100
    print("Global x changed inside function:", x)

def nonlocal_test():
    y = 20
    def inner():
        nonlocal y
        y += 10
        print("Inner y (nonlocal):", y)
    inner()
    print("Outer y after inner:", y)

local_test()
print("Global x outside function:", x)
global_test()
print("Global x outside function:", x)
nonlocal_test()
