class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        people = [0] * num_people
        candies_left = candies
        n = 1
        while(candies_left > 0):
            for i in range(len(people)):
                if n <= candies_left:
                    people[i] += n
                    candies_left -= n
                else:
                    people[i] += candies_left
                    candies_left = 0
                n += 1

        return people
                
