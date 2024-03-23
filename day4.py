def fpb (x, y) :
    if y == 0:
        return x
    else :
        return fpb (y, x%y); 


print(fpb(1, 2))