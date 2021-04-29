# Chpater10-1
# Hangman(행맨) 미니 게임 제작(1)
# 기본 프로그램 제작 및 테스트

import time

# 처음 인사
name = input('Nice to meet you!! What is your name??')

print(name, '? What a cool name!', 'Time to play hangman game welcome!!')

print()

time.sleep(1)

print('Start Loading...')
print()
time.sleep(0.5)

# 정답 단어
word = 'deeplearning'

# 추측 단어
guesses = ''

# 기회 횟수
turns = 10

# 핵심!! while
# 찬스 카운트가 남아 있을 경우
while turns > 0:
    # 실패 횟수(단어 매치 수)
    failed = 0

    # 정답 단어 반복
    for char in word:
        # 정답 단어 에 추측 문자가 포함되어 있는 경우
        if char in guesses:
            # 추측 단어
            print(char, end=' ')
        else:
            # 틀린 경우 대시로 처리
            print('_',end=' ')
            failed += 1
        # 단어 추측이 성공 한 경우
    if failed == 0:
        print()
        print()
        print('Wow! right!')
        break
    print()
        # 추측 단어 글자 단위 입력
    print()
    guess = input('Guess a character : ')
        # 단어 더하기
    guesses += guess
        # 정답 단어에 추측한 문자가 포함되어 있지 않으면
    if guess not in word:
        turns -= 1
        # 오류 메시지
        print('NO...:( that is not wrong')
        print('You have ', turns, ' more chances')
        if turns == 0:
            print('Im sorry to know that you cant play more')
