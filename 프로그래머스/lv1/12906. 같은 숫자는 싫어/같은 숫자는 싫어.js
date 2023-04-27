function solution(arr)
{
    const stack = [];
    
    for (let i = 0; i < arr.length; i++) {
        stack.push(arr[i])
        if (arr[i] == arr[i + 1]) {
            stack.pop()
        }
    }
    return stack;
}