function solution(s) {
    const arr = s.split(' ')
    let result = []
    let joinResult = ''

    for (let i = 0; i < arr.length; i++) {
        let word = ''
        for (let j = 0; j < arr[i].length; j++) {
            if (j % 2 === 0) {
                const upperLetter = arr[i][j].toUpperCase();
                word += upperLetter;
            } else {
                const lowerLetter = arr[i][j].toLowerCase();
                word += lowerLetter;
            }
        }
        result.push(word)
        joinResult = result.join(' ')
    }
  return joinResult
}