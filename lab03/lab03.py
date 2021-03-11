import urllib.request
import unittest
from typing import TypeVar, Callable, List

T = TypeVar('T')
S = TypeVar('S')

#################################################################################
# EXERCISE 1
#################################################################################
def mysort(lst: List[T], compare: Callable[[T, T], int]) -> List[T]:
    """
    This method should sort input list lst of elements of some type T.

    Elements of the list are compared using function compare that takes two
    elements of type T as input and returns -1 if the left is smaller than the
    right element, 1 if the left is larger than the right, and 0 if the two
    elements are equal.
    """
    pass
    sortedLst = []
    for i in lst:
        if len(sortedLst) == 0:
            sortedLst.append(i)
        else:
            inserted = False
            for j in range (len(sortedLst)):
                compRes= compare(i,sortedLst[j])
                if compRes == -1 or compRes == 0:
                    sortedLst.insert(j,i)
                    inserted = True
                    break
            if not inserted:
                sortedLst.insert(len(sortedLst),i) 
    return sortedLst

def mybinsearch(lst: List[T], elem: S, compare: Callable[[T, S], int]) -> int:
    """
    This method search for elem in lst using binary search.

    The elements of lst are compared using function compare. Returns the
    position of the first (leftmost) match for elem in lst. If elem does not
    exist in lst, then return -1.
    """
    min = 0
    max = len(lst)-1
    found = False
    i =0
    while found is False:
        if (min > max):
            return -1
            break
        mid = min + (max-min) // 2
        #check if element is the same
        if compare(lst[mid], elem ) == 0:
            #find left most element
            leftMost = False
            while leftMost is False:
                if mid>0 and compare(lst[mid-1], elem ) == 0:
                    mid = mid -1
                else:
                    leftMost = True
                    break
            return mid
        elif compare(lst[mid],elem) ==-1:
            #print("min was " + str(min) + " min is now " + str(mid+1) + " max is " + str(max))
            min = mid+1
        elif compare(lst[mid],elem) ==1:
            #print("max was " + str(max) + " max is now " + str(mid-1) + " Min is " + str(min))
            max = mid-1
        

class Student():
    """Custom class to test generic sorting and searching."""
    def __init__(self, name: str, gpa: float):
        self.name = name
        self.gpa = gpa

    def __eq__(self, other):
        return self.name == other.name

# 30 Points (total)
def test1():
    """Tests for generic sorting and binary search."""
    print(80 * "#" + "\nTests for generic sorting and binary search.")
    test1_1()
    test1_2()
    test1_3()
    test1_4()
    test1_5()

# 6 Points
def test1_1():
    """Sort ints."""
    print("\t-sort ints")
    tc = unittest.TestCase()
    ints = [ 4, 3, 7, 10, 9, 2 ]
    intcmp = lambda x,y:  0 if x == y else (-1 if x < y else 1)
    sortedints = mysort(ints, intcmp)
    tc.assertEqual(sortedints, [2, 3, 4, 7, 9, 10])

# 6 Points
def test1_2():
    """Sort strings based on their last character."""
    print("\t-sort strings on their last character")
    tc = unittest.TestCase()
    strs = [ 'abcd', 'aacz',  'zasa' ]
    suffixcmp = lambda x,y: 0 if x[-1] == y[-1] else (-1 if x[-1] < y[-1] else 1)
    sortedstrs = mysort(strs,suffixcmp)
    tc.assertEqual(sortedstrs, [ 'zasa', 'abcd', 'aacz' ])

# 6 Points
def test1_3():
    """Sort students based on their GPA."""
    print("\t-sort students on their GPA.")
    tc = unittest.TestCase()
    students = [ Student('Josh', 3.0), Student('Angela', 2.5), Student('Vinesh', 3.8),  Student('Jia',  3.5) ]
    sortedstudents = mysort(students, lambda x,y: 0 if x.gpa == y.gpa else (-1 if x.gpa < y.gpa else 1))
    expected = [ Student('Angela', 2.5), Student('Josh', 3.0), Student('Jia',  3.5), Student('Vinesh', 3.8) ]
    tc.assertEqual(sortedstudents, expected)

# 6 Points
def test1_4():
    """Binary search for ints."""
    print("\t-binsearch ints")
    tc = unittest.TestCase()
    ints = [ 4, 3, 7, 10, 9, 2 ]
    intcmp = lambda x,y:  0 if x == y else (-1 if x < y else 1)
    sortedints = mysort(ints, intcmp)
    tc.assertEqual(mybinsearch(sortedints, 3, intcmp), 1)
    tc.assertEqual(mybinsearch(sortedints, 10, intcmp), 5)
    tc.assertEqual(mybinsearch(sortedints, 11, intcmp), -1)

# 6 Points
def test1_5():
    """Binary search for students by gpa."""
    print("\t-binsearch students")
    tc = unittest.TestCase()
    students = [ Student('Josh', 3.0), Student('Angela', 2.5), Student('Vinesh', 3.8),  Student('Jia',  3.5) ]
    stcmp = lambda x,y: 0 if x.gpa == y.gpa else (-1 if x.gpa < y.gpa else 1)
    stbincmp = lambda x,y: 0 if x.gpa == y else (-1 if x.gpa < y else 1)
    sortedstudents = mysort(students, stcmp)
    tc.assertEqual(mybinsearch(sortedstudents, 3.5, stbincmp), 2)
    tc.assertEqual(mybinsearch(sortedstudents, 3.7, stbincmp), -1)

