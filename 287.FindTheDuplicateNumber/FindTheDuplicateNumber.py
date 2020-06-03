 #Binary search
        low = 0
        high = len(nums) - 1
        while(low <= high):
            count = 0
            mid = low + (high-low) // 2
            for n in nums:
                if n <= mid:
                    count += 1

            if count > mid:
                high = mid - 1
            else:
                low = mid + 1

        return low
