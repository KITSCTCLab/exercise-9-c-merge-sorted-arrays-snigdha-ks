from typing import List

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
  # Write code here
  small_a = nums1[0:m] 
  small_b = nums2[0:n]
  i = 0 
  j = 0
  k = 0
  while(i<len(small_a) and j<len(small_b)):
    if (small_a[i] <= small_b[j]):
      nums1[k] = small_a[i]
      i+=1
    else:
      nums1[k] = small_b[j]
      j+=1
    k+=1
  while i<len(small_a):
    nums1[k]=small_a[i]
    i+=1
    k+=1
  while j<len(small_b):
    nums1[k]=small_b[j]
    j+=1
    k+=1 

# Do not change the following code
nums1 = []
nums2 = []
for item in input().split(', '):
  nums1.append(int(item))
for item in input().split(', '):
  nums2.append(int(item))
m = int(input())
n = int(input())
merge(nums1, m, nums2, n)
print(nums1)
