
## Key takeways:
- The improved algorithm focuses on pruning flight loops rather than optimizing for maximum profits. The intuition comes from the fact that when two vertices lack a direct connection within the optimal solution, there must exist ideal flight loops that can connect them.
- The algorithm initiates with a greedy strategy, where the flight subset $H_{opt}$ is derived by intersecting both the profitable (also positive) flight loop subset and the subset obtained by removing unprofitable (also negative) flight loops. Both subsets are acquired through a greedy approach. We can substantiate that the edges within this flight subset $H_{opt}$ are also present in the optimal solution. Consequently, we can streamline the graph's edges using this technique and employ dynamic optimization to ascertain the optimal solution.

## Note:
- The current code does not precisely align with this concept, and I will address these improvements in the future.
- For readers, I recommend utilizing the ```flight-loop_gurobi.py``` script for small-scale datasets, as I have not yet fine-tuned the enhanced Dijkstra algorithm for speed.

## Algorithm Description: 
The algorithm comprises two main steps:
- Step One: Utilizing a greedy approach, we progressively assemble the set $H_1$ consisting of maximum-profitable loops from the original flight network. The algorithm halts when the maximum-profitable loop becomes negative. Similarly, we employ a greedy algorithm to iteratively construct the set $H'_2$ comprising all minimum non-profitable loops from the original flight network. The algorithm terminates when the minimum-profitable loop becomes positive. At this point, we obtain the set $H_2$ from the original flight network as $H_2 = \Omega - H'_2$. The enhanced Dijkstra algorithm can be employed for the greedy algorithms in this process.
- Step Two: We proceed by defining the following sets: $H_{opt} = H_1 \cap H_2$: The intersection of $H_1$ and $H_2$. $H_{retry} = H_1 \cap H_2 - Maximum_Loop(H_{opt})$: Obtained by subtracting the maximum loop from the intersection of $H_1$ and $H_2$. $H_{waitlist} = H_1 \cup H_2 - H_{maintain}$: Comprising loops not present in the set $H_{maintain}$, formed by uniting $H_1$ and $H_2$. $H_{try} = H_{try} \cup H_{waitlist}$: Adding $H_{waitlist}$ to $H_{try}$, effectively simplifying the graph's complexity. Subsequently, we extract all edges from $H_{retry}$ and employ dynamic optimization techniques to derive optimal solutions.

## Theoretical Analysis (To be completed in the future; the following outlines the basic concept):
Objective: To establish that the edges encompassed within the flight subset $H_{opt}$ are also part of the optimal solution.
Proof Sketch: Utilizing a proof by contradiction, let us assume that for vertices $v_1$ and $v_2$, edge $e_1$ exists in $H_{opt}$ while edge $e_2$ exists in $H_{opt_solution}$. We will demonstrate the validity of this assumption based on the following three points:
- $e_1 = e_2$: This can be deduced by employing the method of selecting the minimum loop.
- $e_1$ does not exist while $e_2$ exists: This can be deduced by employing the method of selecting the minimum loop.
- $e_2$ exists while $e_1$ does not: This can be deduced by employing the method of selecting the minimum loop.

In concluding this proof sketch, we aim to establish that the edges in $H_{opt}$ are integral components of the optimal solution, reinforcing the algorithm's effectiveness in selecting these edges.


---
## (中文)算法描述：
该算法分为两步：
- 第一步：使用贪心算法逐步从原航班图中取得由最大盈利环所构成的集合 $H_1$ ，算法停止于当最大盈利环为负数的时候；使用贪心算法逐步从原航班图中取得由最小非盈利环所有构成的集合$H^'_2$，算法停止于当最小盈利环为正数的时候，此时取原航班图集合 $H_2 = \Omega/H^'_2$。该过程的贪心算法都可使用改进后的Dijkstra算法实现。
- 第二步：取 $H_{opt} = H_1 \cap H_2$, $H_{retry} = H_1 \cap H_2 - Maxmimum_Loop\(H_{opt}\)$ , $H_{waitlist} = H_1 \cup H_2 - H_{maintain}$, $H_{try} = H_{try} \cup H_{waitlist}$, 此时可以有效的降低图的复杂程度。而后从$H_{retry}$中取所有边，使用动态优化得到optimal solutions.


## (中文)理论分析：(留待未来做完整，下面仅描述基本思路)
Target: The edges within this flight subset $H_{opt}$ are also present in the optimal solution. 
proof sketch： 反证法，假设对于顶点 $v_1$,$v_2$ 之间的边 $e_1$ 在 $H_{opt}$ 内, $e_2$ 在$H_{opt_solution}$ 内，从下面三点出发进行说明：
1) $e_1 = e_2$：可由取最小环的方法说明得到
2) $e_1$ 不存在而 $e_2$ 存在：可由取最小环的方法说明得到
3) $e_2$ 存在而 $e_1$ 不存在：可由取最大环的方法说明得到

