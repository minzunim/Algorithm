function solution(s, n) {
        
    // 문자열을 쪼개서 배열에 담음 => split
    
    const splitArr = s.split('')
    console.log(splitArr)
    
    const lowers = 'abcdefghijklmnopqrstuvwxyz'
    const uppers = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    let newArr = []
    let originalIndex = 0
    let newIndex = 0
    let newletter = ''
    
    for (const a of splitArr) {
        
        if (lowers.includes(a)) {
            originalIndex = lowers.indexOf(a)
            newIndex = (originalIndex + n) % 26
            newletter = lowers[newIndex]
        
        } else if (uppers.includes(a)) {
            originalIndex = uppers.indexOf(a)
            newIndex = (originalIndex + n) % 26
            newletter = uppers[newIndex]
            
        } else {
            newletter = ' '
        }    
            newArr.push(newletter)
    }
    
    const newWord = newArr.join('')
    return newWord
    
}