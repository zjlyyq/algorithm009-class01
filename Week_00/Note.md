#### 时间复杂度和空间复杂度

递归斐波那契数函数的时间复杂度：O(k^n)

```js
function fib(n) {
    if (n < 2) return 1;
    return fib(n-1) + fib(n-2);
}
```

递归复杂度分析：递归树

![](C:\Users\Jialu\Documents\mycode\algorithm009-class01\Week_00\digui.png)

##### [主定理]([https://zh.wikipedia.org/wiki/%E4%B8%BB%E5%AE%9A%E7%90%86](https://zh.wikipedia.org/wiki/主定理))

![](C:\Users\Jialu\Documents\mycode\algorithm009-class01\Week_00\zhudinli.png)