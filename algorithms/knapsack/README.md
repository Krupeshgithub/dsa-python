***Knapsack Problem:***

There are many tree main problems int knapsack problem.

<blockquote>

1. 0/1 

2. Frictional

3. Unbound
</blockquote>

**Knapsack = Bag**

> - Problem Exaplaination: We have one bag, 4 items with weight and values. Now, put
items inside the bag but there are one condition, in the last we put values like 
we will make maximum profite.

> - What is 0/1?
Assume, our bag capacity is 10 kg and there are already 9 kg inside the bag.
we have only 1 kg left. so, there are two approach.
0 -> Nothing to put
1 -> Put item and remove lowest weight which not need.

> Note: But, for 0/1 condition we don't have permission to break the item.

```How to find that this is DP (Dynamic Problem)?```


There are two ways to find is this dynamic problem or not.
```
1. Choice
2. Optional (find max, value, min, etc...)
```

- In this problem we have choice to put any item.
Also, we make maxium profile for same problem.

- There are one single rule to solve any DP problem.
First, drow recursion problem. Then solve DP problem.
