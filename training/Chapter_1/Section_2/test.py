#Yasss I used Recursion on my own, Hallelujah
def ConvertUsingBase(Number,Base):
    Conversion = int(Number) % Base
    if int(Number) - Conversion == 0:
        return(str(Conversion))
    return (ConvertUsingBase(str(int((int(Number) - Conversion)/Base)),Base) + str(Conversion))

x = ConvertUsingBase('241',3)

1==1