// https://mp.weixin.qq.com/s?__biz=MzI3NzIwMjk4OA==&mid=2247484626&idx=1&sn=101160d80c16bda479060f1f02e2bcb9&chksm=eb689591dc1f1c8787f4bb886119f84dbc9aea2bb9248b5c3818124e141e6ead4e1377807d3c&mpshare=1&scene=1&srcid=0630ebvWceB73bbd6mEx4HtM&sharer_sharetime=1593477503947&sharer_shareid=4305fe1e1639f31ec6e419a2648da783#rd


import java.util.*;

public class LargestNumber {
    private static String largestNumber(String[] a) {
        //write your code here
        String result = "";
        for (int i = 0; i < a.length; i++) {
            result += a[i];
        }
        return result;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        String[] a = new String[n];
        for (int i = 0; i < n; i++) {
            a[i] = scanner.next();
        }
        System.out.println(largestNumber(a));
    }
}


class Solution {
    public String minNumber(int[] nums) {
        String nums_str[] = new String[nums.length];
        for(int i = 0; i < nums.length; i++){
            nums_str[i] = String.valueOf(nums[i]);
        }
        Arrays.sort(nums_str, (m,n) -> (m + n).compareTo(n + m));
        String result = new String();
        for(String s : nums_str){
            result += s;
        }
        return result;
    }
}

