function solution(x) {
    let answer = false;
    const stringX = String(x);
    let sumNumber = 0;
    for(let i = 0; i < stringX.length; i++){
        sumNumber += Number(stringX[i]);
    }
    if(x % sumNumber === 0){
        answer = true;
    }
    return answer;
}