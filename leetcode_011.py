class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1

        #capacity = (right - left) * min(height[right], height[left])
        maxarea = 0 

        while right > left:
            capacity = (right - left) * min(height[right], height[left])
            if capacity > maxarea:
                maxarea = capacity
            if height[right] > height[left]:
                left += 1
            else: #height[right] < height[left]:
                right -= 1
                
        return maxarea

if __name__ == '__main__':
    sln = Solution()
    print sln.maxArea([7,15,3,10,5,7])