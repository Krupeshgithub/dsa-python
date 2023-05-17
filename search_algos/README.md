# Searching Algorithms

1) Binary Search
2) Exponential Search 
3) Jump Search
4) Interpolation Search

# Prerequisites:
 1. Python

# Time Complexity

  ```1) First case:
    Range = range(0, 100**4)
    findingKey = 90000009


    90000009                                           Time (Second)
    /--------Binary Search Algorithm------------/ 0.0022661685943603516

    90000009
    /--------Jump Search------------/ 1.2163197994232178

    90000009
    /--------Exponential Search------------/ 7.807981014251709

    90000009
    /--------Interpolation Search------------/ 0.0001239776611328125

    2) Second case:
    Range = range(0, 100**4)
    findingKey = 80000000

    80000000
    /--------Binary Search Algorithm------------/ 5.0067901611328125e-05

    80000000
    /--------Jump Search------------/ 0.0609278678894043

    80000000
    /--------Exponential Search------------/ 7.853741884231567

    80000000
    /--------Interpolation Search------------/ 7.414817810058594e-05
