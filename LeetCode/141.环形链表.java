/*
 * @lc app=leetcode.cn id=141 lang=java
 *
 * [141] 环形链表
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public boolean hasCycle(ListNode head) {
        HashMap hashMap = new HashMap();
        ListNode node = head;
        hashMap.put(node,Math.random());
        if (head == null) {
            return false;
        }
        while (node.next != null) {
            if (hashMap.get(node.next) != null) {
                return true;
            }
            hashMap.put(node,Math.random());
            node = node.next;
        }
        return false;
    }
}
// @lc code=end

