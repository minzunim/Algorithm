function solution(t, p) {
    var answer = 0;
    
    // p의 문자열 길이를 셈
    // t를 반복하면서 p의 길이만큼 slice를 한 문자열을 배열에 담음
    // 이 배열을 돌면서 p와 작거나 같은 수의 개수를 찾음
    
    let arr = [];
    let count = 0;
    
    for (let i = 0; i < t.length; i++) {

        const tSlice = t.slice(i, i + p.length)
        arr.push(tSlice)

        if (i + p.length === t.length) {
            break
        }   
    }
    
    let resultArr = [];
    for (let j = 0; j < arr.length; j ++) {
        if (Number(arr[j]) <= Number(p)) {
            resultArr.push(Number(arr[j]))
        }
    }
    // console.log(arr)
    // console.log(resultArr)
    return resultArr.length
}