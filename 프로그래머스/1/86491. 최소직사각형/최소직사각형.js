function solution(sizes) {

    let widthList = [];
    let heightList = [];
    
    for (let i = 0; i < sizes.length; i ++) {
        
        for(let j = 0; j < 2; j ++) {
            
                const width = sizes[i][0] > sizes[i][1] ? sizes[i][0] : sizes[i][1]
                const height = sizes[i][1] < sizes[i][0] ? sizes[i][1] : sizes[i][0]
                widthList.push(width)
                heightList.push(height)
        }
    }
    
    const maxWidth = Math.max(...widthList)
    const maxHeight = Math.max(...heightList)
    
    return maxWidth * maxHeight;
}