def factorsRange(n, m):  
    dict = {}
    for num in range(n, m+1):
        value = []
        for i in range(2, num):
            if num % i == 0:
                value.append(i)
        if value:                
            dict[num] = value
        else:
            dict[num] = ['None']
    return dict   