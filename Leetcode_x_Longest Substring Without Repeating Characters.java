class Solution {
    
        int i;
        int j;
        int max = 0;
    
    public int lengthOfLongestSubstring(String s) {
        
      
        
        HashSet<Character> lonestString  = new HashSet<>();
        
        while(j<s.length()){
            if(!lonestString.contains(s.charAt(j))){
                lonestString.add(s.charAt(j));
                j++;
                max = Math.max(max, lonestString.size());
                
            }else{
                lonestString.remove(s.charAt(i));
                i++;
            }
        }
        return max;
        
    }
    
}   
