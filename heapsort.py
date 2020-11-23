# Heapsort
# Use max-heaps
# If indices start at 1: parent = floor(i/2) ; left_child = 2i ; right_child = (2i+1)
# If indices start at 0: parent = floor((i-1)/2) ; left_child = 2i+1 ; right_child = (2i+2)
# In this file, indices start at 0

def parent(i):
   return((i-1)//2) # floor division

def left_child(i):
   return((2*i)+1)

def right_child(i):
   return((2*i)+2)

# O(lgn)
# Maintains max-heap property
def max_heapify(A,i,n):
   largest = i
   l = left_child(i)
   r = right_child(i)

   if ((l<n)and(A[l]>A[largest])):
      largest = l

   if ((r<n)and(A[r]>A[largest])):
      largest = r

   # Want largest value before left and right to maintain property
   if (largest!=i):
      temp = A[i]
      A[i] = A[largest]
      A[largest] = temp
      max_heapify(A,largest,n)


# O(n)
# Builds max heap from unordered input array
def build_max_heap(A,n):
   # elements in second half of array are leaves
   # need parent indices->max_heapify will check children of parents
   for i in range(((n//2)-1),-1,-1):
      max_heapify(A,i,n)

# O(nlgn)
# Sorts an array in place
def heapsort(A):
   if (len(A)==0):
      print("Error: empty array")
      return
   
   build_max_heap(A,len(A))

   for i in range(len(A)-1,0,-1):
      temp = A[i]
      A[i] = A[0] # move largest element to end of list
      A[0] = temp
      max_heapify(A,0,i)

      
# Change values of unsortedA to test
unsortedA = [5,16,2,1,9,12,189,90]
print(unsortedA)
heapsort(unsortedA)
print(unsortedA)






