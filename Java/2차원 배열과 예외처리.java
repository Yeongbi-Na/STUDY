public class Test1_17100081 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int jumsu[][]= {
				{90, 90, 80},
				{80, 95, 80},
				{80, 80, 90},
				{90, 70, 95},
				{60, 65, 70}};
		int sum=0;
		double avg=0;
		
		System.out.println("\t"+"**성 적 표**");
		
		for(int i=0;i<jumsu.length;i++) {
			System.out.printf("%d번",i+1);
			sum=0;
			avg=0;
			for(int j=0;j<jumsu[i].length;j++) {
				sum+=jumsu[i][j];
				System.out.printf("%d ", jumsu[i][j]);
				
				
				
			}
			avg=(double)sum/(double)jumsu[i].length;
			System.out.printf("%d %.2f",sum, avg);
			System.out.println();
			
		}

		
		
			
	}

}
