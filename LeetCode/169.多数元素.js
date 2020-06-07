function majorityElement(nums) {
    var map = new Map();
    nums.forEach(function (i) {
        if (map[i] == undefined)
            map[i] = 1;
        else {
            var j = map[i] == undefined ? 0 : map[i];
            map[i] = j + 1;
        }
    });
    var ans = [];
    var size = Math.round(nums.length / 2);
    for (var _i = 0, map_1 = map; _i < map_1.length; _i++) {
        var _a = map_1[_i], key = _a[0], value = _a[1];
        if (value >= size)
            ans.push(key);
    }
    return ans[0];
}
;
