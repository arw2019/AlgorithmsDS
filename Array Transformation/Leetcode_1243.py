class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        while True:
            cnt = False
            newArr = arr.copy()
            for i in range(1,len(arr)-1):
                if arr[i-1] > arr[i] and arr[i] < arr[i+1]:
                    newArr[i] += 1
                    cnt = True
                elif arr[i-1] < arr[i] and arr[i] > arr[i+1]:
                    newArr[i] -= 1
                    cnt = True
            if not cnt: 
                break
            arr = newArr
        return arr
