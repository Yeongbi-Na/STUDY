class Car{
	String name;
	
}

class GoodCar extends Car{
	String supply;
	int price;
	
	public void Print() {
		System.out.println("차량 모델:" + name);
		System.out.println("제조사:" + supply);
		System.out.println("차량가격:" + price);}
		
}

public class Test13 {
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		GoodCar aa= new GoodCar();
		aa.name="Sonata";
		aa.supply="Hyundai";
		aa.price=30000000;
		aa.Print();
		
	}

}
