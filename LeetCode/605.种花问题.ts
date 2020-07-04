function canPlaceFlowers(flowerbed: number[], n: number): boolean {
    for (let i: number = 0;i < flowerbed.length; i ++) {
        if (flowerbed[i] == 1) i ++;;
        if (flowerbed[i] == 0) {
            if ( i == 0 || flowerbed[i-1] == 0) {
                if (i + 1 == flowerbed.length ||  flowerbed[i+1] == 0) {
                    n --;
                    if (n == 0) return true;
                }
            }
        }
    }

    return n <= 0;
};