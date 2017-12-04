package ac.day3;

import java.util.*;

import static ac.utility.artPrint.print;

/*
	Advent of code 2017
	
	Day 3
	
	Part one:
	
		Each square on the grid is allocated in a spiral pattern starting at a 
		location marked 1 and then counting up while spiraling outward. For 
		example, the first few squares are allocated like this:

		17  16  15  14  13
		18   5   4   3  12
		19   6   1   2  11
		20   7   8   9  10
		21  22  23---> ...
		
		While this is very space-efficient (no squares are skipped), requested 
		data must be carried back to square 1 (the location of the only access 
		port for this memory system) by programs that can only move up, down, 
		left, or right. They always take the shortest path: the Manhattan 
		Distance between the location of the data and square 1.

		For example:

		Data from square 1 is carried 0 steps, since it's at the access port.
		Data from square 12 is carried 3 steps, such as: down, left, left.
		Data from square 23 is carried only 2 steps: up twice.
		Data from square 1024 must be carried 31 steps.

			
	// Your puzzle input is 265149.

*/

/*
--- Part Two ---

As a stress test on the system, the programs here clear the grid and then store the value 1 in square 1. Then, in the same allocation order as shown above, they store the sum of the values in all adjacent squares, including diagonals.

So, the first few squares' values are chosen as follows:

Square 1 starts with the value 1.
Square 2 has only one adjacent filled square (with value 1), so it also stores 1.
Square 3 has both of the above squares as neighbors and stores the sum of their values, 2.
Square 4 has all three of the aforementioned squares as neighbors and stores the sum of their values, 4.
Square 5 only has the first and fourth squares as neighbors, so it gets the value 5.
Once a square is written, its value does not change. Therefore, the first few squares would receive the following values:

147  142  133  122   59
304    5    4    2   57
330   10    1    1   54
351   11   23   25   26
362  747  806--->   ...
What is the first value written that is larger than your puzzle input?

Your puzzle input is still 265149.
*/


class Day3 {
	
	private static ArrayList<TestCase> tests = new ArrayList<>();
	
	public static void main(String[] args) {
			
		runTests();
		
		if (args.length <= 0) {
			print ("Usage: 'Day3 ###'");
			return;
		}
		
		int theNum = Integer.parseInt(args[0]);
		
		print("");
		print("PHASE ONE:");
		
		Grid g = new Grid(theNum);
		int dist = g.distanceToPort();
		if (g.count() <= 1500) g.draw();
		print ("The distance for " + Integer.toString(theNum) + " is " + Integer.toString(dist));
		
		/* end of phase 1 */
		
		
		print("");
		print("PHASE TWO:");	
		
		Grid h = Grid.gridVersionTwo(theNum);
		h.draw();
		int maxValue = h.getMaxValue();
		print ("The first value over " + Integer.toString(theNum) + " is " + Integer.toString(maxValue));	
	}	
		
	private static void runTests() {
		loadTestCases();
		checkTestCases();
	}
	private static void loadTestCases() {
		tests.add(new TestCase(1,0,2));
		tests.add(new TestCase(12,3,23));
		tests.add(new TestCase(23,2,25));
		tests.add(new TestCase(1024,31,1968));
		tests.add(new TestCase(3,2,4));
		tests.add(new TestCase(6,1,10));
		tests.add(new TestCase(9,2,10));
		tests.add(new TestCase(24,3,25));		
		tests.add(new TestCase(265149,438,266330));
		tests.add(new TestCase(60,5,122));
		tests.add(new TestCase(350,11,351));
		tests.add(new TestCase(800,15,806));
	}
	private static void checkTestCases() {
		for (TestCase tc : tests) {
			int result1 = new Grid(tc.getInputValue()).distanceToPort();
			if (result1 != tc.getP1()) {
				throw new RuntimeException("Hoo Nit tests fail");
			}
			if (Grid.gridVersionTwo(tc.getInputValue()).getMaxValue() != tc.getP2()) {
				throw new RuntimeException("Hoo Nit Too");
			}
		}
	}
}





