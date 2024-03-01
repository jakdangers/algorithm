def solution(parking):
    # 부모 노드인 경우를 제외
    def is_parent(tree, parent, child):
        while child in tree:
            if tree[child] == parent:
                return True
            child = tree[child]
        return False

    tree = {}
    for i, (left, right) in enumerate(parking):
        if left != -1:
            tree[left] = i
        if right != -1:
            tree[right] = i

    count = 0
    for i in range(len(parking)):
        for j in range(i + 1, len(parking)):
            if not (is_parent(tree, i, j) or is_parent(tree, j, i)):
                count += 1

    return count