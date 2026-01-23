def display_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

display_info(name="Ankaj", age=36, city="Chandigarh")
display_info(product="Laptop", price=75000)