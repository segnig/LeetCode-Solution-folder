class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(position[i], speed[i]) for i in range(len(speed))]
        cars.sort(reverse=True)

        cars = [(target - cars[i][0])/ cars[i][1] for i in range(len(speed))]
     
        stack = []
        for car in cars:
            if not stack:
                stack.append(car)
            elif  stack[-1] < car:
                stack.append(car)    
        return len(stack)   