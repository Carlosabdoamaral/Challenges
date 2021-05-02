public class EntradaSite18 {
    public static void main(String[] args) {
        //entrada em site +18

        int idadeUser = 15;
        int idadeApp = 18;

        if(idadeUser >= 18 ){
            System.out.println("Você pode entrar");
        }else{
            System.out.println("Você poderá entrar no app em " + (idadeApp - idadeUser) + " anos");
        }
    }
}
