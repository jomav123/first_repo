def user():
    name = input('tape your name: ')
    id_number = int(input("tape your id: "))
    email = input("tape your email address: username@gmail.com")
    address = input("where do you live?")
    print(f"welcome {name}{id_number}")
    print(f"{email} is your email address: ")
    print(name,' lives at ', address)


user()
