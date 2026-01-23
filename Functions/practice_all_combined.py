def introduce(name="Guest", *hobbies, **info):
    print(f"Hello, my name is {name}.")
    if hobbies:
        print("My hobbies are:", ", ".join(hobbies))
    if info:
        print("Additional info:")
        for key, value in info.items():
            print(f"{key}: {value}")

introduce("Ankaj", "Reading", "Coding", age=36, city="Chandigarh")
introduce()
