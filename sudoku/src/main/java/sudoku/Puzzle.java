package sudoku;

import java.io.IOException;
import java.nio.charset.Charset;
import java.nio.file.FileSystems;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.StandardOpenOption;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Puzzle {

  private List<List<Integer>> grid;

  public Puzzle() {
    grid = Arrays.asList((Arrays.asList(0, 0, 0, 9, 0, 0, 1, 7, 0)),
        (Arrays.asList(0, 0, 4, 0, 3, 0, 8, 0, 5)),
        (Arrays.asList(0, 0, 3, 0, 0, 8, 0, 0, 4)),
        (Arrays.asList(7, 0, 9, 6, 0, 0, 0, 0, 8)),
        (Arrays.asList(0, 0, 0, 0, 0, 0, 0, 0, 0)),
        (Arrays.asList(8, 0, 0, 0, 0, 5, 7, 0, 2)),
        (Arrays.asList(4, 0, 0, 2, 0, 0, 3, 0, 0)),
        (Arrays.asList(1, 0, 7, 0, 5, 0, 6, 0, 0)),
        (Arrays.asList(0, 8, 5, 0, 0, 6, 0, 0, 0)));
  }

  public Puzzle(List<List<Integer>> grid) {
    this.grid = grid;
  }

  public List<List<Integer>> getGrid() {
    return grid;
  }

  public int getValue(int row, int col) {
    return grid.get(row).get(col);
  }

  public int getValue(Coordinate coordinate) {
    return grid.get(coordinate.row).get(coordinate.col);
  }

  public void setValue(int row, int col, int val) {
    grid.get(row).set(col, val);
  }

  public void setValue(Coordinate coordinate, int val) {
    grid.get(coordinate.row).set(coordinate.col, val);
  }

  @Override
  public String toString() {
    String str = "";

    for (int i = 0; i < 9; i++) {
      for (int val : grid.get(i)) {
        str = str + val + ",";
      }
      str = str.replaceAll(",$", "\n") ;
    }
    return str;
  }

  @Override
  public boolean equals(Object obj) {
    if (!(obj instanceof Puzzle)) {
      return false;
    }
    Puzzle that = (Puzzle) obj;
    return grid.equals(that.grid);
  }

  @Override
  public int hashCode() {
    return grid.hashCode();
  }

  public Puzzle copyOf() {
    List<List<Integer>> copy = new ArrayList<>(grid);
    for (int i = 1; i < copy.size(); i++) {
      copy.set(i, new ArrayList<Integer>(grid.get(i)));
    }
    return new Puzzle(copy);
  }

  public Coordinate nextEmptyCell(Coordinate currXY) {
    Coordinate nextCell = new Coordinate();
    nextCell.row = currXY.row;
    nextCell.col = currXY.col;

    while (true) {
      nextCell.col = (nextCell.col + 1) % 9;
      nextCell.row = nextCell.row;
      if (nextCell.col == 0)
        nextCell.row++;
      if (nextCell.row == 9)
        return null;
      if (this.getValue(nextCell.row, nextCell.col) == 0)
        return nextCell;
    }
  }

  public boolean isValid(Coordinate curr, int value) {

    for (int i = 0; i < 9; i++) {
      if (this.getValue(curr.row, i) == value) {
        return false;
      }
      if (this.getValue(i, curr.col) == value) {
        return false;
      }
    }

    Coordinate miniGrid = new Coordinate();
    miniGrid.row = 3 * (curr.row / 3);
    miniGrid.col = 3 * (curr.col / 3);
    for (int i = 0; i < 3; i++) {
      for (int j = 0; j < 3; j++) {
        if (this.getValue(miniGrid.row + i, miniGrid.col + j) == value) {
          return false;
        }
      }
    }
    return true;
  }

  public static Puzzle fromFile(String filename) {
    Path path = FileSystems.getDefault().getPath(filename);
    List<List<Integer>> fileGrid = new ArrayList<>();
    try {
      List<String> lines = Files.readAllLines(path, Charset.defaultCharset());
      for (String line : lines) {
        List<Integer> rowList = new ArrayList<>(9);
        for (String num : line.split(",")) {
          rowList.add(Integer.valueOf(num.trim()));
        }
        fileGrid.add(rowList);
      }
    } catch (IOException e) {
      throw new IllegalArgumentException(e);
    }

    return new Puzzle(fileGrid);
  }

  public void toFile(String filename) {
    Path path = FileSystems.getDefault().getPath(filename);
    String content = this.toString();
    try {
      Files.write(path, content.getBytes(), StandardOpenOption.TRUNCATE_EXISTING);
    } catch (IOException e) {
      // TODO Auto-generated catch block
      e.printStackTrace();
    }
  }
}
