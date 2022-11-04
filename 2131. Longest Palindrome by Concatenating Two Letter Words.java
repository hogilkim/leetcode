class Solution {
    public int longestPalindrome(String[] words) {
        HashMap<String, Integer> m = new HashMap();
        
        for (String word: words) {
            if (!m.containsKey(word)) m.put(word,0);
            m.put(word,m.get(word)+1);
        }
        
        int palin_diff = 0;
        int palin_same = 0;
        int center = 0;
        
        for (String word: m.keySet()){
            if (word.charAt(0) == word.charAt(1)){
                palin_same = palin_same + m.get(word)/2*2;
                if (m.get(word)%2 == 1) {
                center = 2;
                }
            }
            else{
                String reverse = Character.toString(word.charAt(1)) + Character.toString(word.charAt(0));
                if (m.containsKey(reverse)){
                    palin_diff = palin_diff + Math.min(m.get(word), m.get(reverse));
                }
            }
        }

        return palin_same*2 + palin_diff*2 + center;
    }
}