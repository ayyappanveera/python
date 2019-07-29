def rev(str):
    s =""
    for ch in str:
        s=ch+s
    return s
mystr =input()
print(rev(mystr))
