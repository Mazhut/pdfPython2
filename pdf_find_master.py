def fill_folder(li):
    new_list = []
    i = 0
    j = 0
    for file in li:
        if file != '.DS_Store' and j == 0:
            new_list.append(file)
            new_list[i] = open(f'pdfs/{li[j]}', 'rb')
            i += 1
        elif file != '.DS_Store' and j > 0:
            new_list.append(file)
            new_list[i] = open(f'pdfs/{li[j]}', 'rb')
            i += 1
            j += 1
        else:
            j += 1
    return new_list
