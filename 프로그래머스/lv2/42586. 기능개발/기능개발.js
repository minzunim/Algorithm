function solution(progresses, speeds) {
    let answer = [0];
    let days = progresses.map((progress, index) => Math.ceil((100 - progress) / speeds[index]));
    let maxDay = days[0];

    for(let i = 0, j = 0; i< days.length; i++){
        if(days[i] <= maxDay) {
            answer[j] += 1;
        } else {
            maxDay = days[i];
            answer[++j] = 1;
        }
    }

    return answer;
}

/*
days: 각 기능의 배포 소요 시일을 순서대로 배열에 담음 (올림((100 - 현재 작업의 진도) / 개발 속도))
maxDay: 현재 가장 오래 소요되는 기능의 소요 시일 (처음에는 제일 첫 번째 기능 == days[0])
maxDay와 days의 각 요소들의 값을 비교
maxDay보다 작거나 같으면 answer[j] 1 증가
maxDay보다 크면 maxDay에 해당 요소를 저장하고 answer[++j] 1 증가
*/
