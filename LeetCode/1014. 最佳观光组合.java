class Solution {
    public int maxScoreSightseeingPair(int[] A) {
        int maxValue = 0;
        for(int i = 0,j = A.length -1; i < j;) {
            if ( A[i]+A[j]-(j-i) > maxValue ) {
                maxValue = A[i]+A[j]-(j-i);
            }
            if (A[i] > A[j]) {
                j --;
            }
            else if(A[i] == A[j]) {
                if (A[i+1] >= A[j-1]) {
                    i ++;
                }
                else {
                    j --;
                }
            }
            else {
                i ++;
            }
        }

        return maxValue;
    }
}