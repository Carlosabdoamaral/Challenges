public class Ingresso {
    public static void main(String[] args) {
        //1 dia - 05 a 59 anos = R$190
        //Dia de semana - 20% desconto

        int quantidadeDias = 1; 

        int ingressoInteiroValor = 190; 
        int ingressoMeiaValor = 95;

        int quantidadeIngressoInteiro = 2;
        int quantidadeIngressoMeia = 1;

        System.out.println("Você tem que pagar: R$" + (ingressoInteiroValor * quantidadeIngressoInteiro + ingressoMeiaValor * quantidadeIngressoMeia * quantidadeDias));


    }
}
