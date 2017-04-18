def quadric (a,b,c):
    delta=b**2-4*a*c
    if delta > 0:
        x1 = (-b - (delta ** (1.0 / 2.0))) / (2.0 * a)
        x2 = (-b + (delta ** (1.0 / 2.0))) / (2.0 * a)
        return [x2,x1]
    elif delta ==0:
        x0 = -b / 2.0 * a

        return x0
    else:
        return "No Roots"
print quadric(3, -9, 6)
print quadric(1,10,24)
print quadric(1,3,-4)
print quadric(1,2,1)
print quadric(1,1,1)

# AD2
def capital(K,p,t,bool):
    ods=K*(p/100)*t
    if bool ==True:
        ods=ods*0.81
    else:
        ods

    return ods
print capital(5000,5.0,1,False)
print capital(5000,5.0,1,True)