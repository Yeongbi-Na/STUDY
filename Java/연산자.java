import java.util.Scanner;
public class SwitchCal {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String str;
		int a,b;
		int value;
		Scanner scanner=new Scanner(System.in);
		
		System.out.print("수식을 입력하십시오? ");
		a=scanner.nextInt();
		str=scanner.next();
		b=scanner.nextInt();
		
		switch(str) {
		case "+":
			value=a+b;
			System.out.println(a+" + "+b+" = "+value);
			break;
		case "-":
			value=a-b;
			System.out.println(a+" - "+b+" = "+value);
			break;
		case "/":
			value=a/b;
			System.out.println(a+" / "+b+" = "+value);
			break;
		case "*":
			value=a*b;
			System.out.println(a+" * "+b+" = "+value);
			break;
		default:
			System.out.println("사칙연산이 아닙니다");
			break;
		
		
		}
		scanner.close();
		


	}

}
ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
실행결과
수식을 입력하십시오? 6 / 2
6 / 2 = 3
