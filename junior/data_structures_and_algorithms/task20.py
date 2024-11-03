### 10. **Function that returns the maximum depth (or height) of a binary tree**

def max_depth(tree):
    if not tree:
        return 0
    return 1 + max(max_depth(tree[1]), max_depth(tree[2]))


from collections import deque


def max_depth2(tree):
    if not tree:
        return 0
    queue = deque([tree])
    depth = 0
    while queue:
        depth += 1
        for _ in range(len(queue)):
            node = queue.popleft()
            if node[1]:
                queue.append(node[1])
            if node[2]:
                queue.append(node[2])
    return depth

def max_depth3(tree):
    stack = [(tree, 1)]
    max_depth = 0
    while stack:
        node, depth = stack.pop()
        if node:
            max_depth = max(max_depth, depth)
            stack.append((node[1], depth + 1))
            stack.append((node[2], depth + 1))
    return max_depth
