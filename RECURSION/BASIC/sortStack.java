/*package whatever //do not write package name here */

import java.util.Stack;

class GfG{
	public Stack<Integer> sort(Stack<Integer> s)
	{
			if (s.empty() == true) {
			return s;
		}

		// Remove the top element
		int top = s.peek();
		s.pop();
		// Recursion for the remaining elements in the stack
		sort(s);
		// Insert the popped element back in the sorted stack
		sortedInsert(s, top);
		return s;
	}
	public static void sortedInsert(Stack<Integer> stack, int current) {
		if (stack.empty() == true || current > stack.peek()) {
			stack.push(current);
			return;
		}

		// Remove the top element
		int top = stack.peek();
		stack.pop();
		// Recursion for the remaining elements in the stack
		sortedInsert(stack, current);
		// Insert the popped element back in the stack
		stack.push(top);
	}
}
