def modify_list(my_list):
    my_list.append(4)
    my_list[0] = 100

main_list = [1, 2, 3]
modify_list(main_list)

print(main_list)