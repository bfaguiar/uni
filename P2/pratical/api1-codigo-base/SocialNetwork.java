/** //para meter as "@" é necessário meter "/**"
 * 
 * @author Professores da Universidade
 * 
 */

public class SocialNetwork {

		private Person[] members;
		private int numMembers = 0;
		private int sizeExpansion= 0;
		private Post[] posts;
		private int numPosts = 0;
   /**
    * Construtor de objectos da classe SocialNetwork.
    * @param  maxSize Capacidade inicial do vector de membros
    *                 da rede social.
    * @param  sizeExpansion Numero de posicoes a acrescentar
    *                 ao vector quando este enche.
    */
   public SocialNetwork(int maxSize, int sizeExpansion) {

      this.sizeExpansion = sizeExpansion;
      members = new Person[maxSize];
      posts = new Post[100];
   }

   /**
    * Verifica se uma pessoa e' membro da rede social.
    * @param  personName Nome da pessoa.
    * @return true se a pessoa e' membro, false caso contrario
    *
    */
   public boolean personIsMember(String personName) {
      return memberIndex(personName) != -1;
      
   }

	public boolean postIsPublished(String titulo, String authorName) {
      return postIndex(titulo, authorName) != -1;
      
   }

   /**
    * Acrescenta uma nova pessoa como membro da rede social.
    * @param  person Uma pessoa que ainda nao seja membro.
    */
   public void addMember(Person p) {
      assert !personIsMember(p.name());

      if (numMembers==members.length) extendMemberArray();
      members[numMembers] = p;
      numMembers++;
   }
   
   public void addPost(Post p) {
      assert !postIsPublished(p.titulo(), p.author().name());

      if (numPosts==posts.length) extendPostsArray();
      posts[numPosts] = p;
      numPosts++;
   }

   /**
    * Devolve o numero de membros da rede social
    */
   public int numMembers() {
      return numMembers;
   }
   
   public int numPosts(){
		return numPosts;
	}

   /**
    * Devolve o indice de um membro no vector "members".
    * @param personName O nome da pessoa a procurar
    * @return O indice da pessoa no vector, ou -1 caso 
    *         não seja encontrada
    */
  
    
   private int memberIndex(String personName) {
      for(int m=0; m<numMembers(); m++) {
         if (members[m].name().equals(personName))
            return m;
      }
      return -1;
   }
   
   private int postIndex(String titulo, String authorName) {
      for(int m=0; m<numPosts(); m++) {
         if (posts[m].titulo().equals(titulo) && posts[m].author().name().equals(authorName))
            return m;
      }
      return -1;
   }

   /**
    * Expande a dimensao do vector "members", quando
    * este enche.
    */
   private void extendMemberArray() {
      Person[] newmembers = new Person[members.length+sizeExpansion];
      System.arraycopy(members,0,newmembers,0,numMembers);
      members = newmembers;
   }
	
private void extendPostsArray() {
      Post[] newPosts = new Post[100+sizeExpansion];
      System.arraycopy(posts,0,newPosts,0,numPosts);
      posts = newPosts;
   }
   
   
	public Person getPerson(int pos){
		return members[pos];
	}
	
	public Post getPost(int pos){
		return posts[pos];
	}

}

