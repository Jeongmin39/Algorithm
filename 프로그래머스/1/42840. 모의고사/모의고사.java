import java.util.*;

class Solution {
    public int[] solution(int[] answers) {
        int[] a1 = {1, 2, 3, 4, 5};
        int[] a2 = {2, 1, 2, 3, 2, 4, 2, 5};
        int[] a3 = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
        int[] score = {0, 0, 0};
        
        for(int i = 0; i < answers.length; i++) {
            if(answers[i] == a1[i%(a1.length)]) score[0]++;
            if(answers[i] == a2[i%(a2.length)]) score[1]++;
            if(answers[i] == a3[i%(a3.length)]) score[2]++;
        }
        
        // 가장 많이 맞춘 사람의 개수 구하기
        int max = Math.max(score[0], Math.max(score[1], score[2]));
        
        // 결과 담을 리스트 선언
        List<Integer> list = new ArrayList<>();        
        for(int i = 0; i < 3; i++) {
            if(max == score[i]) list.add(i+1);
        }
        
        // return할 배열
        int[] answer = new int[list.size()];
        for(int i = 0; i < list.size(); i++) {
            answer[i] = list.get(i);
        }
        
        return answer;
    }
}