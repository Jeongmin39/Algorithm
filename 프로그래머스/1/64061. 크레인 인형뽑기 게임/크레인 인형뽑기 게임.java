import java.util.*;

class Solution {
    public int solution(int[][] board, int[] moves) {
        int answer = 0;
        int n = board.length;
        Stack<Integer> stack = new Stack<>();
        
        for (int m : moves) {
            for (int i = 0; i < n; i++) {
                if (board[i][m-1] != 0) {
                    int num = board[i][m-1];
                    board[i][m-1] = 0;
                
                if (!stack.isEmpty() && stack.peek() == num) {
                    stack.pop();
                    answer += 2;
                } else {
                    stack.push(num);
                }
                break;
                }
            }
        }
        return answer;
    }
}