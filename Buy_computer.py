
current_choice = "_"
available_parts = ["Computer",
                   "Monitor",
                   "Keyboard",
                   "Mouse",
                   "Mouse mat"]
computer_parts  = []

while current_choice != 0:
    if current_choice in "12345":
        print("Adding {}".format(current_choice))
        if current_choice == '1':
            computer_parts.append("Computer")
        elif current_choice == '2':
            computer_parts.append("Monitor")
        elif current_choice == '3':
            computer_parts.append('Keyboard')
        elif current_choice == '4':
            computer_parts.append('Mouse')
        elif current_choice == '5':
            computer_parts.append('Mouse_mat')
    else:
        # print("Please select options from the list")
        # print("1. Computer")
        # print("2. Monitor")
        # print("3. keyboard")
        # print("4. mouse")
        # print("5. mouse mat")
        # print("0. Finish")
        # for parts in available_parts:
        #     print("{0}: {1}".format(current_choice)+1, parts)
        for number,parts in enumerate(available_parts):
            print("{0}: {1}".format(number+1, parts))


    current_choice = input()
print(current_choice, computer_parts)