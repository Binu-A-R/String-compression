def str_compression():
    index = 0
    let_tr = input("enter the string: ")
    new_string = ""
    len_str = len(let_tr)
    if let_tr.isalpha():
        while index != len_str:
            count = 1
            while (index < len_str - 1) and (let_tr[index] == let_tr[index + 1]):
                count += 1
                index += 1
            if count == 1:
                new_string += str(let_tr[index])
            else:
                new_string += str(count) + str(let_tr[index])
            index += 1
        print(new_string)
        print("compression ratio: ", len(let_tr), ":", len(new_string))
    else:
        print("Enter only letter")


str_compression()
