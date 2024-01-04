```
Constant: O(1)
Linear time: O(n)
Logarithmic time: O(n log n)
Quadratic time: O(n^2)
Exponential time: O(2^n)
Factorial time: O(n!)
```

Time complexity is a concept in computer science that deals with the quantification of the 
amount of time taken by a set of code or algorithm to process or run as a function of the 
amount of input. In other words, time complexity is essentially efficiency, or how long a program function takes to process a given input.

Here are some steps to calculate time complexity:

1. Identify the operations: The first step is to identify the operations that contribute to 
the time complexity. This could be arithmetic operations, comparisons, looping control structures, or function calls.

2. Count the operations: Next, count the number of each operation. This is often where the 
input size comes in - for example, if you're looping over an array of length n, you might perform n operations.

3. Express in terms of n: Express the number of operations as a function of n. This is your time complexity.

4. Simplify: Finally, simplify your time complexity to the highest order term. This is because, for large inputs, 
lower order terms and constants become insignificant. For example, if your time complexity is 3n^2 + 2n + 1, you 
would simplify this to O(n^2).

Here are some common time complexities, from fastest to slowest:

O(1): Constant time complexity. The running time does not change with the size of the input.
O(log n): Logarithmic time complexity. The running time grows logarithmically in proportion to the input size.
O(n): Linear time complexity. The running time grows linearly with the input size.
O(n log n): Quasilinear time complexity. The running time grows linearly and logarithmically.
O(n^2): Quadratic time complexity. The running time grows exponentially for each addition to the input data set.
O(2^n): Exponential time complexity. The growth doubles with each addition to the input data set.
O(n!): Factorial time complexity. The running time grows factorially, making it the slowest and least efficient of all.
Remember, calculating time complexity is an estimation of efficiency, not an exact measurement. It doesn't tell you the 
exact speed of your code, but it gives you an idea of how your code scales with increasing input size.

