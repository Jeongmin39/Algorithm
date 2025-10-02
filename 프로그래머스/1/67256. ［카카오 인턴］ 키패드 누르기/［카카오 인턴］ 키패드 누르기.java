class Solution {
    public String solution(int[] numbers, String hand) {
        String answer = "";
        int LPos = 10;
        int RPos = 12;
        int[][] phone = {
            {0, 0}, {0, 1}, {0, 2},
            {1, 0}, {1, 1}, {1, 2},
            {2, 0}, {2, 1}, {2, 2},
            {3, 0}, {3, 1}, {3, 2}
        };
        
        for (int num : numbers) {
            if (num == 1 || num == 4 || num == 7) {
                LPos = num;
                answer += 'L';
            } else if (num == 3 || num == 6 || num == 9) {
                RPos = num;
                answer += 'R';
            } else {
                if (num == 0) num = 11;
                int LDis = Math.abs(phone[num-1][0] - phone[LPos-1][0]) 
                    + Math.abs(phone[num-1][1] - phone[LPos-1][1]);
                int RDis = Math.abs(phone[num-1][0] - phone[RPos-1][0]) 
                    + Math.abs(phone[num-1][1] - phone[RPos-1][1]);
                if (LDis < RDis) {
                    answer += 'L';
                    LPos = num;
                } else if (LDis > RDis) {
                    answer += 'R';
                    RPos = num;
                } else {
                    if (hand.equals("left")) {
                        answer += 'L';
                        LPos = num;
                    } else {
                        answer += 'R';
                        RPos = num;
                    }
                }
            }
        }
        return answer;
    }
}