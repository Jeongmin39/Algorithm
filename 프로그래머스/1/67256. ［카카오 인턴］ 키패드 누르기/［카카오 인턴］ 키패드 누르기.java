class Solution {
    public String solution(int[] numbers, String hand) {
        StringBuilder sb = new StringBuilder();
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
                sb.append('L');
            } else if (num == 3 || num == 6 || num == 9) {
                RPos = num;
                sb.append('R');
            } else {
                if (num == 0) num = 11;
                int LDis = Math.abs(phone[num-1][0] - phone[LPos-1][0]) 
                    + Math.abs(phone[num-1][1] - phone[LPos-1][1]);
                int RDis = Math.abs(phone[num-1][0] - phone[RPos-1][0]) 
                    + Math.abs(phone[num-1][1] - phone[RPos-1][1]);
                if (LDis < RDis) {
                    LPos = num;
                    sb.append('L');
                } else if (LDis > RDis) {
                    RPos = num;
                    sb.append('R');
                } else {
                    if (hand.equals("left")) {
                        LPos = num;
                        sb.append('L');
                    } else {
                        RPos = num;
                        sb.append('R');
                    }
                }
            }
        }
        return sb.toString();
    }
}