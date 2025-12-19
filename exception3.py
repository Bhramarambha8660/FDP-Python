try:
    f=open('D:\\bangalore.txt','r')
except FileNotFoundError as fe:
    print(fe)
else:
    print('no error')
finally:
    print('always executed')