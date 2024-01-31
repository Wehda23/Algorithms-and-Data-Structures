class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        frequency_counter = {key: 0 for key in range(0, len(nums))}

        for number in nums:
            if number in frequency_counter.keys():
                frequency_counter[number] += 1
        print(frequency_counter)
        missing: int = None

        for key, value in frequency_counter.items():
            if value == 0:
                missing = key
                break

        print(missing)
        return missing


Solution().missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1])
