# Exercise 04. Leap Year

이번 과제에서는 입력된 연도가 윤년인지 판단하여 알려주는 프로그램을 작성합니다.

윤년의 자세한 의미에 대해서는 [위키피디아-윤년](https://ko.wikipedia.org/wiki/%EC%9C%A4%EB%85%84)을 참고하세요. 간단히 얘기해서, 주어진 연도가 4의 배수이면서 100의 배수가 아니면 윤년이고, 400의 배수인 경우도 윤년입니다. 나머지 경우들은 평년이 됩니다.

템플릿 코드 `leap_year.py`에서 여러분들은 `main`함수 내부의 주석 아래에 코드를 작성하면 됩니다. 주어진 템플릿은 수정하면 안됩니다. 즉, 주어진 조건문 구조 하에서 비어있는 부분에 대한 조건과 새로운 조건문 및 실행문을 기입해야 합니다.

``` python
def main():
    #===== write your code below =======

    if : 
        
    elif : 
            
    else:
        

if __name__ == '__main__':
    main()
```

작성된 코드를 실행하면 아래와 같이 사용자에게 연도를 입력받습니다.
``` bash
> python leap_year.py
Give a year:
```

입력받은 연도가 윤년이면 `The year is a leap year.`라는 메세지를 출력하고, 평년이면 `The year is not a leap year.`라는 메세지를 출력합니다. 예시들은 아래와 같습니다.
``` bash
Give a year: 2011
The year is not a leap year.

Give a year: 2012
The year is a leap year.

Give a year: 1800
The year is not a leap year.

Give a year: 2000
The year is a leap year.
```
위의 예시들과 같은 결과가 나오면 맞게 작성한 것으로 볼 수 있습니다. 작성한 후 여러 연도들을 입력하여 테스트해보세요.