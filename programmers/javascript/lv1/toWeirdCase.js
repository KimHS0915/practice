function solution(s) {
    let answer = '';
    let wordIndex = 0;
    for(let i=0; i < s.length; i++) {
        if(s[i] === ' ') {
            answer += ' ';
            wordIndex = 0;
        } else if(wordIndex % 2 === 0) {
            answer += s[i].toUpperCase();
            wordIndex += 1;
        } else {
            answer += s[i].toLowerCase();
            wordIndex += 1;
        }
    }
    return answer;
}