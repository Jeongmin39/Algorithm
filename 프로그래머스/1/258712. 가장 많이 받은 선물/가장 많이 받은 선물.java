import java.util.*;

class Solution {
    public int solution(String[] friends, String[] gifts) {
        int n = friends.length;
        
        Map<String, Integer> map = new HashMap<>();
        for (int i = 0; i < n; i++) {
            map.put(friends[i], i);
        }
        
        // 주고받은 선물 개수, 선물지수 저장
        int[][] giftCount = new int[n][n];
        int[] giftNumber = new int[n];
        for (String gift : gifts) {
            String[] arr = gift.split(" ");
            int index1 = map.get(arr[0]);
            int index2 = map.get(arr[1]);
            giftCount[index1][index2]++;
            giftNumber[index1]++;
            giftNumber[index2]--;
        }
        
        // 다음달 받을 선물 개수 저장
        int[] nextGift = new int[n];
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (giftCount[i][j] > giftCount[j][i]) {
                    nextGift[i]++;
                } else if (giftCount[i][j] < giftCount[j][i]) {
                    nextGift[j]++;
                } else {
                    if (giftNumber[i] > giftNumber[j]) nextGift[i]++;
                    else if (giftNumber[i] < giftNumber[j]) nextGift[j]++;
                }
            }
        }
        
        return Arrays.stream(nextGift).max().getAsInt();
    }
}