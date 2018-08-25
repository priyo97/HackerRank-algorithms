def main():
    y = int(input())
    
    if y < 1918:
        if isJulianYear(y):
            print("12.09."+str(y))
        else:
            print("13.09."+str(y))
    
    elif y == 1918:
        print("26.09.1918")
    else:
        if isGregorianYear(y):
            print("12.09."+str(y))
        else:
            print("13.09."+str(y))
    
        
def isJulianYear(y):
    
    if not y % 4:
        return True
    else:
        return False
    
def isGregorianYear(y):
    
    if not y % 400:
        return True
    elif y % 100 and not y % 4:
        return True
    else:
        return False
    
main()
    
