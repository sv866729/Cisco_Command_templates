# Prompt the user to enter the outside network
outsideNet = input("Enter the outside network (e.g. 203.0.113.0): ")

# Use the outside network variable in the route command
print(f"""route outside 0.0.0.0 0.0.0.0 {outsideNet}""")
