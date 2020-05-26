data = "<hahah>fgfgfgf<dfdfdf></hey>"
count = 0
token_list = []

with open("test.xml") as fp:
    Lines = fp.readlines()
    for line in Lines:
        count += 1
        data = line.strip()
        while len(data) > 0:
            front = data.index('<')
            end = data.index('>')
            if data[:front]:
                token_list.append(data[:front])
            token_list.append(data[front:end+1])
            data = data[end+1:]


print(token_list)
