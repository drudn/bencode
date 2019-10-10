#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      danru
#
# Created:     13-09-2019
# Copyright:   (c) danru 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def integer(s):
    if(s[0]=='i' and s[-1]=='e'):
        k=s[1:]
        t=k[:-1]
        return int(t)
    else:
        return false

def toInteger(s):
    try:
        y=''
        s=s[1:]
        for i in s:
            if (i=='e'):
                break
            else:
                y+=i
        return int(y)
    except:
        print("Invalid bencode integer")

#toString() converts a bencode encoded string value to it's python value
def toByteString(s):
    try:
        k=stringLength(s)
        y=len(str(k))+1
        t=s[y:y+k]
        return t
    except:
        print("Invalid bencode string value")

#stringLength() determines the length of a bencode string
def stringLength(s):
    k=0
    for i in s:
        if(i==':'):
            return int(s[:k])
        else:
            k+=1


#findvalues(,) is a method that recursively iterates through a bencode encoded list or dictionary to determine the keys/values for lists/dictionaries
def findvalues(s, current):
    if (len(s)==0):
        return current
    if (s[0]=='i'):
        y=toInteger(s)
        current.append(str(y))
        i=len(str(y))+2
        a=s[i:]
        return findvalues(a, current)
    else:
        g=stringLength(s)
        b=toByteString(s)
        current.append(b)
        q=str(g)+':'+b
        a=s[len(q):]
        return findvalues(a, current)

#convert() is a general method that accepts either a string, integer, list or dictionary encoded in bencode and return the corresponding value in python.
def convert(s):
    current = []
    start = s[0]
    if(start=='i'):
        current = toInteger(s)
        return current
    elif(start=='d'):
        t=s[1:-1]
        current = findvalues(t, current)
        dict={}
        x=current[::2]
        lst=current[1:]
        y=lst[::2]
        for i in range(0,len(y)):
            dict[x[i]]=y[i]
        return dict
    elif(start=='l'):
        t=s[1:-1]
        current = findvalues(t, current)
        return current
    else:
        b=toByteString(s)
        return b
