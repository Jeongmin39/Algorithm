import java.util.Arrays;

class Solution {
    public String[] solution(int n, int[] arr1, int[] arr2) {
        String[] answer = new String[n];
        String[] b1 = new String[n];
        String[] b2 = new String[n];
        
        for (int i = 0; i < n; i++) {
            b1[i] = String.format("%" + n + "s", Integer.toBinaryString(arr1[i])).replace(' ', '0');
            b2[i] = String.format("%" + n + "s", Integer.toBinaryString(arr2[i])).replace(' ', '0');
        }
        
        for (int i = 0; i < n; i++) {
            StringBuilder sb = new StringBuilder();
            for (int j = 0; j < n; j++) {
                if (b1[i].charAt(j) == '0' && b2[i].charAt(j) == '0') {
                    sb.append(' ');
                } else {
                    sb.append('#');
                }
            }
            answer[i] = sb.toString();
        }        
        return answer;
    }
}