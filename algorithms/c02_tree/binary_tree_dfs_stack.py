import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from algorithms.models import TreeNode, list_to_tree, print_tree


def pre_order_stack(root: TreeNode | None) -> list[int]:
    """使用栈实现前序遍历"""
    if root is None:
        return []

    stack = [root]
    result = []

    while stack:
        node = stack.pop()
        result.append(node.val)

        # 先压入右子节点，再压入左子节点
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return result


def in_order_stack(root: TreeNode | None) -> list[int]:
    """使用栈实现中序遍历"""
    stack = []
    result = []
    current = root

    while current or stack:
        # 遍历到最左侧节点
        while current:
            stack.append(current)
            current = current.left

        # 访问节点并转向右子树
        current = stack.pop()
        result.append(current.val)
        current = current.right

    return result


def post_order_stack(root: TreeNode | None) -> list[int]:
    """使用栈实现后序遍历"""
    if root is None:
        return []

    stack = [root]
    result = []

    while stack:
        node = stack.pop()
        result.append(node.val)

        # 先压入左子节点，再压入右子节点
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    # 反转结果得到后序遍历序列
    return result[::-1]


"""Driver Code"""
if __name__ == "__main__":
    # 初始化二叉树
    arr = [1, 2, 3, 4, 5, 6, 7]
    root = list_to_tree(arr)
    print("\n初始化二叉树\n")
    print_tree(root)

    # 前序遍历
    print("\n前序遍历的节点序列 = ", pre_order_stack(root))

    # 中序遍历
    print("\n中序遍历的节点序列 = ", in_order_stack(root))

    # 后序遍历
    print("\n后序遍历的节点序列 = ", post_order_stack(root))
