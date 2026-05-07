class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        mstack = []
        res = [0]*len(temperatures)

        for i in range(len(temperatures)):
            while mstack and temperatures[mstack[-1]]<temperatures[i]:
                res[mstack[-1]] = i-mstack[-1]
                mstack.pop()
            mstack.append(i)

        return res