while True:
    try:
        val = int(input("Enter Number: "))
        break
    except ValueError:
        print("Numbers Only")
