def line(deli):
    if len(deli) == 0:
        print("The line is currently empty.")
    else:
        queue = "The line is currently:"
        for i, customer in enumerate(deli, start=1):
            queue += f" {i}. {customer}"
        print(queue)

def take_a_number(katz_deli, name):
    katz_deli.append(name)
    position = len(katz_deli)
    print(f"Welcome, {name}. You are number {position} in line.")

def now_serving(deli):
    if len(deli) == 0:
        print("There is nobody waiting to be served!")
    else:
        customer = deli.pop(0)
        print(f"Currently serving {customer}.")