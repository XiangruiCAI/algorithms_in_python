class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int] 
        :type nums2: List[int] 
        :rtype: float
        """
        # swap to make sure nums1 shorter
        temp = nums1
        if len(nums1) > len(nums2):
            nums1 = nums2
            nums2 = temp
        
        m = len(nums1)
        n = len(nums2)
        imin = 0
        imax = m
        while imin <= imax:
            i = (imin + imax) / 2
            j = (m + n + 1) / 2 - i
            if i < m and nums2[j-1] > nums1[i]:
                imin = i + 1
            elif i > 0 and nums1[i - 1] > nums2[j]:
                imax = i - 1
            else:
                if i == 0:
                    max_left = nums2[j-1]
                elif j == 0:
                    max_left = nums1[i - 1]
                else:
                    max_left = max(nums1[i - 1], nums2[j - 1])
                if (m + n) % 2 == 1:
                    return max_left
                if i == m:
                    min_right = nums2[j]
                elif j == n:
                    min_right = nums1[i]
                else:
                    min_right = min(nums1[i], nums2[j]) 
                return (max_left + min_right) / 2.0

    
    

if __name__ == '__main__':
    sln = Solution()
    x = [1]
    sln.findMedianSortedArrays(x,x)