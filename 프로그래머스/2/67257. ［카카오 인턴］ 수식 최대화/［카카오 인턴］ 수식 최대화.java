import java.util.*;

class Solution {
    static char[] ops = {'+', '-', '*'};
    static long max = 0;
    
    public long solution(String expression) {
        List<Long> numbers = new ArrayList<>();
        List<Character> operators = new ArrayList<>();
        
        String num = "";
        for (char c : expression.toCharArray()) {
            if (c == '+' || c == '-' || c == '*') {
                numbers.add(Long.parseLong(num));
                num = "";
                operators.add(c);
            } else num += c;
        }
        numbers.add(Long.parseLong(num)); // 마지막 숫자 추가
        permute(operators, numbers, new boolean[3], new ArrayList<>());
        return max;
    }
    
    // 연산자 우선순위 순열 생성
    private void permute(List<Character> opsList, List<Long> nums, boolean[] visited, List<Character> order) {
        if (order.size() == 3) {
            evaluate(nums, opsList, order);
            return;
        }
        for (int i = 0; i < 3; i++) {
            if (!visited[i]) {
                visited[i] = true;
                order.add(ops[i]);
                permute(opsList, nums, visited, order);
                order.remove(order.size() - 1);
                visited[i] = false;
            }
        }
    }
    
    // 스택 계산
    private void evaluate(List<Long> nums, List<Character> opsList, List<Character> priority) {
        List<Long> numbers = new ArrayList<>(nums);
        List<Character> operators = new ArrayList<>(opsList);
        
        for (char op : priority) {
            Stack<Long> numStack = new Stack<>();
            Stack<Character> opStack = new Stack<>();
            numStack.push(numbers.get(0));
            
            for (int i = 0; i < operators.size(); i++) {
                char curOp = operators.get(i);
                long curNum = numbers.get(i+1);
                
                if (curOp == op) {
                    long prev = numStack.pop();
                    numStack.push(cal(prev, curOp, curNum));
                } else {
                    numStack.push(curNum);
                    opStack.push(curOp);
                }
            }
            numbers = new ArrayList<>(numStack);
            operators = new ArrayList<>(opStack);
        }
        
        max = Math.max(max, Math.abs(numbers.get(0)));
    }
    
    private long cal(long a, char op, long b) {
        return switch (op) {
            case '+' -> a + b;
            case '-' -> a - b;
            case '*' -> a * b;
            default -> 0;
        };
    }
}