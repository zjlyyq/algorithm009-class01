/*
 * @lc app=leetcode.cn id=142 lang=java
 *
 * [142] 环形链表 II
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
    public ListNode detectCycle(ListNode head) {
        HashMap<ListNode,Integer> hashMap = new HashMap<>();
        while (head != null) {
            if (hashMap.get(head) != null) {
                return head;
            }
            hashMap.put(head, hashMap.size());
            head = head.next;
        }
        return null;
    }
}
// @lc code=end

