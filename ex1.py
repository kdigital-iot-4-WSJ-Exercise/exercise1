def start():
    print("Hello C World~")
    print("You are first here")
    print("Let's practice some exercises")


def add():
    print("Add Function Start)
    numbers = list(map(int, input(덧셈을 할 숫자를 입력하세요 : )))
    sum = 0
    for number in numbers:
        sum = sum + number
    return sum


print("System Initiating")
start()
sum = add()
print("덧셈 결과 : %d" % d)
print("더하기 날로 먹냐??")
print("End of File")
