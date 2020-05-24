/*
 * @lc app=leetcode.cn id=25 lang=java
 *
 * [25] K 个一组翻转链表
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode reverseKGroup(ListNode head, int k) {
        ListNode[] endpoints = reverseKListNodeRet(head, k);
        if (endpoints.length > 2) {
            endpoints[1].next = reverseKGroup(endpoints[2],k);
        }
        // System.out.println(endpoints[0].val);
        return endpoints[0];
    }
    public ListNode[] reverseKListNodeRet(ListNode head, int k) {
        if (!isLongThanK(head,k)){
            return new ListNode[]{head, null};
        }
        ListNode t = head;
        ListNode cur = null, pre = head;
        while (k > 0 && pre != null) {
            k --;
            ListNode tmp = pre.next;
            pre.next = cur;
            cur = pre;
            pre = tmp;
        }
        if (k == 0) {
            return new ListNode[]{cur, t, pre};
        }
        else {
            return new ListNode[]{t, null};
        }
    }
    public boolean isLongThanK(ListNode head, int k) {
        ListNode node = head;
        while (k  > 0 && node!=null) {
            k --;
            node = node.next;
        }
        // System.out.println(k);
        // System.out.println(k==0);
        return  k==0;
    }   
}
// @lc code=end

