from task03 import clac_dragon_heads


def main():
    age = int(input("Dragon age: "))
    head = clac_dragon_heads(age)
    msq = f"Dragon with {age} hears has {head} heads."
    print(msq)


if __name__ == "__main__":
    main()
