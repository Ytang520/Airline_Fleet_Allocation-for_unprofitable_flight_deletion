#  Airline Fleet Allocation for Unprofitable Flight Deletion Project
The repository focuses on Airline Fleet Allocation with a primary emphasis on unprofitable flight deletion. Within this repository, you will find code for solving this problem using the Gurobi solver and an improved Dijkstra algorithm to efficiently remove non-profitable airline cycles.

## Files

- flight-loop_gurobi.py: Gurobi solver code for solving the airline fleet allocation problem
- preprocess.py: preprocesses the data into graph
- optimization.py: improved Dijkstra algorithm to efficiently remove non-profitable airline cycles
- main_optimization.py: main file for running the optimization

## Notes

- While the enhanced Dijkstra algorithm offers improvements, it may not consistently deliver optimal performance. This limitation arises when the algorithm encounters scenarios where two vertices lack a direct connection within the optimal solution. For optimal results, I recommend utilizing the ```flight-loop_gurobi.py``` script for small-scale datasets, as I have not yet fine-tuned the enhanced Dijkstra algorithm for speed.
_**Please refer to the ```Analysis_algorithm.md document``` for detailed information.**_


**Update 20230916**

- It is essential to note that the improved algorithm focuses on pruning flight loops rather than optimizing for maximum profits. Please refer to ```Analysis_algorithm.md``` for detaied information.