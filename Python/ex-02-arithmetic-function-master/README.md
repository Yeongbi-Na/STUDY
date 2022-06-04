# Exercise 02. Arithmetic Function

이제 두 번째 과제입니다. 첫 번째 과제와 마찬가지로 어렵지 않게 해결할 수 있는 내용입니다.

이 과제에서는 산술연산을 수행한 후 그 결과를 특정 변수에 할당하면 됩니다. 아래와 같은 연산을 수행하는 함수를 작성해보도록 하죠. 지금 **함수**라는게 뭔지 무엇인지 몰라도 전혀 걱정할 필요 없습니다. 그 개념을 몰라도 이번 과제는 해결할 수 있습니다.

여기서 작성할 5개의 연산 함수는 아래와 같습니다
* 두 수의 합을 계산하는 `addition` 함수
* 두 수의 차를 계산하는 `subtraction` 함수
* 두 수의 곱을 계산하는 `multiplication` 함수
* 두 수의 나눗셈을 계산하는 `division` 함수
* 두 수의 차이의 절대값을 계산하는 `absolute_value` 함수

`arithmetic_function.py` 파일을 열어보면 각 함수의 역할과 예시에 대해 자세히 기술되어 있으니 참고하세요. `addition` 함수를 하나의 예로 살펴보도록 하죠. `addition` 함수에 해당되는 템플릿 코드는 아래와 같습니다.

``` python
def addition(a, b):
    """두 개의 숫자 a, b를 입력받아 그 합을 출력하는 함수입니다.

    Input:
        a: 숫자 값 (e.g., int or float)
        b: 숫자 값 (e.g., int or float)
    
    Output:
        result: a와 b의 합
    
    Examples:
      >>> addition(3,5)
      8
      >>> addition(3,2)
      5
    """
    #===== write your code below =======

    result = None

    #===================================

    return result
```

여러분들이 코드를 작성해야 하는 부분은 `#===== write your code below =======`와 `#===================================` 사이 부분입니다. 이 부분을 보면 우변에서 연산을 수행하여 `result` 변수에 그 결과 값을 저장해야 한다는 것을 알 수 있을꺼에요. 좀 더 구체적으로 설명하면, `a`와 `b`라는 이름의 변수를 이용하여 주어진 연산을 수행하도록 우변에 코드를 작성하면 됩니다.

다른 것들은 아주 간단하게 해결이 가능한데 마지막 함수인 `absolute_value`는 수업시간에 다루지 않아 어떻게 구현할 수 있을지 금방 떠오르지 않을꺼에요. 이 부분은 여러분들이 직접 검색을 통해 해결해보도록 하세요. 막상 찾아보면 아주 간단하게 해결할 수 있을겁니다. 하나 힌트를 주자면, Python의 built-in 함수 중 하나를 이용하면 됩니다.

템플릿 코드의 맨 마지막 부분을 보면 아래와 같이 코드가 이미 작성되어 있습니다.

``` python
def main():
    print("Addition Test")
    print(addition(3,5)) # Expected Result: 8
    print(addition(10,5) == 15) # Expected Result: True
    print("Addition Test Closed \n")


    print("Subtraction Test")
    print(subtraction(3,5)) # Expected Result: -2
    print(subtraction(10,5) == 5) # Expected Result: True
    print(subtraction(10,15) == 5) # Expected Result: False
    print("Subtraction Test Closed \n")

    print("Multiplication Test")
    print(multiplication(3,5)) # Expected Result: 15
    print(multiplication(10,5) == 50) # Expected Result: True
    print(multiplication(10,-3) == 20) # Expected Result: False
    print("Multiplication Test Closed \n")

    print("Division Test")
    print(division(5,5)) # Expected Result: 1
    print(division(5,4)) # Expected Result: 1.25
    print(division(10,5) == 2) # Expected Result: True
    print(division(10,-3) == 0.33333) # Expected Result: False
    print("Division Test Closed \n")

    print("Absolute Value Test")
    print(absolute_value(1,2)) # Expected Result: 1
    print(absolute_value(4,2.5) == 1.5) # Expected Result: True
    print(absolute_value(-3,5) == 8) # Expected Result: True
```

이 코드들은 여러분들이 터미널에서 `python arithmeric_function.py` 를 입력하면 자동으로 실행됩니다. 여러분들이 각 함수를 제대로 구현했다면 주석으로 쓰여진 결과값들이 나와야 하겠죠? 맞게 구현했는지 위의 간단한 테스트를 통해 스스로 확인해보기 바랍니다.

지난 과제와 마찬가지로, 코드 작성이 완료되면 [codepost.io](https://codepost.io/) 에 업로드를 하고 테스트 결과를 확인하세요. 테스트를 통과하면 과제를 제대로 수행한 겁니다!