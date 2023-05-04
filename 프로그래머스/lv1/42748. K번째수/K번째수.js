function solution(array, commands) {
    var answer = [];
    for (let i = 0; i < commands.length; i ++) {
        const slicedArray = array.slice(commands[i][0] - 1, commands[i][1])
        slicedArray.sort((a, b) => a - b)
        const index = commands[i][2]
        const num = slicedArray[index -1]
        answer.push(num)    
    }    
    return answer;
}