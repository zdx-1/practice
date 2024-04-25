
"""
链表
"""
# #可以快速插入，删除元素，用于存储元素
# #每个节点维护两个部分：数据域和指针域
# #链表维护head和tail，每次从tail处插入新元素
# """在python中常用list，一般不需要再特别写链表，但是有需要，下面是一个符合情况的模板"""
# class Node:#节点类
#     def __init__(self,data) -> None:
#         self.data=data#数据
#         self.next=None#指针
# class LinkList:
#     def __init__(self,node) -> None:
#         self.head=node
#         self.tail=self.head
#     def insert(self,data):
#         self.tail.next=Node(data)
#         self.tail=self.tail.next
#     def print(self):
#         cur=self.head
#         while cur!=None:
#             print(cur.data)
#             cur=cur.next
# a=LinkList(Node(1))#头节点构建一个链表
# a.insert(2)
# a.insert(3)
# a.insert(4)
# a.insert(5)
# a.print()


n=int(input())
s=input()
a=[]
isT=True
for i in s:
    if i=='(':
        a.append(i)
    else:
        if len(a)==0:
            break
        a.pop()
