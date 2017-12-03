import java.util.*;
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
*/

class Day3 {
	// private static int theNum;
	// private Grid g;
	
	public static void main(String[] args) {
		
		if (args.length <= 0) {
			print ("Usage: 'Day3 ###'");
			return;
		}
		int theNum = Integer.parseInt( args[0]);
		
		Grid g = new Grid(theNum);
		g.draw();
	}
	
	static class Grid {
		enum direction {
			right,
			up,
			left,
			down
		}
		
		
		private ArrayList<Cell> cells = new ArrayList<>();
		private int value;
		private int max_x, min_x, max_y, min_y;
		private int curr_x, curr_y;
		private direction currDirection;
		
		public Grid(int value) {
			this.value = value;
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

				
			
		
		
		
		public void draw() { 
			print(this.toString());
		}
		public String toString() {
			StringBuilder sb = new StringBuilder();
			for(Cell c : cells) {
				// for(int i = 0 ; i < c.getValue() ; i++) {
					// sb.append("-");
				// }
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





