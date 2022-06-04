class Animal{
	public void speak() {
		System.out.println("안녕하세요~");
	}

	
}
class Duck extends Animal{
	public void speak() {
		System.out.println("꽥꽥!");
	}
	
}

class Dog extends Animal{
	public void speak() {
		System.out.println("멍멍멍!");
	}
	
}

class Cat extends Animal{
	public void speak() {
		System.out.println("야옹 야옹");
	}
	
}
public class Test2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Animal duck=new Duck();
		Animal cat=new Cat();
		Animal dog= new Dog();
		
		duck.speak();
		cat.speak();
		dog.speak();
	}

}
