class Solution {
    public boolean increasingTriplet(int[] nums) {
        if (nums.length < 3) return false;
        int i = Integer.MAX_VALUE, j = Integer.MAX_VALUE;
        for (int m = 0 ; m<nums.length; m++){
            if (nums[m] <= i ){
                i =  nums[m];
            }
            else if  (nums[m] <= j){
                j = nums[m];         
                    
            }
            else {
                return true;
            }
        }
       return false; 
    }
}
