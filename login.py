clearnum = 1  # for clearing        | sets clearnum to 1
logix = "admin"  # you can change login here
logiy = "adminpass"  # you can change password here

print("Please log in")
name = input("Login: ")  # ask user for login
passw = input("Password: ")  # aks user for password

is_name_true = name == logix  # check if login is correct (chek if login is logix (admin))
is_pass_true = passw == logiy  # check if password is correct (check if password is logiy (adminpass))
if is_name_true == True:  # if login is correct then
    if is_pass_true == True:  # if password is correct then
        while clearnum < 100:  # clearing | print nothing              is 100
            print(" ")  # clearing        |              until clearnum
            clearnum += 1  # clearing     adds +1 to clearnum every loop
        # place for app
        print("Hello " + name + "!")

        # place for app end
    elif is_pass_true == False:  # if password is wrong then
        print("Unkown name or password (DevNote: password false)")  # TODO remove devnote
elif is_name_true == False:  # if login is wrong then
    print("Unkown name or password (DevNote: login false)")  # TODO remove devnote
