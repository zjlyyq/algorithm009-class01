var CQueue = function() {
    this._queue = [];
    this._size = 0;
};

/** 
 * @param {number} value
 * @return {void}
 */
CQueue.prototype.appendTail = function(value) {
    this._queue.push(value);
    this._size ++;
};

/**
 * @return {number}
 */
CQueue.prototype.deleteHead = function() {
    if (this._size === 0) {
        return -1;
    }
    let ret =  this._queue[0];
    let stack = [].concat(this._queue.slice(1));
    this._queue = stack;
    this._size --;
    return ret;
};

/**
 * Your CQueue object will be instantiated and called as such:
 * var obj = new CQueue()
 * obj.appendTail(value)
 * var param_2 = obj.deleteHead()
 */