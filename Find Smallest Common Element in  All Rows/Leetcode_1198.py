from bisect import bisect_left
class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        def helper(row_idx: int, target: int) -> bool:
            """
            use binary search to check if element present
            O(len(row)) time complexity
            pass row index rather than entire row to helper function
            """
            idx = bisect_left(mat[row_idx], target)
            return idx < len(mat[0]) and mat[row_idx][idx]==target
        for num in mat[0]:
            if all([helper(row_idx, num) for row_idx in range(len(mat))]):
                return num
        return -1
    
# ***********
# from bisect import bisect_left
# class Solution:
#     def smallestCommonElement(self, mat: List[List[int]]) -> int:
#         def helper(row: List[int], target: int) -> bool:
#             """
#             use binary search to check if element present
#             O(len(row)) time complexity
#             """
#             idx = bisect_left(row, target)
#             return idx < len(row) and row[idx]==target
#         for num in mat[0]:
#             if all([helper(row, num) for row in mat]):
#                 return num
#         return -1

# ***********
# from collections import Counter
# class Solution:
#     """
#     brute force solution
#     load all the elements into a Counter and find smallest element that occurs in every row
#     """
#     def smallestCommonElement(self, mat: List[List[int]]) -> int:
#         cnt = Counter()
#         for row in mat:
#             for num in row:
#                 cnt[num]+=1
#         for num in sorted(cnt.keys()):
#             if cnt[num]==len(mat):
#                 return num
#         return -1
