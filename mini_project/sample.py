def add(x,y):
    return x+y


def is_leap(yy):
    #return yy%4==0
    return yy%400==0 or yy%4==0 and yy%100!=0


def mydiv(a,b):
        res=a/b 
        return res