#################################################################################
# EXERCISE 2
#################################################################################
class PrefixSearcher():
    def __init__(self, document, k):
        """
        Initializes a prefix searcher using a document and a maximum
        search string length k.
        """
        strs= []
        chars = list(document)
        for i in range(len(chars)):
            strTemp = ""
            strTemp += chars[i]
            for j in range (0,k):
                if(i+j+1<len(chars)):
                    strTemp += chars[i+j+1]
            if strTemp not in strs:
                strs.append(strTemp)
        strCmp = lambda x,y: 0 if x is y else (-1 if x < y else 1)
        strs = mysort(strs,strCmp)
        self.strs = strs
        self.k =k


    def search(self, q):
        """
        Return true if the document contains search string q (of

        length up to n). If q is longer than n, then raise an
        Exception.
        """
        if(len(q)<=self.k):
            for item in self.strs:
                if q == item[0:len(q)]:
                    return True
            return False
        else:
            print("raising error")
            raise LookupError("q is too large")


def test2_c():
    firstLcmp = lambda x,y: 0 if x is y else (-1 if x < y else 1)
    tester = ["lac","lad","lax","ll","lda","ldb","ldc","ldd","lde","ldf","ld","ldi"]
    tester=mysort(tester,firstLcmp)
    print (mybinsearch(tester,"ll",firstLcmp))
    p = PrefixSearcher("Hello World!", 2)
    print(p.search("ll"))



# 30 Points
def test2():
    print("#" * 80 + "\nSearch for substrings up to length n")
    test2_1()
    test2_2()

# 15Points
def test2_1():
    print("\t-search in hello world")
    tc = unittest.TestCase()
    p = PrefixSearcher("Hello World!", 1)
    tc.assertTrue(p.search("l"))
    tc.assertTrue(p.search("e"))
    tc.assertFalse(p.search("h"))
    tc.assertFalse(p.search("Z"))
    tc.assertFalse(p.search("Y"))
    p = PrefixSearcher("Hello World!", 2)
    tc.assertTrue(p.search("l"))
    tc.assertTrue(p.search("ll"))
    tc.assertFalse(p.search("lW"))

# 20 Points
def test2_2():
    print("\t-search in Moby Dick")
    tc = unittest.TestCase()
    md_url = 'https://www.gutenberg.org/files/2701/2701-0.txt'
    md_text = urllib.request.urlopen(md_url).read().decode()
    p = PrefixSearcher(md_text[0:1000],4)
    tc.assertTrue(p.search("Moby"))
    tc.assertTrue(p.search("Dick"))

#################################################################################
# EXERCISE 3
#################################################################################
class SuffixArray():

    def __init__(self, document: str):
        """
        Creates a suffix array for document (a string).
        """
        self.doc = document
        sa = []
        for i in range(len(document)):
            sa.append(document[i:])
        self.sa = mysort(sa,self.strComp)

    def strComp(self, x, y):
        
        #check which string has a smaller length
        smallLeng =0
        if len(x)>=len(y):
            smallLeng = len(y)
            failsafe = 1
        else:
            smallLeng = len(x)
            failsafe =-1
        #do comparisons
        if x[0:smallLeng] == y[0:smallLeng]:
            return 0
        if x[0:smallLeng]< y[0:smallLeng]:
            return -1
        if x[0:smallLeng]> y[0:smallLeng]:
            return 1
        return failsafe

         # self.strcmp = strcmp = lambda x,y: 0 if x[0] == y[0] else (-1 if x < y else 1)  



    def positions(self, searchstr: str):
        """
        Returns all the positions of searchstr in the documented indexed by the suffix array.
        """
        pass
        index = mybinsearch(self.sa,searchstr,self.strComp)
        searchCont= True
        indices =[]
        if index != -1:
            indices.append(index)
        i =1
        while searchCont:
            if self.sa[index+i] is searchstr:
                indices.append(index+i)
                i+=1
            else:
                searchCont=False
                break
        return indices
        
        

    def contains(self, searchstr: str):
        """
        Returns true of searchstr is coontained in document.
        """
        index = mybinsearch(self.sa,searchstr,self.strComp)
        if index != -1:
            return True
        else:
            return False

# 40 Points
def test3():
    """Test suffix arrays."""
    print(80 * "#" + "\nTest suffix arrays.")
    test3_1()
    test3_2()


# 20 Points
def test3_1():
    print("\t-suffixarray on Hello World!")
    tc = unittest.TestCase()
    s = SuffixArray("Hello World!")
    tc.assertTrue(s.contains("l"))
    tc.assertTrue(s.contains("e"))
    tc.assertFalse(s.contains("h"))
    tc.assertFalse(s.contains("Z"))
    tc.assertFalse(s.contains("Y"))
    tc.assertTrue(s.contains("ello Wo"))


# 20 Points
def test3_2():
    print("\t-suffixarray on Moby Dick!")
    tc = unittest.TestCase()
    md_url = 'https://www.gutenberg.org/files/2701/2701-0.txt'
    md_text = urllib.request.urlopen(md_url).read().decode()
    s = SuffixArray(md_text[0:1000])
    tc.assertTrue(s.contains("Moby-Dick"))
    tc.assertTrue(s.contains("Herman Melville"))
    posset = set(s.positions("Moby-Dick"))
    tc.assertEqual(posset, {355, 356})


#################################################################################
# TEST CASES
#################################################################################
def main():
    test1()
    test2()
    test3()

if __name__ == '__main__':
    main()
