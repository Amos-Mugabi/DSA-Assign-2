# num 3

mylist =["ucu", "kyambogo", "ndejje", "gulu", "victoria"]


def myunilist(mylist):
    string_length = []

    for string in mylist:
        if len(string) > 5:
            string_length.append(string)
    return string_length

final_list = myunilist(mylist)
print(final_list)
