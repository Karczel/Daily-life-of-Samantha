slowprint(i['Output'])
while choice:
    # what do next?
    choice_list = []
    for i in Question_line:
        if i['Note'] == 'What you want to do':
            slowprint(i['Question'])
    for i in Narrator_line:
        if i['Note'] == 'What you want to do':
            choice_list.append(i['Answer'])
    choice_list.pop("Karczel's House")
    for i in range(len(choice_list)):
        print(f"{i}: {choice_list[i]}")
    choose = input("Enter your choice: ")
    for i in range(len(choice_list)):
        if choose == choice_list[i] or choose == str(i + 1):
            break
    print('Wrong answer')
if choose.lower() == "omisha's room" or choose == '4':
    # omisha
    for i in Narrator_line:
        if i['Note'] == 'What you want to do':
            if i['Answer'] == "Omisha's room":
                slowprint(i['Output'])
    while choice:
        # what do next?
        choice_list = []
        for i in Question_line:
            if i['Note'] == 'What you want to do':
                slowprint(i['Question'])
        for i in Narrator_line:
            if i['Note'] == 'What you want to do':
                choice_list.append(i['Answer'])
        choice_list.pop("Karczel's House")
        choice_list.pop("Omisha's room")
        for i in range(len(choice_list)):
            print(f"{i}: {choice_list[i]}")
        choose = input("Enter your choice: ")
        for i in range(len(choice_list)):
            if choose == choice_list[i] or choose == str(i + 1):
                break
        print('Wrong answer')
    if choose.lower() == "the kitchen" or choose == '2':
        # kitchen
        for i in Narrator_line:
            if i['Note'] == 'What you want to do':
                if i['Answer'] == "The kitchen":
                    slowprint(i['Output'])
        while choice:
            # what do next?
            choice_list = []
            for i in Question_line:
                if i['Note'] == 'What you want to do':
                    slowprint(i['Question'])
            for i in Narrator_line:
                if i['Note'] == 'What you want to do':
                    choice_list.append(i['Answer'])
            choice_list.pop("Karczel's House")
            choice_list.pop("Omisha's room")
            choice_list.pop("The kitchen")
            for i in range(len(choice_list)):
                print(f"{i}: {choice_list[i]}")
            choose = input("Enter your choice: ")
            for i in range(len(choice_list)):
                if choose == choice_list[i] or choose == str(i + 1):
                    break
            print('Wrong answer')
        if choose.lower() == "zahur’s room;" or choose == '1':
            # see zahur
            for i in Narrator_line:
                if i['Note'] == 'What you want to do':
                    if i['Answer'] == "Zahur’s room;":
                        slowprint(i['Output'])
        slowprint("There's nothing else to do today.")
    elif choose.lower() == "zahur’s room" or choose == '1':
        # see zahur
        for i in Narrator_line:
            if i['Note'] == 'What you want to do':
                if i['Answer'] == "Zahur’s room":
                    slowprint(i['Output'])
        while choice:
            # what do next?
            choice_list = []
            for i in Question_line:
                if i['Note'] == 'What you want to do':
                    slowprint(i['Question'])
            for i in Narrator_line:
                if i['Note'] == 'What you want to do':
                    choice_list.append(i['Answer'])
            choice_list.pop("Karczel's House")
            choice_list.pop("Omisha's room")
            choice_list.pop("Zahur’s room")
            for i in range(len(choice_list)):
                print(f"{i}: {choice_list[i]}")
            choose = input("Enter your choice: ")
            for i in range(len(choice_list)):
                if choose == choice_list[i] or choose == str(i + 1):
                    break
            print('Wrong answer')
        if choose.lower() == "the kitchen" or choose == '1':
            # kitchen
            for i in Narrator_line:
                if i['Note'] == 'What you want to do':
                    if i['Answer'] == "The kitchen":
                        slowprint(i['Output'])
        slowprint("There's nothing else to do today.")
