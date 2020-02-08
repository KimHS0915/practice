function solution(s) {
    const idx = parseInt(s.length / 2);
    if(s.length % 2 === 0){
        return s.slice(idx-1, idx+1);
    } else { 
        return s.charAt(idx);
    }
}