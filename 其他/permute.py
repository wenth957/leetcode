from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        sum_path = 0

        def dfs(candidates, target, start_index):
            nonlocal sum_path
            if sum_path > target:
                return
            if sum_path == target:
                res.append(path[:])
                return

            for i in range(start_index, len(candidates)):
                path.append(candidates[i])
                sum_path += i
                dfs(candidates, target, i + 1)
                sum_path -= i
                path.pop()
        dfs(candidates, target, 0)
        return res


s = Solution()
print(s.combinationSum([2, 2, 3, 7], 7))
