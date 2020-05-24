/*
 * @lc app=leetcode.cn id=146 lang=java
 *
 * [146] LRU缓存机制
 */

// @lc code=start
class LRUCache {
    int size;
    int cap;
    Node first;
    Node last;
    public LRUCache(int capacity) {
        cap = capacity;
        size = 0;
    }
    
    public int get(int key) {
        if (first == null) return -1;
        Node e = first;
        while(e != null) {
            if (e.key != key){
                e = e.next;
                continue;
            }
            // 如果查询元素不是不在链表头部，删除该元素放于头部
            if (e != first){
                removeEntry(e);
                addFirst(e.key, e.value);
            }
            return e.value;
        }
        return -1;
    }
    public void put(int key, int value) {
        Node e = getNode(key);
        if (e != null) {
            // 如果查询元素已经在链表头部，更新vlaue即可
            if (e == first) {
                e.value = value;
                return;
            }
            removeEntry(e);
        }
        addFirst(key, value);
    }

    Node getNode(int key) {
        if (first == null) return null;
        Node e = first;
        while(e != null) {
            if (e.key != key) {
                e = e.next;
                continue;
            }
            return e;
        }
        return null;
    }

    void addFirst(int key, int value) {
        Node e = new Node(key, value);
        if (size == cap) {
            removeEntry(last);
        }
        if (size == 0) {
            first = last = e;
        }
        else {
            e.next = first;
            first.pre = e;
            first = e;
        }
        size ++;
    }

    
    void removeEntry(Node e) {
        size --;
        if (size == 0) first = last = null;
        else {
            if (e == first) {
                first = first.next;
                first.pre = null;
            }
            else if (e == last) {
                last = last.pre;
                last.next = null;
            }    
            else {
                e.pre.next = e.next;
                e.next.pre = e.pre;
            }
        }
    }

    private static final class Node {
        int key;
        int value;
        Node next;
        Node pre;
        Node (int k, int v) {
            key = k;
            value = v;
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

