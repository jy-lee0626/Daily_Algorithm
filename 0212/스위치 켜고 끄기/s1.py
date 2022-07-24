import sys

sys.stdin = open('input.txt')

T = int(input())  # 스위치 갯수
arr = list(map(int, input().split()))   # 초기 스위치 상태 리스트
student_num = int(input())  # 학생 수


'''
학생 수 만큼 반복문을 돌린다.
학생이 남자라면 받은 수의 배수 스위치를 바꿔준다.
학생이 여자라면 받은 수를 기준으로 양 옆이 같다면 스위치를 바꿔준다.
양 옆이 다르다면 받은 수의 스위치만 바꿔준다.
'''
for i in range(student_num):   # 학생 수 만큼 반복
    gender, num = map(int, input().split())
    number = num
    if gender == 1:
        while number <= T:
            if arr[number - 1]:
                arr[number - 1] -= 1
            else:
                arr[number - 1] += 1
            number += num

    elif gender == 2:
        j = 1
        if arr[num - 1]:
            arr[num - 1] -= 1
        else:
            arr[num - 1] += 1

        while arr[num - j - 1] == arr[num + j - 1] and num - j >= 0 and num + j - 1 < T:
            if arr[num - j - 1]:
                arr[num - j - 1] -= 1
                arr[num + j + 1] -= 1
            else:
                arr[num - j - 1] += 1
                arr[num + j + 1] += 1
            j += 1

for i in range(T):
    if (i + 1) % 20 == 0:
        print(arr[i])
    else:
        print(arr[i], end=' ')





