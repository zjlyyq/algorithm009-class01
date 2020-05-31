class Solution {
    public boolean hasAllCodes(String s, int k) {
        if (s.length() - k + 1 < (1<<k)) return false;
        int count = 0;
        boolean[] cache = new boolean[1<<k + 1];
        int tmp;
        for (int i = 0;i < s.length() - k + 1;i ++) {
            tmp = getCodeOfSubString(s.substring(i, i+k), k);
            if (cache[tmp] == true) continue;
            cache[tmp] = true;
            count ++;
        }
        return count == 1<<k;
    }

    public int getCodeOfSubString(String s, int k) {
        int ret = 0;
        char[] chars = s.toCharArray();
        for (int i = 0;i < k;i ++) {
            if (chars[i] != '1') continue;
            ret += 1 << (k - i - 1);
        }
        return ret;
    }
}