# https://www.codewars.com/kata/52bef5e3588c56132c0003bc/

def tree_by_levels(node):
    if node is None:
        return []
    result = []
    queue = [node]
    while queue:
        node = queue.pop(0)
        result.append(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result