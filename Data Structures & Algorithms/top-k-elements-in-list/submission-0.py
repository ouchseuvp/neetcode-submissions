class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        # bucket[f] = числа, встретившиеся ровно f раз
        bucket = [[] for _ in range(len(nums) + 1)]
        for num, freq in count.items():
            bucket[freq].append(num)

        res = []
        for f in range(len(bucket) - 1, 0, -1):
            for num in bucket[f]:
                res.append(num)
                if len(res) == k:
                    return res
        return res