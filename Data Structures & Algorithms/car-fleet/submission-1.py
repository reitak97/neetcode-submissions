class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(position)):
            cars.append([position[i],speed[i]])

        cars.sort(reverse=True)

        stack = []
        for pos,speed in cars:
            time = (target-pos) / speed
            if stack and stack[-1] >= time:
                continue

            else:
                stack.append(time)


        return len(stack)
        
