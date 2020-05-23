package LeetCode;

/*
 * @lc app=leetcode.cn id=641 lang=java
 *
 * [641] 设计循环双端队列
 */

// @lc code=start
class MyCircularDeque {
    int limit;
    int size;
    int[] arr;
    /** Initialize your data structure here. Set the size of the deque to be k. */
    public MyCircularDeque(int k) {
        limit = k;
        size = 0;
        arr = new int[k];
    }
    
    /** Adds an item at the front of Deque. Return true if the operation is successful. */
    public boolean insertFront(int value) {
        if (size == limit) return false;
        for(int i = size;i > 0;i --) arr[i] = arr[i-1];
        arr[0] = value;
        size ++;
        printArr();
        return true;
    }   
    
    /** Adds an item at the rear of Deque. Return true if the operation is successful. */
    public boolean insertLast(int value) {
        if (size == limit) return false;
        arr[size++] = value;
        printArr();
        return true;
    }
    
    /** Deletes an item from the front of Deque. Return true if the operation is successful. */
    public boolean deleteFront() {
        if (size == 0) return false;
        for (int i = 0;i < size-1;i ++) arr[i] = arr[i + 1];
        --size;
        return true;
    }
    
    /** Deletes an item from the rear of Deque. Return true if the operation is successful. */
    public boolean deleteLast() {
        if (size == 0) return false;
        size --;
        return true;
    }
    
    /** Get the front item from the deque. */
    public int getFront() {
        if (size == 0) return -1;
        return arr[0];
    }
    
    /** Get the last item from the deque. */
    public int getRear() {
        if (size == 0) return -1;
        return arr[size-1];
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
        System.out.print("[ ");
        for(int i = 0;i < arr.length;i ++){
            System.out.print(arr[i]);
            System.out.print(" ");
        }
        System.out.print("]");
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

