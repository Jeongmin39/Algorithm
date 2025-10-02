import java.util.*;

class Solution {
    public String solution(String[] survey, int[] choices) {
        StringBuilder sb = new StringBuilder();
        int[] scores = {3, 2, 1, 0, 1, 2, 3};
        
        Map<Character, Integer> map = new HashMap<>();
        char[] keys = {'R', 'T', 'C', 'F', 'J', 'M', 'A', 'N'};
        for (char key : keys) {
            map.put(key, 0);
        }
        
        for (int i = 0; i < survey.length; i++) {
            int c = choices[i];
            if (c < 4) {
                map.put(survey[i].charAt(0), map.get(survey[i].charAt(0)) + scores[c-1]);
            } else if (c > 4) {
                map.put(survey[i].charAt(1), map.get(survey[i].charAt(1)) + scores[c-1]);
            } 
        }
        
        for (int i = 0; i < keys.length; i += 2) {
            if (map.get(keys[i]) >= map.get(keys[i+1])) {
                sb.append(keys[i]);
            } else {
                sb.append(keys[i+1]);
            }
        }
         
        return sb.toString();
    }
}