class Solution {
    public int solution(String dartResult) {
        int[] score = new int[3];
        int idx = -1;
        
        for (int i = 0; i < dartResult.length(); i++) {
            char c = dartResult.charAt(i);
            
            // 숫자인 경우
            if (Character.isDigit(c)) {
                idx++;
                if (c == '1' && dartResult.charAt(i + 1) == '0') {
                    score[idx] = 10;
                    i++;
                } else {
                    score[idx] = c - '0';
                }
            // 문자인 경우
            } else if (c == 'D') {
                score[idx] *= score[idx];
            } else if (c == 'T') {
                score[idx] *= score[idx] *= score[idx];
            } else if (c == '*') {
                if (idx == 0) {
                    score[idx] *= 2;
                } else {
                    score[idx - 1] *= 2;
                    score[idx] *= 2;
                }
            } else if (c == '#') {
                score[idx] *= -1;
            }
        }
        
        return score[0] + score[1] + score[2];
    }
}