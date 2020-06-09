function majorityElement(nums: number[]): number {
    let map: Map<any,number> = new Map<any,number>();

    nums.forEach(i => {
        if (map[i] == undefined) map[i] = 1;
        else {
            let j = map[i] == undefined?0:map[i];
            map[i] = j+1;
        }
    })

    let ans: number[] = [];
    let size = Math.round(nums.length / 2);
    for (let [key, value] of map) {
        if (value >= size) ans.push(key);
    }

    return ans[0];
};