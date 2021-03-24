
class Solution:
    def __init__(self,jewels,stones):
        self.jewels = jewels
        self.stones = stones
    def numJewelsInStones(jewels,stones):
        count = 0
        for a in range(len(jewels)):
            for A in range(len(stones)):
                if jewels[a] == stones[A]:
                    count += 1
        return count

print(Solution.numJewelsInStones(input (f"enter jewels " ),input("enter stones")))



