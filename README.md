# Airline_Fleet_Allocation-for_unprofitable_flight_deletion
The repository focuses on Airline Fleet Allocation with a primary emphasis on unprofitable flight deletion. Within this repository, you will find code for solving this problem using the Gurobi solver and an improved Dijkstra algorithm to efficiently remove non-profitable airline cycles.

## Files

- flight-loop_new_gurobi.py: Gurobi solver code for solving the airline fleet allocation problem
- preprocess.py: preprocesses the data into graph
- optimization.py: improved Dijkstra algorithm to efficiently remove non-profitable airline cycles
- main_optimization.py: main file for running the optimization

## Notes

- The improved Dijkstra algorithm may not achieve optimal performance, as it cannot handle cases where two vertices are not connected in the optimal solution.
- 