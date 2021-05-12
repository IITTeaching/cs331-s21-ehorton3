import urllib
import requests

def book_to_words(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    booktxt = urllib.request.urlopen(book_url).read().decode()
    bookascii = booktxt.encode('ascii','replace')
    return bookascii.split()

def radix_a_book(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    wordList = book_to_words()
    a= radix_sort(wordList)
    b = wordList
    b.sort()
    if a is b:
        print("sorted correctly")
    else:
        for i in range(len(a)):
            if a[i] != b[i]:
                print("a",a[i],"b",b[i])
        print("sad sad failure")


def radix_sort(keys):
    mLeng= len(max(keys, key =len))
    #sort each part
    for i in range(mLeng):
        count_sort(keys,i)
    return keys



def count_sort(lst,leng):
    mNum = 0
    for i in range(len(lst)):
        try:
            index = ord(str(lst[i])[leng])
        except:
            index = -1
        if index>mNum:
            mNum =index
    counts = [0]*(mNum+1)
    counts[-1]=0
    fin = [None]*len(lst)
    for i in range(len(lst)):
        try:
            char = str(lst[i])[leng]
            counts[ord(char)] +=1
        except:
            counts[-1]+=1
    for i in range (1,mNum):
        counts[i] = counts[i]+counts[i-1]
    for i in range(len(lst)):
        try:
            index = ord(str(lst[i])[leng])
        except:
            index = -1
        xdex = counts[index] - 1
        fin[xdex] = lst[i]
        counts[index]-=1
    return fin

radix_a_book(book_url="https://www.gutenberg.org/files/64317/64317-0.txt")