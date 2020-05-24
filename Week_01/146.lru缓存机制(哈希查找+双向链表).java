package Week_01;

import java.util.HashMap;
import java.util.Map;

/*
 * @lc app=leetcode.cn id=146 lang=java
 *
 * [146] LRU缓存机制
 */

// @lc code=start
class LRUCache {
    int size;
    int cap;
    // 伪头部，尾部——避免插入到头部和尾部使得判断
    DLinkedNode head;
    DLinkedNode tail;
    Map<Integer, DLinkedNode> cache = new HashMap<Integer, DLinkedNode>();
    public LRUCache(int capacity) {
        cap = capacity;
        size = 0;
        head = new DLinkedNode();
        tail = new DLinkedNode();
        head.next = tail;
        tail.pre = head;
    }
    
    public int get(int key) {
        DLinkedNode node = cache.get(key);
        if (node == null) {
            return -1;
        }
        if (node != head.next) {
            removeEntry(node);
            addFirst(node);
        }
        return node.value;
    }
    public void put(int key, int value) {
        DLinkedNode node = cache.get(key);
        if (node == null) {
            DLinkedNode dLinkedNode = new DLinkedNode(key, value);
            cache.put(key, dLinkedNode);
            if (size == cap) {
                cache.remove(tail.pre.key);
                removeEntry(tail.pre);
            }
            addFirst(dLinkedNode);
        }
        else {
            node.value = value;
            removeEntry(node);
            addFirst(node);
        }
    }


    void addFirst(DLinkedNode dLinkedNode) {
        dLinkedNode.next = head.next;
        dLinkedNode.pre = head;
        head.next.pre = dLinkedNode;
        head.next = dLinkedNode;
        size ++;
    }

    
    void removeEntry(DLinkedNode dLinkedNode) {
        dLinkedNode.pre.next = dLinkedNode.next;
        dLinkedNode.next.pre = dLinkedNode.pre;
        size --;
    }

    private static final class DLinkedNode {
        int key;
        int value;
        DLinkedNode next;
        DLinkedNode pre;
        DLinkedNode (int k, int v) {
            key = k;
            value = v;
        }
        DLinkedNode () {
            
        }
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */
// @lc code=end

