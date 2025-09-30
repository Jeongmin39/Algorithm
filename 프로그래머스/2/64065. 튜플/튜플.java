import java.util.*;

class Solution {
    public int[] solution(String s) {
        List<Integer> answer = new ArrayList<>();
        // s의 "},{"를 한번에 "-"로 치환
        s = s.substring(2, s.length() - 2).replace("},{", "-"); 
        // "-" 기준으로 분리
        String[] arr = s.split("-");
        
        Arrays.sort(arr, Comparator.comparingInt(String::length));
        for (String str : arr) {
            String[] temp = str.split(",");
            for (int i = 0; i < temp.length; i++) {
                int n = Integer.parseInt(temp[i]);
                
                if (!answer.contains(n)) {
                    answer.add(n);
                }
            }
        }
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}