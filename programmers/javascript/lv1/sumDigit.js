function solution(n){
    let answer = 0;
    let stringN = String(n);
    for(let i = 0; i < stringN.length; i++){
        answer += stringN[i]*1;
    }
    return answer;
}