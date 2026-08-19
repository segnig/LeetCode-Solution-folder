class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        total = 2 * n
        
        reserved_seats = defaultdict(list)

        for row, seat_num in reservedSeats:
            reserved_seats[row].append(seat_num)

        
        for row in reserved_seats:

            first_group, second_group = True, True
            for seat in reserved_seats[row]:
                if 2 <= seat <= 5:
                    first_group = False
                if 6 <= seat <= 9:
                    second_group = False
            
            if first_group or second_group:
                total -= int(not second_group) + int(not first_group)

            if not first_group and not second_group:
                middle_group = True
                for seat in reserved_seats[row]:
                    if 4 <= seat <= 7:
                        middle_group = False
                
                if middle_group:
                    total -= 1
                else:
                    total -= 2

        return total