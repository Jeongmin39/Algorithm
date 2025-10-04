class Solution {
    public int[] solution(String[][] places) {
        int[] answer = new int[5];
        for (int i = 0; i < 5; i++) {
            if (isSafe(places[i])) {
                answer[i] = 1;
            } else {
                 answer[i] = 0;
            }
        }
        return answer;
    }
    
    private boolean isSafe(String[] place) {
        char[][] map = new char[5][5];
        for (int i = 0; i < 5; i++) {
            map[i] = place[i].toCharArray();
        }
        
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                if (map[i][j] == 'P') {
                    if (!dfs(map, i, j, 0, new boolean[5][5])) {
                        return false;
                    }
                }
            }
        }
        return true;
    }
    
    private boolean dfs(char[][] map, int x, int y, int distance, boolean[][] visited) {
        if (distance > 0 && map[x][y] == 'P') return false;
        if (distance == 2) return true;
        
        visited[x][y] = true;
        int[] dx = {-1, 1, 0, 0};
        int[] dy = {0, 0, -1, 1};
        
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            
            if (nx < 0 || ny < 0 || nx >= 5 || ny >= 5 || visited[nx][ny]) continue;
            if (map[nx][ny] == 'X') continue;
            
            if (!dfs(map, nx, ny, distance + 1, visited)) {
                return false;
            }
        }
        return true;
    }
}