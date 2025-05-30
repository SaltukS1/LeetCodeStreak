class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # Ensure nums1 is the shorter array to optimize the algorithm
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        left, right = 0, m
        
        while left <= right:
            
            partition1 = (left + right) // 2
            partition2 = (m + n + 1) // 2 - partition1
        
            maxLeft1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            minRight1 = float('inf') if partition1 == m else nums1[partition1]
            maxLeft2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            minRight2 = float('inf') if partition2 == n else nums2[partition2]
            
           
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
               
                if (m + n) % 2 == 1:
                    return max(maxLeft1, maxLeft2)
          
                return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2.0
          
            elif maxLeft1 > minRight2:
                right = partition1 - 1
            else:
                left = partition1 + 1
        
        return 0.0  

if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    print(solution.findMedianSortedArrays([1,3], [2]))  
    
   
    print(solution.findMedianSortedArrays([1,2], [3,4])) 