try:
    a,b=10,0
    print(a//b)
except ZeroDivisionError as ze:
    print(ze)