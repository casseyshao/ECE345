# Counting Sort
# Assumes each element in input array has value in range 0 to k
# Runtime is Big-Theta(n+k)
# Use counting sort when k=O(n)->running time is Big-Theta(n)

def counting_sort(A,B,k):
   # define array with indices that go from 0 to k
   C = []
   for i in range(0,k+1):
      C = C + [0] # initialize all elements to 0

   for j in range(0,len(A)):
      C[A[j]] = C[A[j]]+1 # C with index == A[j] is incremented
   # C[i] contains number of elements from A that are equal to i

   for i in range(1,k+1):
      C[i] = C[i]+C[i-1]
   # C[i] contains number of elements from A that are <= to i

   # Place numbers in sorted position
   for j in range(0,len(A)):
      B[C[A[j]]-1] = A[j]
      C[A[j]] = C[A[j]]-1


# Test using different values for array
unsortedA = [2,6,4,4,1,5,3]
maxVal = 6
# sortedOutput needs to be same size as unsortedA
sortedOutput = []
for i in range(0,len(unsortedA)):
   sortedOutput = sortedOutput + [0]
counting_sort(unsortedA,sortedOutput,maxVal)
print(unsortedA)
print(sortedOutput)
