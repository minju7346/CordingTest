class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        a = [0]*n
        for i in range(n):
                    a[(i+k)%n] = nums[i] #전체 크기로 %연산하면 out of index를 피할 수 있음
        nums[:] = a #주소복사가 아닌 배열 전체가 복사되는 방법