package Week_01;
import java.util.Deque;
import java.util.LinkedList;

class DequeDemo {
    public void demo(String[] args) {
        Deque<String> deque = new LinkedList<String>();
        deque.addFirst("one");
        deque.addFirst("two");
        deque.addFirst("three");
        deque.addFirst("four");
        System.out.println(deque);

        // poll() return null,while remove() throws an exception 
        // when the queue is empty 
        String polledELement = deque.pollFirst();
        System.out.println(polledELement);
        System.out.println(deque);

        String  peekedElement = deque.peekFirst();
        System.out.println(peekedElement);
        System.out.println(deque);

        while(!deque.isEmpty()) {
            System.out.println(deque.pollFirst());
        }   
    }
}