

/*
 * @lc app=leetcode.cn id=641 lang=java
 *
 * [641] 设计循环双端队列
 */

// @lc code=start
class MyCircularDeque{
    int limit;
    int size;
    Node hNode;
    /** Initialize your data structure here. Set the size of the deque to be k. */
    public MyCircularDeque(int k) {
        limit = k;
        size = 0;
        hNode = null;
    }
    
    /** Adds an item at the front of Deque. Return true if the operation is successful. */
    public boolean insertFront(int value) {
        if (size == limit) return false;
        if (hNode == null) {
            hNode = new Node(value);
            hNode.pre = hNode;
            hNode.next = hNode;
            size ++;
            printArr();
            return true;
        } 
        Node node = new Node(value);
        node.next = hNode;
        node.pre = hNode.pre;
        hNode.pre.next = node;
        hNode.pre = node;
        hNode = node;
        size ++;
        printArr();
        return true;
    }   
    
    /** Adds an item at the rear of Deque. Return true if the operation is successful. */
    public boolean insertLast(int value) {
        if (size == limit) return false;
        if (hNode == null) {
            hNode = new Node(value);
            // hNode.val = value;
            hNode.pre = hNode;
            hNode.next = hNode;
            size ++;
            printArr();
            return true;
        } 
        Node node = new Node(value);
        hNode.pre.next = node;
        node.pre = hNode.pre;
        hNode.pre = node;
        node.next = hNode;
        size ++;
        printArr();
        return true;
    }
    
    /** Deletes an item from the front of Deque. Return true if the operation is successful. */
    public boolean deleteFront() {
        if (hNode == null) return false;
        if (size == 1) {
            hNode = null;
            size = 0;
            return true;
        }
        hNode.next.pre = hNode.pre;
        hNode.pre.next = hNode.next;
        hNode = hNode.next;
        size --;
        return true;
    }
    
    /** Deletes an item from the rear of Deque. Return true if the operation is successful. */
    public boolean deleteLast() {
        if (hNode == null) return false;
        if (size == 1) {
            hNode = null;
            size = 0;
            return true;
        }
        hNode.pre = hNode.pre.pre;
        hNode.pre.next = hNode;
        size --;
        return true;
    }
    
    /** Get the front item from the deque. */
    public int getFront() {
        if (hNode == null) return -1;
        return hNode.val;
    }
    
    /** Get the last item from the deque. */
    public int getRear() {
        if (hNode == null) return -1;
        return hNode.pre.val;
    }
    
    /** Checks whether the circular deque is empty or not. */
    public boolean isEmpty() {
        return size == 0;
    }
    
    /** Checks whether the circular deque is full or not. */
    public boolean isFull() {
        return size == limit;
    }
    public void printArr() {
        if (hNode == null) return;
        System.out.print("[ ");
        Node tmp1 = hNode,tmp2 = hNode.next;
        System.out.print(tmp1.val);
        System.out.print(",");
        while(tmp2 != tmp1){
            System.out.print(tmp2.val);
            System.out.print(",");
            tmp2 = tmp2.next;
        }
        System.out.print("]");
    }
}
class Node {
    int val;
    Node pre;
    Node next;
    Node(int value) {
        val = value;
        pre = null;
        next = null;
    }
}
/**
 * Your MyCircularDeque object will be instantiated and called as such:
 * MyCircularDeque obj = new MyCircularDeque(k);
 * boolean param_1 = obj.insertFront(value);
 * boolean param_2 = obj.insertLast(value);
 * boolean param_3 = obj.deleteFront();
 * boolean param_4 = obj.deleteLast();
 * int param_5 = obj.getFront();
 * int param_6 = obj.getRear();
 * boolean param_7 = obj.isEmpty();
 * boolean param_8 = obj.isFull();
 */
// @lc code=end

