import heapq

def read_map():
    """دریافت نقشه از کاربر"""
    m, n = map(int, input("Enter map dimensions (m n): ").split())
    print(f"Enter the {m}x{n} map row by row (space-separated values):")
    grid = []
    for _ in range(m):
        row = list(map(int, input().split()))
        grid.append(row)
    return grid, m, n

def is_valid_move(x, y, m, n, grid):
    """بررسی اعتبار حرکت به نقطه جدید"""
    return 0 <= x < m and 0 <= y < n and grid[x][y] in [1, 3, 17]

def a_star(grid, start, goal, m, n):
    """الگوریتم A* برای پیدا کردن مسیر بهینه"""
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # حرکت به چهار جهت
    open_set = []
    heapq.heappush(open_set, (0, start))  # (اولویت، نقطه)
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            return reconstruct_path(came_from, current)

        for dx, dy in directions:
            neighbor = (current[0] + dx, current[1] + dy)

            if not is_valid_move(neighbor[0], neighbor[1], m, n, grid):
                continue

            tentative_g_score = g_score[current] + 1

            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return None  # اگر مسیری یافت نشد

def heuristic(a, b):
    """محاسبه فاصله منهتن برای تخمین هزینه"""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def reconstruct_path(came_from, current):
    """بازسازی مسیر از دیکشنری came_from"""
    path = []
    while current in came_from:
        path.append(current)
        current = came_from[current]
    path.append(current)
    return path[::-1]  # مسیر معکوس

def print_map_with_path(grid, path):
    """نمایش نقشه با مسیر مشخص شده"""
    path_set = set(path)
    for i, row in enumerate(grid):
        for j, value in enumerate(row):
            if (i, j) in path_set:
                print("*", end=" ")  # علامت مسیر
            else:
                print(value, end=" ")
        print()

def main():
    grid, m, n = read_map()
    start = tuple(map(int, input("Enter start point (x y): ").split()))
    goal = tuple(map(int, input("Enter goal point (x y): ").split()))

    if not is_valid_move(start[0], start[1], m, n, grid) or not is_valid_move(goal[0], goal[1], m, n, grid):
        print("Invalid start or goal point.")
        return

    path = a_star(grid, start, goal, m, n)

    if path:
        print("Path found:", path)
        print("Map with path:")
        print_map_with_path(grid, path)
    else:
        print("No path found.")

if __name__ == "__main__":
    main()



"""

5 5
1 1 1 2 1
3 2 1 2 1
1 1 1 1 1
2 1 17 17 1
1 1 1 3 1

شروع: 0 0
مقصد: 4 4


-----------------------


6 6
1 3 3 3 3 1
1 2 2 2 3 1
1 1 1 2 3 1
2 2 1 1 1 1
1 1 17 17 1 3
1 1 1 1 1 1


شروع: 0 0
مقصد: 5 5


-----------------------------
7 7
1 1 1 1 1 1 1
1 2 2 2 1 17 1
1 3 3 3 1 17 1
1 3 2 2 1 1 1
1 1 1 1 1 3 1
1 17 17 17 1 3 1
1 1 1 1 1 1 1



شروع: 0 0
مقصد: 6 6


---------------------------------
8 8
1 1 1 1 1 1 1 1
1 2 2 2 3 3 1 1
1 2 1 1 1 3 1 17
1 3 1 17 1 3 1 17
1 3 1 17 1 1 1 1
1 1 1 1 1 2 2 1
1 17 17 17 1 1 1 1
1 1 1 1 1 1 1 1


شروع: 0 0
مقصد: 7 7
---------------------------------

10 10
1 1 1 1 1 1 1 1 1 1
1 17 17 17 1 1 3 3 3 1
1 3 3 17 1 1 1 1 3 1
1 17 1 17 1 17 17 1 3 1
1 17 1 1 1 17 3 1 1 1
1 1 1 1 1 1 3 1 1 1
1 1 17 17 17 1 3 1 1 1
1 1 1 1 1 1 3 3 3 1
1 1 1 1 17 17 17 1 1 1
1 1 1 1 1 1 1 1 1 1


شروع: 0 0
مقصد: 9 9



"""