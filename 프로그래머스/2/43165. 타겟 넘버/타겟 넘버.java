class Solution {
    int count = 0;
    public int solution(int[] numbers, int target) {
        int answer = 0;
        dfs(numbers, 0, target, 0);
        answer = count;
        
        return answer;
    }
    
    public void dfs(int[] numbers, int depth, int target, int sum) {
        if (depth == numbers.length) {
            if (target == sum) {
                count++;
            }
            return;
        }
        
        int plus = sum + numbers[depth];
        int minus = sum - numbers[depth];
        
        dfs(numbers, depth+1, target, plus);
        dfs(numbers, depth+1, target, minus);
    }
}