list= []
i= 0
while i< 1:
    print("1.input name;2.delete name;3.output name;4.show all the names;5.")
    num = int(input("Please input the number:"))
    if num== 1:
        a= input("Please input the name:")
        list.append(a)
    elif num== 2:
        b= input("Please input the name:")
        c= list.index(b)
        list.pop(c)
    elif num== 3:
        d= int(input("Please input the number:"))
        if d< (len(list)):
            print(list[d])
        else:
            print("There is no such name!")
    elif num== 4:
        t= 0
        while t< (len(list)):
            print(list[t])
            t= t+ 1
    else:
        continue
