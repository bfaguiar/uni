package ex2;

import java.util.Arrays;
import java.util.Scanner;
import java.util.Stack;

import static java.lang.System.*;

public class ReversePolishNotation {

	static Scanner sc = new Scanner(System.in);
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		String line = sc.nextLine();
		String[] lineSplitted = line.split(" ");
		Stack<Double> stck = new Stack();
		
		Arrays.asList(lineSplitted).forEach(ln -> add(ln, stck));
		
	}

	
	static void add(String elem, Stack<Double> stck) {
		
		if (!(isOperator(elem))) 
			stck.push( Double.parseDouble(elem));
		
		else {
			
			
			stck.forEach(out::println);
			
			double num1 = stck.pop();
			double num2 = stck.pop();
			
			if (elem.equals("+")) {
				stck.push(num1 + num2);
				stck.forEach(out::println);
			}
			
			else if (elem.equals("-")) {
				stck.push(num1 - num2);
				stck.forEach(out::println);
			}
			
			else if (elem.equals("/")) {
				stck.push(num1 / num2);
				stck.forEach(out::println);
			}
			
			else {
				stck.push(num1 * num2);
				stck.forEach(out::println);
			}
		}
	}
	
	static boolean isOperator(String elem) {
		if (elem.equals("+") || elem.equals("-") || elem.equals("/") || elem.equals("*"))
			return true;
		return false;
	}

}
