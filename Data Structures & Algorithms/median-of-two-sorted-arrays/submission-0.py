class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        even = (len(nums1) + len(nums2))%2 == 0
        half = (len(nums1) + len(nums2))//2

        A, B = nums1, nums2

        if len(A) > len(B): # binary search on shortest array only
            A, B = B, A

        l, r = 0, len(A)-1 
        while True:
            i = (l+r)//2
            j = half - i - 2 # to make up for 0 indexing of the 2 arrays

            # protect against index out of range
            Aleft = A[i] if i>=0 else float('-inf') 
            Aright = A[i+1] if (i+1) < len(A) else float('inf')
            Bleft = B[j] if j>=0 else float('-inf')
            Bright = B[j+1] if (j+1) < len(B) else float('inf')

            if Aleft <= Bright and Bleft <= Aright: # left partition is correct
                if even:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) /2
                else:
                    return min(Aright, Bright)
            elif Aleft > Bright: #shrink A left partition
                r = i-1
            else: #expand A left partition
                l = i+1

