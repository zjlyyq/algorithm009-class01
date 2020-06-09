### 递归

什么样的问题适合递归？  **重复性**

递归模板：

```typescript
function recur(level: number, MaxLevel: number, param: any): any{
    // recursion terminator 
    if (level > MaxLevel) return;
    
    // process current logic 
    process(level, param); 

    // drill down 
    process(level+1, newParam); 
    
    // restore current status 
}
```



### 分治

什么样的问题适合分治？  **子问题拆分**

分治模板：

```typescript
function divide_conquer(problem: any, param1: any, param2: any, ...): any{
    // recursion terminator 
    if (problem == null) return;

    // prepare data 
    data:any  = prepare_data(problem) 
    subproblems:any = split_problem(problem, data) 

    // conquer subproblems 
    subresult1 = divide_conquer(subproblems[0], p1, ...) 
    subresult2 = divide_conquer(subproblems[1], p1, ...) 
    subresult3 = divide_conquer(subproblems[2], p1, ...) 
    ...

    // process and generate the final result
    result = process_result(subresult1, subresult2, subresult3, …) 

    // revert the current level states
}
```

### 回溯

采用递归方法，在每一层递归中采用试错的办法尝试解决问题，当发现不能解决问题的时候，取消上一步乃至上几步的计算。经典应用：八皇后问题

