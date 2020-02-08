function solution(arr) {
    let sumArr = 0;
    for(let i = 0; i < arr.length; i++) {
        sumArr += arr[i];        
    }
    return sumArr / arr.length;
}