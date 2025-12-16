Emergency_Brake = False

while Emergency_Brake == False:
    a= input("Enter Password: ")
    if a == "stop":
        Emergency_Brake = True
        break
    else:
        continue