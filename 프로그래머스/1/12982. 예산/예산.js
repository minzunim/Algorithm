function solution(d, budget) {
    var answer = 0;
    let sum = 0;
    // 배열 안에 숫자들을 정렬함
    d.sort((a, b) => a - b)
    console.log(d)
    for (let i = 0; i < d.length ; i ++) {
        sum += d[i];
        if (sum < budget && d.length !== i + 1) {
            continue;
        } else if (sum === budget) {
            return i + 1
        } else if (sum > budget) {
            return i
        } else {
            return i + 1
        }
    }
}