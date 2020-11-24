# Quicksort
# divide-and-conquer
# Recursive

import random

def partition(A,left,right):
   ls = left
   pivot = A[left]

   for i in range(left+1,right+1):

      # if smaller than pivot->move element forward
      if (A[i] <= pivot):
         ls = ls+1
         A[i],A[ls] = A[ls],A[i]

   # want pivot to be around middle point->subarrays have even amount of work
   A[left],A[ls] = A[ls],A[left]
   # now pivot is in position where elements to left are smaller
   # and elements to right are larger

   return(ls)

# O(nlgn)
def quicksort(A,left,right):
   pivot = partition(A,left,right)

   if (pivot>left):
      quicksort(A,left,pivot)

   if (pivot+1<right):
      quicksort(A,pivot+1,right)

def randomized_partition(A,left,right):
   i = random.randint(left,right)

   if (i!=left):
      A[left],A[i] = A[i],A[left]
   
   return partition(A,left,right)

def randomized_quicksort(A,left,right):
   pivot = randomized_partition(A,left,right)

   if (pivot>left):
      quicksort(A,left,pivot)

   if (pivot+1<right):
      quicksort(A,pivot+1,right)


# Change array below to test
unsortedA = [17,12,3,26,8,19]
l = 0
r = len(unsortedA)-1
print(unsortedA)
quicksort(unsortedA,l,r)
print(unsortedA)

unsortedB = [1,3,5,2,4,7,9,8,6]
l = 0
r = len(unsortedB)-1
print(unsortedB)
randomized_quicksort(unsortedB,l,r)
print(unsortedB)

