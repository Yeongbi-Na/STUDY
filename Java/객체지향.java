package java_Ch10;

public class Dog {
	String name;
	String chulsin;
	int age;
	String color;
	public void getInfo(){
	System.out.printf("강아지 종류:%s, 강아지 태생:%s, 연령:%d, 색깔:%s " ,name, chulsin,age,color);
		
	};
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Dog aa = new Dog();
		
		aa.name="Hush Puppy";
		aa.chulsin="England";
		aa.age=2;
		aa.color="Brown";
		aa.getInfo();
		
	}

}
