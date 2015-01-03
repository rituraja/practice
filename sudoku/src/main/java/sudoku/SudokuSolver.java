package sudoku;


public class SudokuSolver {

  private static boolean doSolve(Coordinate current , Puzzle puzzle) {
    Coordinate next = puzzle.nextEmptyCell(current);
    if (next == null)
      return true; /* found solution */

    for (int val = 1; val <= 9; val++) {
      if (puzzle.isValid(next, val)) {
        puzzle.setValue(next, val);
        if (doSolve(next, puzzle)) {
          System.out.println("Hurray!!!");
          return true;
        } else
          puzzle.setValue(next, 0);
      }
    }
    return false;
  }

  public static Puzzle solve(Puzzle puzzle) {
    Puzzle solution = puzzle.copyOf();
    boolean found = doSolve(new Coordinate(-1, -1), solution);
    if (!found)
      throw new IllegalArgumentException("The puzzle is invalid");
    return solution;
  }

  public static void main(String[] args) {
    // TODO Auto-generated method stub
    System.out.println("Finding Solution...");
    Puzzle solution = SudokuSolver.solve(new Puzzle());
    System.out.println(solution);
  }

}
