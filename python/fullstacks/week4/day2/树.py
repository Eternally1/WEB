# @author: "QiuJunan"
# @date: 2018/3/28 15:39
import queue

class Bitree(object):
    """编写一些树相关的方法"""
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

    def tree_depth(self,tree):
        """
        计算树的深度
        :param tree: 树
        :return:
        """
        if not tree:
            return 0
        else:
            # 使用递归来求解树的深度
            left_depth = self.tree_depth(tree.left)
            right_depth = self.tree_depth(tree.right)
            if left_depth > right_depth:
                return left_depth+1
            else:
                return right_depth+1

    def tree_depth_min(self,tree):
        """计算树的最小深度,和计算树的深度，只需修改一下小于符号即可"""
        if not tree:
            return 0
        else:
            # 使用递归来求解树的深度
            left_depth = self.tree_depth(tree.left)
            right_depth = self.tree_depth(tree.right)
            if left_depth < right_depth:
                return left_depth+1
            else:
                return right_depth+1
            # 下面这个也可行
            # if left_depth == 0 or right_depth ==0:
            #     return left_depth+right_depth+1
            # else:
            #     return min(left_depth,right_depth)+1

    def get_tree_width(self,tree):
        """
        求树的宽度，使用一个队列来，在上一层遍历完成之后，将下一层所有节点放入进去，即可得到最大宽度
        :param tree:
        :return:
        """
        max_width = 0
        q = queue.Queue()
        q.put(tree)
        while not q.empty():    # 当树不为空的时候
            cur_width = q.qsize() # 获取当前层的节点数
            # 遍历当前层的结点，看每一个结点有几个子节点，从而进行入队，进而得到节点个数
            for i in range(cur_width):   # 如果当前层还有节点
                node = q.get()
                cur_width -=1
                if node.left:
                    q.put(node.left)
                    cur_width += 1
                if node.right:
                    q.put(node.right)
                    cur_width +=1
            if cur_width > max_width:
                max_width = cur_width

        return max_width

    def post_order(self,tree):
        if tree:
            self.post_order(tree.left)
            self.post_order(tree.right)
            print(tree.data,'->',end=" ")
        else:
            return


# 每一个结点都要是一些Bitree的实例对象
tree = Bitree('D',Bitree('B',Bitree('A'),Bitree('C')),Bitree('E',Bitree('F')))
depth = tree.tree_depth(tree)
min_depth = tree.tree_depth_min(tree)
max_width = tree.get_tree_width(tree)
print(depth,min_depth,max_width)
print("后续遍历：")
tree.post_order(tree)


