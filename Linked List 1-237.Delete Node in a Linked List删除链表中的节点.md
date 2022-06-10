---

---

# Linked List 1-237.Delete Node in a Linked List删除链表中的节点

Write a function to ==**delete a node**== in a singly-linked list. You will **not** be given access to the `head` of the list, instead you will be given access to **the node to be deleted** directly.

It is **guaranteed** that the node to be deleted is **not a tail node** in the list.



![img](https://img-blog.csdnimg.cn/c54e6d462f01480cae9cf42c233325df.png)![点击并拖拽以移动](data:image/gif;base64,R0lGODlhAQABAPABAP///wAAACH5BAEKAAAALAAAAAABAAEAAAICRAEAOw==)编



请编写一个函数，用于 ==**删除单链表**==中某个特定节点 。在设计函数时需要注意，你无法访问链表的头节点 head ，只能直接访问 要被删除的节点 。

题目数据保证需要删除的节点 不是末尾节点 。



方法一:**和下一个节点交换**
删除链表中的节点的常见的方法是定位到待删除节点的上一个节点，修改上一个节点的next指针，使其指向待删除节点的下一个节点，即可完成删除操作。
这道题中，传入的参数node为要被删除的节点，无法定位到该节点的上一个节点。注意到要被删除的节点不是链表的末尾节点，因此 node.next 不为空，可以通过对node和node.neat进行操作实现删除节点。
在给定节点node的情况下，可以通过修改node的nezt 指针的指向，删除node的下一个节点。但是题目要求删除node，为了达到删除node的效果，只要在删除节点之前，将node的节点值修改为node.next 的节点值即可。
例如，给定链表4→5→1→9，要**被删除的节点是5**，即链表中的**第2个**节点。可以通过如下两步操作实现删除节点的操作。
1.将第2个节点的值修改为第3个节点的值，即将节点5的值修改为1，此时链表如下:
 		4→1→1→9

1. 删除第 3 个节点，此时链表如下：

​		4→1→9



```java
#既然不能先删除自己，那就把自己整容成儿子，再假装儿子养活孙子
```

```python
class Solution:
    def deleteNode(self, node):
	node.val = node.next.val #我们将要删除节点的 next 节点的值赋值给要删除的节点，转而去删除 next 节点，从而达成目的。
	node.next = node.next.next
```
