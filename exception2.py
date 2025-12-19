try:
    num=[10,20,30]
    print(num[2])
except IndexError as ie:
    print(ie)
else:
    print('no error')