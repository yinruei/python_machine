fp = open('file.txt','r')
if fp != None:
    str = fp.read()
    print(str)
    str = fp.read()
    print(str)
fp.close()

fp = open('file.txt','r')
if fp != None:
    strList = fp.readlines()
    print(strList)
fp.close()