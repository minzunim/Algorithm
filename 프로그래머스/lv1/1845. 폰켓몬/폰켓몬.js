function solution(nums) {
    console.log(nums)
    const length = nums.length / 2
    const setNums = new Set(nums)
    
    console.log(setNums)
    console.log(length)
    
    if (length > setNums.size) {
        return setNums.size
    }
    return length
}