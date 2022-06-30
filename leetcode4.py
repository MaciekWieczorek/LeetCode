def findMedianSortedArrays(nums1, nums2):
        n = nums1 + nums2
        n.sort()
        idx = len(n)//2
        
        if len(n)%2 == 0:
            median = (n[idx] + n[idx+1])/2
        else:
            median = n[idx]
        
        return median

s = findMedianSortedArrays([1,2], [3,4])
print(s)