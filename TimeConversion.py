def main():
    hr, min , sec = input().split(":")
    sec , t = sec[:2], sec[2:]
    
    hr = int(hr)
    min = int(min)
    sec = int(sec)
    
    if hr == 12:
        hr = 0
        
    if t == "AM":
        print("{:02d}:{:02d}:{:02d}".format(0 + hr,min,sec))
    else:
        print("{:02d}:{:02d}:{:02d}".format(12 + hr,min,sec))
        
main()
