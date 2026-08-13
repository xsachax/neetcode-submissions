class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # find how much time it takes for each car to get to the finish
        # start by end of array, make way to front
        # as long as the time of a car is smaller than the bottom of the stack, that is a fleet
        # once a fleet is found, pop the whole stack and start the next fleet


        s = []
        times = []
        res = 0

        for i in range(len(position)):
            times.append((position[i], (target - position[i])/speed[i]))

        times.sort(reverse=True)

        for i in range(len(times)):
            if s and times[i][1] <= s[0][1]: # if car is faster than current fleet leader (s)
                s.append(times[i])
            else:
                while s:
                    s.pop()
                s.append(times[i]) #otherwise, clear the pile and start a new fleet
                res+=1

        return res

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # fleets = 0
        # pairs = list(zip(position, speed))
        # pairs.sort(reverse=True)
        # anchor = -1
        # for pair in pairs:
        #     t = (target-pair[0]) / pair[1]
        #     if t > anchor:
        #         fleets+=1
        #         anchor = t
        # return fleets
