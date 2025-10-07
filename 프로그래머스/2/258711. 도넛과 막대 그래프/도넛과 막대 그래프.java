import java.util.*;

class Solution {
    public int[] solution(int[][] edges) {
        int[] answer = new int[4];
        
        Map<Integer, List<Integer>> graph = new HashMap<>();
        int[] inDegree = new int[1000001];
        int[] outDegree = new int[1000001];
        
        for (int[] edge : edges) {
            graph.computeIfAbsent(edge[0], k -> new ArrayList<>()).add(edge[1]);
            inDegree[edge[1]]++;
            outDegree[edge[0]]++;
        }
        
        for (int i = 0; i < outDegree.length; i++) {
            if (outDegree[i+1] >= 2 && inDegree[i+1] == 0) {
                answer[0] = i+1;
                break;
            }
        }
        
        boolean[] visited = new boolean[1000001];
        for (int i : graph.get(answer[0])) {
            if (visited[i]) continue;
            
            int idx = dfs(graph, i, visited);
            answer[idx]++;
        }
        return answer;
    }
    
    public int dfs(Map<Integer, List<Integer>> graph, int start, boolean[] visited) {
        Stack<Integer> stack = new Stack<>();
        stack.push(start);
        
        int nodeCount = 0, edgeCount = 0;
        while (!stack.isEmpty()) {
            int now = stack.pop();
            if (visited[now]) continue;
            
            visited[now] = true;
            nodeCount += 1;
            
            for (int next : graph.getOrDefault(now, new ArrayList<>())) {
                edgeCount += 1;
                if (!visited[next]) {
                    stack.push(next);
                }
            }
        }
        
        if (nodeCount == edgeCount) {
            return 1;
        } else if (nodeCount == edgeCount + 1) {
            return 2;
        } else {
            return 3;
        }
    }
}