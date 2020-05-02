import math

def sieve_of_eratosthenes(x:int) -> list:
    # 初期化　全ての要素を1にする
    array = [1] * (x+1)

    # 素数でない0と1を0にする
    array[0] = 0
    array[1] = 0
    # 平方根を求める
    sqrt = int(math.sqrt(x))
    # 素数でないものを0にしていく(エラトステネスの篩)
    for n in range(2, (sqrt+1)):
        for i in range((n*2), (x+1), n):
            array[i] = 0

    # 要素が1のキーを格納した配列を作り直す
    answer = []
    for i, v in enumerate(array):
        if v:
            answer.append(i)
    return answer

if __name__ == '__main__':
    x = int(input())
    answer = sieve_of_eratosthenes(x)
    message = ','.join([ str(a) for a in answer])
    print(f'{x} の素数は {message} です\n')
