import java.util.*;

class Solution {
    public int solution(int[] queue1, int[] queue2) {
        int answer = -1;
        Queue<Integer> q1 = new ArrayDeque<>();
        Queue<Integer> q2 = new ArrayDeque<>();
        
        long sum1 = 0, sum2 = 0;
        for (int n : queue1) {
            q1.offer(n);
            sum1 += n;
        }
        for (int n : queue2) {
            q2.offer(n);
            sum2 += n;
        }
        if ((sum1 + sum2) % 2 != 0) return -1;
        
        int count = 0;
        int limit = queue1.length * 3;
        while (count < limit) {
            if (sum1 > sum2) {
                int num = q1.poll();
                sum1 -= num;
                sum2 += num;
                q2.add(num);
            } else if (sum2 > sum1) {
                int num = q2.poll();
                sum2 -= num;
                sum1 += num;
                q1.add(num);
            } else if (sum1 == sum2) {
                answer = count;
                break;
            }
            count++;
        }
        return answer;
    }
}