clearnum = 1  # for clearing
logix = "admin"  # you can change login here
logiy = "adminpass"  # you can change password here

print("Please log in")
name = input("Login: ")
passw = input("Password: ")

is_name_true = name == logix
is_pass_true = passw == logiy
if is_name_true == True:
    if is_pass_true == True:
        while clearnum < 100:  # clearing
            print(" ")  # clearing
            clearnum += 1  # clearing
        print("Hello " + name + "!")
        # place for app

        # place for app end
    elif is_pass_true == False:
        print("Unkown name or password (DevNote: password false)")  # TODO remove devnote
elif is_name_true == False:
    print("Unkown name or password (DevNote: login false)")  # TODO remove devnote