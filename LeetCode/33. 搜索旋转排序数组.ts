function search(nums: number[], target: number): number {
    let offset = getTurnPoint(nums);
    return binary_search(nums, target, offset);
};

function getTurnPoint(nums: number[]): number {
    let count = nums.length;
    let mod = nums.length;
    let cur = 0;
    while(count -- ){
        let pre = (cur - 1 + mod)%mod;
        let next = (cur + 1 + mod)%mod;
        if ((nums[next]-nums[cur])*(nums[cur]-nums[pre]) < 0) return cur+1;
        cur ++;
    }
    return 0;
}

function binary_search(nums:number[], target:number, offset:number):number {
    let low = 0, high = nums.length - 1;
    let mid = 0;
    let mod = nums.length;
    while(low <= mid) {
        mid = Math.floor(low + high / 2);
        let origin_pos = (mid - offset + mod)%nums.length;
        if (nums[origin_pos] == target) return mid;
        else if(nums[origin_pos] < target) low = mid + 1;
        else high = mid - 1;
    }
    return -1;
}