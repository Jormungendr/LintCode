# TODO Rewrite it to C++
import math
class Solution:
    """
    @param: : an int
    @param: : an int
    @return: if N can be expressed in the form of sum of K primes, return true; otherwise, return false.
    """
    def isSumOfKPrimes(n, k):
        def findSu(num):
            array = set()
            for n in range(1,num):
                array.add(n)
            for i in range(3,num):
                for jj in range(2,int(math.ceil(math.sqrt(i)))):
                    if i % jj == 0:
                        try:
                            array.remove(i)
                        except KeyError:
                            pass
                    if i % math.sqrt(i) == 0:
                        try:
                            array.remove(i)
                        except KeyError:
                            pass
            array.remove(4)
            return array
        
        array = findSu(n)
        aa = list()
        a = list()
        def ap(array,n,aa=[]):
            for j in range(1,n):
                if j < n:
                    for i in array:
                        aa.append(i)
                        if len(aa) == n:
                            a.append(aa)
                            aa = []
                ap(a,n)
                
        ap(array,k)
        sum = 0
        for i in a:
            for j in i:
                sum = sum + j
                if n == sum:
                    return True
        return False
    n = input("input n")
    k = input("input k")
    print isSumOfKPrimes(n,k)