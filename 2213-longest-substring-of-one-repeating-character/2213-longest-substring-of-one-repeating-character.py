from typing import List
from sortedcontainers import SortedList


class Solution:
    def longestRepeating(
        self,
        s: str,
        queryCharacters: str,
        queryIndices: List[int]
    ) -> List[int]:
        n = len(s)
        s = list(s)
        segs = SortedList()
        lens = SortedList()
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            segs.add((i, j - 1))
            lens.add(j - i)
            i = j
        ans = []
        for q in range(len(queryIndices)):
            pos = queryIndices[q]
            ch = queryCharacters[q]
            if s[pos] == ch:
                ans.append(lens[-1])
                continue
            idx = segs.bisect_right((pos, n)) - 1
            L, R = segs[idx]
            segs.pop(idx)
            lens.remove(R - L + 1)
            if L <= pos - 1:
                segs.add((L, pos - 1))
                lens.add(pos - L)
            if pos + 1 <= R:
                segs.add((pos + 1, R))
                lens.add(R - pos)
            newL = pos
            newR = pos
            if pos + 1 < n and s[pos + 1] == ch:

                idx2 = segs.bisect_left((pos + 1, -1))

                if (
                    idx2 < len(segs)
                    and segs[idx2][0] == pos + 1
                ):
                    rightL, rightR = segs[idx2]

                    lens.remove(rightR - rightL + 1)
                    segs.pop(idx2)

                    newR = rightR
            if pos > 0 and s[pos - 1] == ch:

                idx3 = segs.bisect_right((pos - 1, n)) - 1

                if (
                    idx3 >= 0
                    and segs[idx3][1] == pos - 1
                ):
                    leftL, leftR = segs[idx3]

                    lens.remove(leftR - leftL + 1)
                    segs.pop(idx3)

                    newL = leftL
            s[pos] = ch
            segs.add((newL, newR))
            lens.add(newR - newL + 1)
            ans.append(lens[-1])
        return ans