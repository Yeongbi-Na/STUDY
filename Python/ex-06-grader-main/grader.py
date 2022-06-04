
def compute_average(*args):
    """점수들을 인자로 받아 평균 점수를 계산하는 함수입니다.

    Input:
        args: 0점 이상 100점 이하의 점수들 (가변인자)
    
    Output:
        average: 평균 점수
    
    Examples:
        >>> compute_average(10,20,30)
        20.0
        >>> compute_average(60,54,82,100)
        74.0
        >>> compute_average(60,120)
        Invalid score!
    """
    #===== write your code below =======
    sum=0
    for i in range(0,len(args)):
        if args[i]<0 or args[i]>100:
            sum=sum+args[i]
        else:
            print("Invalid score")
    average=sum/len(args)
    #===================================
    
    return average

def print_grade(avg):
    """평균 점수를 입력받아 해당되는 grade를 화면에 출력하는 함수입니다.

    Input:
        average: 평균 점수

    Examples:
        >>> get_grade(90.0)
        Average: 90.0000
        Grade: A
        >>> get_grade(62.4)
        Average: 62.4000
        Grade: D
    """
    #===== write your code below =======
    if avg>=90:
        score="A"

    
    #===================================


if __name__ == '__main__':

    print('Test...')
    average = compute_average(10,20,30)
    print_grade(average)
