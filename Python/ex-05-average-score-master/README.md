# Exercise 05. 평균 점수 구하기

이번 과제에서는 입력된 점수들의 평균을 계산해 화면에 출력해주는 프로그램을 작성합니다.

이 프로그램이 수행해야 하는 기능들은 아래와 같습니다.
- 이 프로그램을 사용자로부터 0점 이상 100점 이하의 점수를 입력받습니다. 아래와 같이 안내를 출력하고 입력을 받습니다.
  
  ```bash
  Give your score (0~100):
  ```

- 사용자는 여러 개의 점수를 입력할 수 있고, 입력을 마치고 싶은 경우는 0점 이상 100점 이하의 수가 아닌 숫자를 입력합니다. 즉, 입력된 점수가 `0 <= 점수 <= 100` 가 아니면 프로그램은 더 이상 입력을 받지 않습니다. 

- 사용자로부터 입력이 끝나면 지금까지 입력된 점수를 바탕으로 평균 점수를 계산하여 화면에 출력합니다. 평균 점수는 소수점 아래 둘째자리까지만 표시합니다. 예시는 이렇습니다.
  
  ```bash
  Average score is 76.53.
  ```

템플릿 코드 `avg_score.py` 에서 `main` 함수 내부의 주석 아래에 코드를 작성하면 됩니다.

``` python
def main():
    #===== write your code below =======
  x=float(input())
  sum=0
  n=0
  while 1:
    if x<0 or x>100:
      break
    sum=sum+x
    n=n+1

  print("%.2f" %(sum/n))
  print("{}".format(sum/n))  
if __name__ == '__main__':
    main()
```
완성된 프로그램의 동작 예는 아래와 같습니다.

```bash
> python avg_score.py
Give your score (0~100): 78
Give your score (0~100): 82.3
Give your score (0~100): 90
Give your score (0~100): -1
Average score is 83.43.
```

여러 점수들을 입력하여 테스트해보고 제출하면 됩니다.