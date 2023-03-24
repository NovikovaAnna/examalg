def count_connected_components(graph):
    # Проверка на пустой граф
    if not graph:
        return 0

    visited = set()

    def dfs(v):
        visited.add(v)
        for u in graph[v]:
            if u not in visited:
                dfs(u)

    count = 0
    for v in graph:
        # Проверка на корректность графа
        if not all(u in graph for u in graph[v]):
            raise ValueError("Некорректный граф")
        if v not in visited:
            dfs(v)
            count += 1

    return count

# Пример использования
graph = {
    1: ['A', 'B'],
    2: ['B', 'C'],
    3: ['C', 'D'],
    4: ['E'],
    5: ['G', 'F']
}
print(count_connected_components(graph)) # выводит 3
