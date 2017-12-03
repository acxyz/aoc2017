import java.util.*;
import java.lang.Math;
import static ac.artPrint.print;

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

	
	public static void main(String[] args) {
		
		// unit tests
		
		int dist_1 = new Grid(1).distanceToPort();
		int dist_12 = new Grid(12).distanceToPort();
		int dist_23 = new Grid(23).distanceToPort();
		int dist_1024 = new Grid(1024).distanceToPort();
		
		if (dist_1 != 0 ||
			dist_12 != 3 ||
			dist_23 != 2 ||
			dist_1024 != 31) {		
				throw new RuntimeException("Unit tests fail");
		}
		
		
		if (args.length <= 0) {
			print ("Usage: 'Day3 ###'");
			return;
		}
		int theNum = Integer.parseInt( args[0]);
		
		print("");
		print("PHASE ONE:");
		
		Grid g = new Grid(theNum);
		int dist = g.distanceToPort();
		// g.draw();
		print ("The distance for " + Integer.toString(theNum) + " is " + Integer.toString(dist));
		
		/* end of phase 1 */
		
		
		print("");
		print("PHASE TWO:");
		
		Grid h = gridVersionTwo(dist);
		h.draw();
		int maxValue = h.getMaxValue();
		print ("The maximum value is " + Integer.toString(maxValue));
		
		
	}
	
	static Grid gridVersionTwo(int targetMaxValue) {
		Grid g = new Grid(1);
		g.makeCellsToTargetValue(targetMaxValue);
		return g;
	}
	
	static class Grid {
		enum direction {
			right,
			up,
			left,
			down
		}
		
		
		private ArrayList<Cell> cells = new ArrayList<>();
		
		private int max_x, min_x, max_y, min_y;
		private int curr_x, curr_y;
		private direction currDirection;
		
		public int getMaxValue() {
			if (!cells.isEmpty()) {
				Cell last = cells.get(cells.size() - 1);
				return last.getValue();
			} else {
				throw new IndexOutOfBoundsException();
			}
		}
		
		public Grid(int value) {
			makeCells(value);
		}

		private void makeCells(int value) { // phase 1
			for(int i = 1 ; i <= value ; i++) {
				cells.add(makeCell(i));
			}
		}

		private Cell makeCell(int value) {
			if (value == 1) {
				initializeGrid();
				return new Cell(value,0,0);
			} else {
				return getNextCell(value);
			}
		}
		
		private void makeCellsToTargetValue(int target) {
			int nextValue;
			do {
				setNextCoordinates();
				nextValue = getAdjacentValues();
				// if (nextValue <= target) {
					cells.add( new Cell(nextValue, curr_x, curr_y) );
				// }
			} while (nextValue <= target);			
		}
		
		private int getAdjacentValues() {
			// for now, just read through whole list although this is not efficient.
			int total = 0;
			for (Cell c : cells) {
				if (Math.abs(c.getX() - curr_x) == 1 ||
					Math.abs(c.getY() - curr_y) == 1) {
					total += c.getValue();
				}
			}
			return total;
		}
		
		private void initializeGrid() {
			max_x = 0;
			max_y = 0;
			min_x = 0;
			min_y = 0;
			curr_x = 0;
			curr_y = 0;
			currDirection = direction.right;
		}
		
		private Cell getNextCell(int value) {
			setNextCoordinates();
			return new Cell(value, curr_x, curr_y);
		}
		private void setNextCoordinates() {
			if (currDirection == direction.right) {
				curr_x++;
				if (curr_x > max_x) {
					max_x = curr_x;
					currDirection = direction.up;
				}
			} else if (currDirection == direction.up) {
				curr_y++;
				if (curr_y > max_y) {
					max_y = curr_y;
					currDirection = direction.left;
				}
			} else if (currDirection == direction.left) {
				curr_x--;
				if (curr_x < min_x) {
					min_x = curr_x;
					currDirection = direction.down;
				}
			} else {
				curr_y--;
				if (curr_y < min_y) {
					min_y = curr_y;
					currDirection = direction.right;
				}
			}
		}

		public int distanceToPort() {
			return Math.abs(curr_x) + Math.abs(curr_y);
		}
		
		
		
		public void draw() { 
			print(this.toString());
		}
		public String toString() {
			StringBuilder sb = new StringBuilder();
			for(Cell c : cells) {
				sb.append(Integer.toString(c.getValue()) + " [" + Integer.toString(c.getX()) + "," + Integer.toString(c.getY()) + "]\n");
			}
			return sb.toString();
		}
				
	}
	
	static class Cell {
		private int value;
		private int x;
		private int y;
		
		public int getValue() {
			return value;
		}
		public int getX() {
			return x;
		}
		public int getY() {
			return y;
		}
		
		public Cell(int value, int x, int y) {
			this.value = value;
			this.x = x;
			this.y = y;
		}
	}
	
}





