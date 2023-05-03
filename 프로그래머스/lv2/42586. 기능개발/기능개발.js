function solution(progresses, speeds) {
  const rest = []
  const result = []
  
  for (let i = 0; i < progresses.length; i++) {
    const restEl = Math.ceil((100 - progresses[i]) / speeds[i])
    rest.push(restEl)
  }
  
  let count = 1
  let maxDay = rest[0]
  
  for (let j = 1; j < rest.length; j++) {
    if (maxDay >= rest[j]) {
      count += 1
    } else {
      result.push(count)
      maxDay = rest[j]
      count = 1
    }
  }
  
  result.push(count)
  
  return result
}
