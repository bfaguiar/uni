package exercicio1;

import java.util.ArrayList;

public class Disciplina {
	
	String nomeDisciplina;
	String areaCientifica;
	int ects;
	Professor responsavel;
	ArrayList<Estudante> alunos = new ArrayList<>();
	
	public Disciplina(String nomeDisciplina, String areaCientifica, int ects, Professor responsavel) {
		this.nomeDisciplina = nomeDisciplina;
		this.areaCientifica = areaCientifica;
		this.ects = ects;
		this.responsavel = responsavel;
	}
	
	public boolean addAluno(Estudante est) { 
		if (alunos.contains(est)) {
			return false;
		} else { alunos.add(est); }
		
		return false;
	}
	
	public boolean delAluno(int nMec) {
		//Estudante aux.
		if(alunos.contains(nMec)) {
			return false;
		} else { alunos.remove(nMec); }
		return false;
	}
	
	public boolean alunoInscrito(int nMec) {
		if(alunos.contains(nMec)) {
			return true;
		} else return false;
	}
	
	public int numAlunos() {
		int count = 0;
		for (int i = 0; i < alunos.size(); i++) {
			Estudante alun = alunos.get(i);
			if( alunoInscrito(alun.nmec())) {
				count++;
			}
		}
		return count;
	}

	@Override
	public String toString() {
		return "Disciplina [alunos=" + alunos + ", responsavel=" + responsavel + ", nomeDisciplina=" + nomeDisciplina
				+ ", areaCientifica=" + areaCientifica + ", ects=" + ects + "]";
	}
	
	public Estudante[] getAlunos() {
		
		return (Estudante[]) alunos.toArray();
	}
	
//	public Estudante[] getAlunos(String tipo) {
//		Disciplina aux = null;
//		if (aux.areaCientifica.equals(tipo)) {
//			
//		}
//	}
	
	public Estudante[] getAlunos(String tipo){
		Estudante alutype[] = new Estudante[0];
		
		for(int i=0;i<alunos.size();i++){
			if(alunos.get(i).getClass().getSimpleName().equals(tipo)){
				alutype[i] = (alunos.get(i));
			}
		}
		
		return alutype;
	}
	
	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Disciplina other = (Disciplina) obj;
		if (!alunos.equals(other.alunos))
			return false;
		if (areaCientifica == null) {
			if (other.areaCientifica != null)
				return false;
		} else if (!areaCientifica.equals(other.areaCientifica))
			return false;
		if (ects != other.ects)
			return false;
		if (nomeDisciplina == null) {
			if (other.nomeDisciplina != null)
				return false;
		} else if (!nomeDisciplina.equals(other.nomeDisciplina))
			return false;
		if (responsavel == null) {
			if (other.responsavel != null)
				return false;
		} else if (!responsavel.equals(other.responsavel))
			return false;
		return true;
	}

	
	
}
