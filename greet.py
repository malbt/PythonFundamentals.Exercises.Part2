def greet(name: str) -> None:
    print("hello " + name)
    print("Hi" + name)


def name_input() -> str:
    return input("Please enter your name:\n")


name = name_input()
greet(name)
