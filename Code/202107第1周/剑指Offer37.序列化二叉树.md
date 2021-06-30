<!--
 * @Description: 
 * @Autor: Au3C2
 * @Date: 2021-06-30 10:10:25
 * @LastEditors: Au3C2
 * @LastEditTime: 2021-06-30 10:13:08
-->
# [剑指 Offer 37. 序列化二叉树](https://leetcode-cn.com/problems/xu-lie-hua-er-cha-shu-lcof/)

请实现两个函数，分别用来序列化和反序列化二叉树。

你需要设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。

**提示：**输入输出格式与 LeetCode 目前使用的方式一致，详情请参阅 [LeetCode 序列化二叉树的格式](https://leetcode-cn.com/faq/#binary-tree)。你并非必须采取这种方式，你也可以采用其他的方法解决这个问题。

 

**示例：**

![img](https://assets.leetcode.com/uploads/2020/09/15/serdeser.jpg)

```
输入：root = [1,2,3,null,null,4,5]
输出：[1,2,3,null,null,4,5]
```


注意：本题与主站 297 题相同：https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/

树 困难

和 [0297.二叉树的序列化与反序列化](../Code/202103第4周/0297.二叉树的序列化与反序列化.md) 相同

# 代码

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root: return
        queue = collections.deque()
        queue.append(root)
        res = []
        while queue:
            size = len(queue)
            # level = list()
            for _ in range(size):
                cur = queue.popleft()
                if not cur:
                    continue
                res.append(cur.val)
                if not cur.left and cur.val != None:
                    cur.left = TreeNode(None)
                if not cur.right and cur.val != None:
                    cur.right = TreeNode(None)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        while res[-1] == None:
            res.pop()
        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data: return
        n = len(data)
        queue = deque()
        queue.append(TreeNode(data[0]))
        res = queue[0]
        if n == 1: return res
        i = 1
        while queue:
            size = len(queue)
            level = deque()
            for _ in range(size):
                cur = queue.popleft()
                if data[i] != None:
                    t = TreeNode(data[i])
                    cur.left = t
                    level.append(t)
                i += 1
                if i == n:
                    return res
                if data[i] != None:
                    t = TreeNode(data[i])
                    cur.right = t
                    level.append(t)
                i += 1
                if i == n:
                    return res
            queue = level
        return res
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
```
