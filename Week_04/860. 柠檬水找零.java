class Solution {
    public boolean lemonadeChange(int[] bills) {
        int sum_5 = 0;
        int sum_10 = 0;
        for(int bill:bills) {
            if (bill == 5) sum_5 += 5;
            else if (bill == 10) {
                if (sum_5 < 5) return false;
                sum_10 += 10;
                sum_5 -= 5;
            }
            else {
                if (sum_5 < 5 || (sum_10+sum_5 < 15)) return false;
                if (sum_10 > 0) {
                    sum_10 -= 10;
                    sum_5 -= 5;
                }
                else {
                    sum_5 -= 15;
                }
            }
        }
        return true;
    }
}