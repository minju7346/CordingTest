class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a = [str(i) for i in digits]
        a = str(int(''.join(a)) + 1)
        return list(map(int, a))