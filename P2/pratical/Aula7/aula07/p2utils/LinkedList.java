package aula07.p2utils;

public class LinkedList<E> {
	
	private class Node<E> {
		
		final E elem;
		Node<E> next;

		Node(E e, Node<E> n) {
			elem = e;
			next = n;
		}

		Node(E e) {
			elem = e;
			next = null;
		}
	}
   /**
    * {@code LinkedList} constructor, empty so far.
    */
   public LinkedList() { return;  }

   /**
    * @return Number of elements in the list
    */
   public int size() { return size; }

   /**
    * Checks if the list is empty
    * @return  {@code true} if list empty, otherwise {@code false}.
    */
   public boolean isEmpty() { return size == 0; }

   /**
    * @return  First element in the list
    */
   public E first() {
      assert !isEmpty(): "empty!";

      return first.elem;
   }

   /**
    * @return  Last element in the list
    */
   public E last() {
      assert !isEmpty(): "empty!";
 
      return last.elem;
   }

   /**
    * Adds a new element to the start of the list
    */
   public void addFirst(E e) {
      first = new Node<>(e, first);
      if (isEmpty())
         last = first;
      size++;
   }

   /**
    * Adds a new element to the end of the list
    */
   public void addLast(E e) {
      Node<E> newest = new Node<>(e);
      if (isEmpty())
         first = newest;
      else
         last.next = newest;
      last = newest;
      size++;
   }

   /**
    * Removes the first element in the list
    */
   public void removeFirst() {
      assert !isEmpty(): "empty!";
      first = first.next;
      size--;
      if (isEmpty())
         last = null;
   }
   
   
   public LinkedList<E>  clone() {
	    
		LinkedList<E> getClone = new LinkedList<E>();
		Node<E> n = first;
		for (int i = 0; i < size(); i++) {
			getClone.addLast(n.elem);
		}
	    return getClone;
   }
   
	public LinkedList<E> reverse() { //nao sei se esta bem
		LinkedList<E> getReverse = new LinkedList<E>();
		Node<E> n = first;
		for (int i = 0; i < size () ; i++ ) {
			getReverse.addFirst(n.elem);
		}
		return getReverse; 
	}
	
	public E get(int pos) { //fazer
		for (int i = 0; i < size()-1; i++) {
			 ;
		}
		return null;
	}
   
   
   

   private Node<E> first = null;
   private Node<E> last = null;
   private int size = 0;
  
}


