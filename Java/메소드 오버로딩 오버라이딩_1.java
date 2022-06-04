class Sungjuk{
	public void Sungjuk(String name, int kor, int eng) {
		int sum=0;
		sum=kor+eng;
		System.out.println(name+" 성적 총점:"+sum);
	}
	
	public void Sungjuk(String name, int kor, int eng,int com) {
		int sum=0;
		sum=kor+eng+com;	
		System.out.println(name+" 성적 총점:"+sum);
	}
	
}
public class Test {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Sungjuk obj=new Sungjuk();
		obj.Sungjuk("임영웅", 90, 80);
		obj.Sungjuk("정동원",100, 90, 100);
	}

}
