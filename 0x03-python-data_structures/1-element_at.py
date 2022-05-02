def element_at(my_list, idx):
    lenlist = len(my_list)
    if(idx < 0):
        return (NULL)
    elif (idx > lenlist):
        return (NULL)
    else:
        return (my_list[idx])
