
class Sales{
	String title;
	int qty;
	
	public Sales(String t) {
		
		
		
		
	}
	public Sales(String t, int q) {
		title=t;
		qty=q;
		
		
	}
	public void SalesPrint() {
		if(this.title.equals("노트북") ){
			System.out.println("판매품목:"+this.title+ "\t"+"수량:"+this.qty+ "\t"+"가격:"+500000*this.qty);
			
		}else {
			System.out.println("판매품목:"+this.title+ "\t"+ "수량:"+this.qty+ "\t"+ "가격:"+700000*this.qty);
		}
		
	}
	
}



public class Devices {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Sales aa= new Sales("노트북",2);
		Sales bb=new Sales("스마트폰",5);
		aa.SalesPrint();
		bb.SalesPrint();
	
		
			
	}

}
