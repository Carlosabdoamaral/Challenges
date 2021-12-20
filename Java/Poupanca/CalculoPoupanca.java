public class CalculoPoupanca {
    public static void main(String[] args) {
        
        int valorRecebido = 100;
        int poupanca = 350;

        if(valorRecebido >= 50){
            System.out.println("Você deve depositar R$" + valorRecebido * 0.2 + " para a sua poupança");
            System.out.println("Você tem R$" + (valorRecebido + poupanca) + " na sua poupança");

        }else if(valorRecebido < 50){
            System.out.println("Você não precisa depositar os 20% de R$" + valorRecebido + ", acumule mais e tente novamente");
        }
    }
}
