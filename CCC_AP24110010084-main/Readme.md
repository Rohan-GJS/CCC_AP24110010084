#  Smart Resource Allocation System (Greedy + Dynamic Programming)

##  Overview

The **Smart Resource Allocation System** is a terminal-based Python project that demonstrates and compares two important algorithmic approaches:

* **Greedy Algorithm**
* **Dynamic Programming (0/1 Knapsack Problem)**

The system allows users to input items with values and weights, and a maximum capacity. It then computes the best selection of items using both approaches and compares the results.

---

##  Objectives

* Demonstrate the working of **Greedy and DP algorithms**
* Compare **optimal vs approximate solutions**
* Provide a **hands-on understanding** of algorithm efficiency
* Build a **terminal-based application** suitable for lab exams

---

##  Features

* User input for items (name, value, weight)
* Displays item list in tabular format
* Implements:

  * Greedy approach (value/weight ratio)
  * Dynamic Programming approach (Knapsack)
* Shows:

  * Selected items
  * Total value
* Compares both approaches

---

##  Algorithms Used

###  Greedy Algorithm

* Selects items based on the highest **value-to-weight ratio**
* Fast and efficient
* Does not always give optimal result

###  Dynamic Programming (0/1 Knapsack)

* Considers all possible combinations
* Guarantees optimal solution

**DP Formula:**
dp[i][w] = max(dp[i-1][w], value[i] + dp[i-1][w - weight[i]])

---

##  Project Structure

```
project/
 └── main.py
```

---

##  How to Run

### 1. Clone or Download

```
git clone <your-repo-link>
cd project
```

### 2. Run the Program

```
python main.py
```

---

## 📥 Sample Input

```
Enter number of items: 3

Item 1:
Name: A
Value: 60
Weight: 10

Item 2:
Name: B
Value: 100
Weight: 20

Item 3:
Name: C
Value: 120
Weight: 30

Enter total capacity: 50
```

---

## 📤 Sample Output

```
Greedy Approach:
Selected Items: ['A', 'B']
Total Value: 160

Dynamic Programming Approach:
Selected Items: ['B', 'C']
Total Value: 220
```

---

##  Comparison

| Approach | Result Type | Performance | Accuracy           |
| -------- | ----------- | ----------- | ------------------ |
| Greedy   | Approximate | Fast        | Not Always Optimal |
| DP       | Optimal     | Slower      | Always Optimal     |

---

##  Time Complexity

* **Greedy:** O(n log n)
* **Dynamic Programming:** O(n × capacity)

---

##  Learning Outcomes

* Understanding of **Greedy vs DP**
* Implementation of **Knapsack problem**
* Algorithm comparison and analysis
* Practical coding for exams and viva

---

##  Viva Explanation (Short)

This project compares Greedy and Dynamic Programming approaches for solving the Knapsack problem. The Greedy method provides a fast solution based on local optimization, while Dynamic Programming ensures a globally optimal solution by evaluating all possibilities.

---

##  Future Enhancements

* Add menu-driven interface
* Save results to file
* Visualize DP table
* Add execution time comparison

---

##  Author

Teja Ganugula

---

##  License

This project is for educational purposes.