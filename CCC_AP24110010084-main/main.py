def greedy_knapsack(items, capacity):
    # Sort items based on value/weight ratio
    items_sorted = sorted(items, key=lambda x: x['value']/x['weight'], reverse=True)

    total_value = 0
    selected_items = []

    for item in items_sorted:
        if capacity >= item['weight']:
            capacity -= item['weight']
            total_value += item['value']
            selected_items.append(item['name'])

    return total_value, selected_items


def dp_knapsack(items, capacity):
    n = len(items)

    # Create DP table
    dp = [[0]*(capacity+1) for _ in range(n+1)]

    # Build table
    for i in range(1, n+1):
        value = items[i-1]['value']
        weight = items[i-1]['weight']

        for w in range(capacity+1):
            if weight <= w:
                dp[i][w] = max(dp[i-1][w], value + dp[i-1][w-weight])
            else:
                dp[i][w] = dp[i-1][w]

    # Backtrack to find selected items
    w = capacity
    selected_items = []

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selected_items.append(items[i-1]['name'])
            w -= items[i-1]['weight']

    selected_items.reverse()

    return dp[n][capacity], selected_items


def take_input():
    items = []

    n = int(input("Enter number of items: "))

    for i in range(n):
        print(f"\nItem {i+1}:")
        name = input("Enter item name: ")
        value = int(input("Enter value: "))
        weight = int(input("Enter weight: "))

        items.append({
            'name': name,
            'value': value,
            'weight': weight
        })

    capacity = int(input("\nEnter total capacity: "))

    return items, capacity


def display_items(items):
    print("\nItems List:")
    print("---------------------------------")
    print("Name\tValue\tWeight")
    print("---------------------------------")

    for item in items:
        print(f"{item['name']}\t{item['value']}\t{item['weight']}")

    print("---------------------------------")


def main():
    print("====== SMART RESOURCE ALLOCATION SYSTEM ======")

    items, capacity = take_input()

    display_items(items)

    print("\nRunning Greedy Algorithm...")
    g_value, g_items = greedy_knapsack(items, capacity)

    print("\nRunning Dynamic Programming...")
    d_value, d_items = dp_knapsack(items, capacity)

    print("\n====== RESULTS ======")

    print("\nGreedy Approach:")
    print("Selected Items:", g_items)
    print("Total Value:", g_value)

    print("\nDynamic Programming Approach:")
    print("Selected Items:", d_items)
    print("Total Value:", d_value)

    print("\n====== COMPARISON ======")
    if d_value > g_value:
        print("DP gives better (optimal) result than Greedy.")
    elif d_value == g_value:
        print("Both give same result.")
    else:
        print("Greedy performed better (rare case).")


if __name__ == "__main__":
    main()