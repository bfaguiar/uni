package exercicio3;

public class video {
	
		public enum categoria {
			 
			 M10(10, "Maiores de 10 anos"), 
			 M12(12, "Maiores de 12 anos"), 
			 M14(14, "Maiores de 14 anos"), 
			 M16(16, "Maiores de 16 anos"), 
			 M18(18, "Maiores de 18 anos");
			
			private int idd;
			private String iddSTR;
			
			private categoria(int idd, String iddSTR) {
				this.idd = idd;
				this.iddSTR = iddSTR;
			}
		
		public int getIdade() {
				return idd;
			}


			public String getStringIdade() {
				return iddSTR;
			}
		}

		private String titulo;
		private categoria idade;
		private String cat;
		
		
		
		video(String titulo, categoria idade, String cat) {
			this.titulo = titulo;
			this.idade = idade;
			this.cat = cat;
		}
		
		
		categoria idade() { return idade; }
		String titulo() { return titulo; }
		String categoria() { return cat; }
		
		void getVideo(video objVid) {
			System.out.println("");
			System.out.println("NOME DO VIDEO: " + objVid.titulo);
			System.out.println("IDADE: " + objVid.idade);
			System.out.println("CATEGORIA: " + objVid.cat);
		
		}
}
