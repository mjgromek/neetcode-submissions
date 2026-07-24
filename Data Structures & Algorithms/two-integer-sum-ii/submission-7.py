class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(numbers)):
            seen[numbers[i]] = i + 1
            compliment = target - numbers[i]
            if compliment in seen and seen[compliment] != i + 1:
                return [seen[compliment],i + 1]