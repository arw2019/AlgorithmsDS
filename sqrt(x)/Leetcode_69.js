/**
 * @param {number} x
 * @return {number}
 */
var mySqrt = function(x) {
    var r = x;
    while (r*r > x){
        r = Math.floor((r+x/r)/2);
    }
    return Math.floor(r)
    
};
