'''
def search_element(x,listed):
    truth = False
    for number in listed:
        if float(x) == number:
            truth = True
            break
        else:
            continue
    print(truth)

search_element(11.0,[12.0,23.5,45.6,100.2])
'''

'''
def search_element(x,listed):
    truth = False
    if float(x) == listed[(len(listed)//2)]:
        truth = True
        print('Right smack in the middle')
    elif float(x) >= listed[len(listed)//2]:
        for num in listed[(len(listed)//2)+1:]:
            if float(x) == num:
                truth = True
                print('Towards the right')
    elif float(x) <= listed[len(listed)//2]:
        for num in listed[:(len(listed)//2)]:
            if float(x) == num:
                truth = True
                print('Towards the left')
    print(truth)

search_element(8,[2,3,5,7,8,21.0,54.0,63])
'''

'''
def search_element(x,listed):
    match_list = []
    for number in listed:
        if float(x) == number:
            match_list.append(x)
            if len(match_list) >= 10:
                break
        else:
            continue
    print(len(match_list))

search_element(10,[10,11,10,12,10,40,13,10,90,10,10,10,10,10,10,10,10,10,10])
'''

'''
my_list = [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10]
def matching(A):
    truth = False
    for i in range(len(A)):
        if i == A[i]:
            truth = True
    print(truth)

matching(my_list)
'''
