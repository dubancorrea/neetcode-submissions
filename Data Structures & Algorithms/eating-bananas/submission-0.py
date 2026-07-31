class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo = 1 # this is going to be the smalles eating rate
        hi = max(piles)  # the largest possible eating rate / like "eat biggest pile in an hour"

        while lo < hi: #do the binary search over possible values of k
            mid = (lo + hi) // 2  # candidate eating rate to test

            hours = 0 
            for pile in piles:
                hours += math.ceil( pile / mid) # hours needed to finish this pile at rate mid

            if hours <= h:  #mid is fast enough to finish in time
                hi = mid
            else:                  # mid is to slow, takes too many hours
                lo = mid +1 # need a faster rate
        return lo


    