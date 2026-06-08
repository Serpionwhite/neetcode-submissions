class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:

        total_customers = len(customers)
        current_time = 0
        wait_time = 0


        for index in range(total_customers):
            arrival_time = customers[index][0]

            prep_time = customers[index][1]
            current_time = max(current_time, arrival_time) + prep_time
            wait_time += current_time - arrival_time

        return wait_time / total_customers
        