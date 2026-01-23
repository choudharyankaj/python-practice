x = 10  # Global variable

def local_scope():
    x = 5  # Local variable
    print("Local x inside function:", x)

def global_scope():
    global x
    x = 20  # Modify global variable
    print("Global x modified inside function:", x)

def nonlocal_scope():
    y = 10
    def inner():
        nonlocal y
        y += 5
        print("Inner y:", y)
    inner()
    print("Outer y after inner:", y)

# Function calls
local_scope()
print("Global x outside function:", x)
global_scope()
print("Global x outside function:", x)
nonlocal_scope()
