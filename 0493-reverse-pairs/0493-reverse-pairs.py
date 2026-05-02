class Solution:
    def reversePairs(self, nums):
        
        self.count = 0

        def merge(arr):
            if len(arr) > 1:

                mid = len(arr) // 2

                left = arr[:mid]
                right = arr[mid:]

                merge(left)
                merge(right)

                # Count reverse pairs
                rp = 0

                for lp in range(len(left)):

                    while rp < len(right) and left[lp] > 2 * right[rp]:
                        rp += 1

                    self.count += rp

                # Merge step
                lp = 0
                rp = 0
                fp = 0

                while lp < len(left) and rp < len(right):

                    if left[lp] <= right[rp]:
                        arr[fp] = left[lp]
                        lp += 1
                    else:
                        arr[fp] = right[rp]
                        rp += 1

                    fp += 1

                while lp < len(left):
                    arr[fp] = left[lp]
                    lp += 1
                    fp += 1

                while rp < len(right):
                    arr[fp] = right[rp]
                    rp += 1
                    fp += 1

        merge(nums)

        return self.count