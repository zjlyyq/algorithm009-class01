function maxProfit(prices: number[]): number {
    let buyPoint: number = -1;
    let inCome: number = 0;
    for (let i = 0;i < prices.length;i ++) {
        if (buyPoint == -1 || prices[buyPoint] > prices[i]) {
            buyPoint = i;
        }
        if (buyPoint != -1 && prices[i] > prices[buyPoint]) {   
            inCome += prices[i] - prices[buyPoint];
            buyPoint = i;
        }
    }
    return inCome;
};