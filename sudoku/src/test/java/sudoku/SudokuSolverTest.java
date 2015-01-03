package sudoku;

import java.util.Arrays;

import org.junit.Assert;
import org.junit.Test;

public class SudokuSolverTest {

  private static final Puzzle PROBLEM = new Puzzle(Arrays.asList(
      (Arrays.asList(0, 0, 0, 9, 0, 0, 1, 7, 0)),
      (Arrays.asList(0, 0, 4, 0, 3, 0, 8, 0, 5)),
      (Arrays.asList(0, 0, 3, 0, 0, 8, 0, 0, 4)),
      (Arrays.asList(7, 0, 9, 6, 0, 0, 0, 0, 8)),
      (Arrays.asList(0, 0, 0, 0, 0, 0, 0, 0, 0)),
      (Arrays.asList(8, 0, 0, 0, 0, 5, 7, 0, 2)),
      (Arrays.asList(4, 0, 0, 2, 0, 0, 3, 0, 0)),
      (Arrays.asList(1, 0, 7, 0, 5, 0, 6, 0, 0)),
      (Arrays.asList(0, 8, 5, 0, 0, 6, 0, 0, 0))));

  private static final Puzzle SOLUTION = new Puzzle(Arrays.asList(
      (Arrays.asList(2, 5, 8, 9, 6, 4, 1, 7, 3)),
      (Arrays.asList(9, 1, 4, 7, 3, 2, 8, 6, 5)),
      (Arrays.asList(6, 7, 3, 5, 1, 8, 9, 2, 4)),
      (Arrays.asList(7, 4, 9, 6, 2, 1, 5, 3, 8)),
      (Arrays.asList(5, 3, 2, 8, 7, 9, 4, 1, 6)),
      (Arrays.asList(8, 6, 1, 3, 4, 5, 7, 9, 2)),
      (Arrays.asList(4, 9, 6, 2, 8, 7, 3, 5, 1)),
      (Arrays.asList(1, 2, 7, 4, 5, 3, 6, 8, 9)),
      (Arrays.asList(3, 8, 5, 1, 9, 6, 2, 4, 7))));

  private static final Puzzle INVALID_PROBLEM = new Puzzle(Arrays.asList(
      (Arrays.asList(0, 0, 0, 9, 0, 0, 1, 7, 1)),
      (Arrays.asList(0, 0, 4, 0, 3, 0, 8, 0, 5)),
      (Arrays.asList(0, 0, 3, 0, 0, 8, 0, 0, 4)),
      (Arrays.asList(7, 0, 9, 6, 0, 0, 0, 0, 8)),
      (Arrays.asList(0, 0, 0, 0, 0, 0, 0, 0, 0)),
      (Arrays.asList(8, 0, 0, 0, 0, 5, 7, 0, 2)),
      (Arrays.asList(4, 0, 0, 2, 0, 0, 3, 0, 0)),
      (Arrays.asList(1, 0, 7, 0, 5, 0, 6, 0, 0)),
      (Arrays.asList(0, 8, 5, 0, 0, 6, 0, 0, 0))));

  @Test
  public void basicPuzzle() {
    Assert.assertEquals(SOLUTION, SudokuSolver.solve(PROBLEM));
  }

  @Test(expected=IllegalArgumentException.class)
  public void invalidPuzzle() throws Exception {
    SudokuSolver.solve(INVALID_PROBLEM);
  }
}