elif choose.lower() == 'the kitchen' or choose == '3':
    # kitchen
    for i in Narrator_line:
        if i['Note'] == 'What you want to do':
            if i['Answer'] == 'The kitchen':
                slowprint(i['Output'])
    while choice:
        # what do next?
        choice_list = []
        for i in Question_line:
            if i['Note'] == 'What you want to do':
                slowprint(i['Question'])
        for i in Narrator_line:
            if i['Note'] == 'What you want to do':
                choice_list.append(i['Answer'])
        choice_list.pop("Karczel's House")
        choice_list.pop('The kitchen')
        for i in range(len(choice_list)):
            print(f"{i}: {choice_list[i]}")
        choose = input("Enter your choice: ")
        for i in range(len(choice_list)):
            if choose == choice_list[i] or choose == str(i + 1):
                break
        print('Wrong answer')
    if choose.lower() == "omisha's room" or choose == '2':
        # omisha room
        for i in Narrator_line:
            if i['Note'] == 'What you want to do':
                if i['Answer'] == "Omisha's room":
                    slowprint(i['Output'])
        while choice:
            # what do next?
            choice_list = []
            for i in Question_line:
                if i['Note'] == 'What you want to do':
                    slowprint(i['Question'])
            for i in Narrator_line:
                if i['Note'] == 'What you want to do':
                    choice_list.append(i['Answer'])
            choice_list.pop("Karczel's House")
            choice_list.pop("The kitchen")
            choice_list.pop("Omisha's room")
            for i in range(len(choice_list)):
                print(f"{i}: {choice_list[i]}")
            choose = input("Enter your choice: ")
            for i in range(len(choice_list)):
                if choose == choice_list[i] or choose == str(i + 1):
                    break
            print('Wrong answer')
        if choose.lower() == "zahur’s room;" or choose == '1':
            # see zahur
            for i in Narrator_line:
                if i['Note'] == 'What you want to do':
                    if i['Answer'] == "Zahur’s room;":
                        slowprint(i['Output'])
        slowprint("There's nothing else to do today.")
    elif choose.lower() == "zahur’s room" or choose == '1':
        # see zahur
        for i in Narrator_line:
            if i['Note'] == 'What you want to do':
                if i['Answer'] == "Zahur’s room":
                    slowprint(i['Output'])
        while choice:
            # what do next?
            choice_list = []
            for i in Question_line:
                if i['Note'] == 'What you want to do':
                    slowprint(i['Question'])
            for i in Narrator_line:
                if i['Note'] == 'What you want to do':
                    choice_list.append(i['Answer'])
            choice_list.pop("Karczel's House")
            choice_list.pop("The kitchen")
            choice_list.pop("Zahur’s room")
            for i in range(len(choice_list)):
                print(f"{i}: {choice_list[i]}")
            choose = input("Enter your choice: ")
            for i in range(len(choice_list)):
                if choose == choice_list[i] or choose == str(i + 1):
                    break
            print('Wrong answer')
        if choose.lower() == "omisha's room" or choose == '1':
            # omisha
            for i in Narrator_line:
                if i['Note'] == 'What you want to do':
                    if i['Answer'] == "Omisha's room":
                        slowprint(i['Output'])
        slowprint("There's nothing else to do today.")
elif choose.lower() == "zahur’s room" or choose == '2':
    # zahur room
    for i in Narrator_line:
        if i['Note'] == 'What you want to do':
            if i['Answer'] == "Zahur’s room":
                slowprint(i['Output'])
    while choice:
        # what do next?
        choice_list = []
        for i in Question_line:
            if i['Note'] == 'What you want to do':
                slowprint(i['Question'])
        for i in Narrator_line:
            if i['Note'] == 'What you want to do':
                choice_list.append(i['Answer'])
        choice_list.pop("Karczel's House")
        choice_list.pop("Zahur’s room")
        for i in range(len(choice_list)):
            print(f"{i}: {choice_list[i]}")
        choose = input("Enter your choice: ")
        for i in range(len(choice_list)):
            if choose == choice_list[i] or choose == str(i + 1):
                break
        print('Wrong answer')
    if choose.lower() == "omisha's room" or choose == '2':
        # omisha room
        for i in Narrator_line:
            if i['Note'] == 'What you want to do':
                if i['Answer'] == "Omisha's room":
                    slowprint(i['Output'])
        while choice:
            # what do next?
            choice_list = []
            for i in Question_line:
                if i['Note'] == 'What you want to do':
                    slowprint(i['Question'])
            for i in Narrator_line:
                if i['Note'] == 'What you want to do':
                    choice_list.append(i['Answer'])
            choice_list.pop("Karczel's House")
            choice_list.pop("Zahur’s room")
            choice_list.pop("Omisha's room")
            for i in range(len(choice_list)):
                print(f"{i}: {choice_list[i]}")
            choose = input("Enter your choice: ")
            for i in range(len(choice_list)):
                if choose == choice_list[i] or choose == str(i + 1):
                    break
            print('Wrong answer')
        if choose.lower() == "the kitchen" or choose == '1':
            # the kitchen
            for i in Narrator_line:
                if i['Note'] == 'What you want to do':
                    if i['Answer'] == "The kitchen":
                        slowprint(i['Output'])
        slowprint("There's nothing else to do today.")
    elif choose.lower() == "the kitchen" or choose == '1':
        # the kitchen
        for i in Narrator_line:
            if i['Note'] == 'What you want to do':
                if i['Answer'] == "The kitchen":
                    slowprint(i['Output'])
        while choice:
            # what do next?
            choice_list = []
            for i in Question_line:
                if i['Note'] == 'What you want to do':
                    slowprint(i['Question'])
            for i in Narrator_line:
                if i['Note'] == 'What you want to do':
                    choice_list.append(i['Answer'])
            choice_list.pop("Karczel's House")
            choice_list.pop("Zahur’s room")
            choice_list.pop("The kitchen")
            for i in range(len(choice_list)):
                print(f"{i}: {choice_list[i]}")
            choose = input("Enter your choice: ")
            for i in range(len(choice_list)):
                if choose == choice_list[i] or choose == str(i + 1):
                    break
            print('Wrong answer')
        if choose.lower() == "omisha's room" or choose == '1':
            # omisha
            for i in Narrator_line:
                if i['Note'] == 'What you want to do':
                    if i['Answer'] == "Omisha's room":
                        slowprint(i['Output'])
        slowprint("There's nothing else to do today.")
# do nothing(void)