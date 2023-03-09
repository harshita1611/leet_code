/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        ListNode *first = head;
        ListNode *second = head;

        while(!(second == NULL) && !(second->next == NULL)) {
            first = first->next;
            second = (second->next)->next;

            if(first == second) {
                first = head;
                int count = 0;
                while(first != second) {
                    first = first->next;
                    second = second->next;
                    count++;
                }
                return second;
            } 
        }
        return NULL; 
    }
};