# Radix Sort
# Stable sorting algorithm
# Key idea: sort from LSB->MSB (or digit)
# Time complexity is d*theta(n+k)
# where d is number of digits in largest number, n is number of numbers, k is range of the digits

def counting_sort(tempA,B,k):
   # define array with indices that go from 0 to k
   C = []
   for i in range(0,k+1):
      C = C + [0] # initialize all elements to 0

   for j in range(0,len(tempA)):
      C[tempA[j]] = C[tempA[j]]+1 # C with index == tempA[j] is incremented
   # C[i] contains number of elements from tempA that are equal to i

   for i in range(1,k+1):
      C[i] = C[i]+C[i-1]
   # C[i] contains number of elements from tempA that are <= to i

   tempB = []
   for i in range(0,len(B)):
      tempB = tempB + [0]
   
   # Place numbers in sorted position
   for j in range(0,len(tempA)):
      tempB[C[tempA[j]]-1] = B[j]
      C[tempA[j]] = C[tempA[j]]-1

   # save sorted list in output list
   for i in range(0,len(B)):
      B[i] = tempB[i]


# A is list of numbers that need to be sorted
# d is number of digits
def radix_sort(A,d):
   # define sorted output list
   O = []
   for i in range(0,len(A)):
      O = O + [A[i]] # initialize all elements to 0

   largestIdx = 1
   for i in range(0,d):
      largestIdx = largestIdx*10
    
   tempA = []
   for i in range (0,len(A)):
      tempA += [0]

   # call counting sort on each digit of numbers in A
   digitIdx = 10
   while (digitIdx <= largestIdx):
      for i in range (0,len(A)):
         tempA[i] = O[i]%digitIdx
      counting_sort(tempA,O,digitIdx)
      print("After sorting a digit:", O)
      digitIdx = digitIdx*10

   # save sorted list in input so that it can be used by caller
   for i in range(0,len(O)):
      A[i] = O[i]

# testing
A = [857,814,724,937,152,654,11,7]
print(A)
radix_sort(A,3)
print(A)