if choose.lower() == 'no' or choice == '2':
    # festi 2 gun stall
    for i in Narrator_line:
        if i['Note'] == 'Festival':
            if i['Answer'] == 'Virtual gun game':
                slowprint(i['Output'])
    while choice:
        # festi 3
        choice_list = []
        for i in Question_line:
            if i['Note'] == 'Wake up':
                slowprint(i['Question'])
        for i in Narrator_line:
            if i['Note'] == 'Wake up':
                choice_list.append(i['Answer'])
        for i in range(len(choice_list)):
            print(f"{i}: {choice_list[i]}")
        choose = input("Enter your choice: ")
        for i in range(len(choice_list)):
            if choose == choice_list[i] or choose == str(i - 1):
                break
    print('Wrong answer')
    if choose.lower() == 'no' or choice == '2':
    # no
    for i in Narrator_line:
        if i['Note'] ==:
            if i['Answer'] ==:
                slowprint(i['Output'])