public class Desconto {
    public static void main(String[] args) {
        
        int idadeUsuario = 18;
        int quantidade = 3;  
             
        int valorProduto1 = 200;
        int valorProduto2 = 100;
        int valorProduto3 = 200;
        int valorProdutoTotal = (valorProduto1 + valorProduto2 + valorProduto3);


        if(valorProdutoTotal <= 200){
            System.out.println(("Desconto de 5% aplicado! Você deverá receber: " + valorProdutoTotal * 0.95));
            System.out.println();
            System.out.println("O valor da soma dos produos foi: " + valorProdutoTotal);
            System.out.println("A quantidade que o usuario pegou foi: " + quantidade);
            System.out.println("A idade do usuário é: " + idadeUsuario);
        }
        else if(valorProdutoTotal <= 400){
            System.out.println(("Desconto de 40% aplicado! Você deverá receber: " + valorProdutoTotal * 0.6));
            System.out.println();
            System.out.println("O valor da soma dos produos foi: " + valorProdutoTotal);
            System.out.println("A quantidade que o usuario pegou foi: " + quantidade);
            System.out.println("A idade do usuário é: " + idadeUsuario);
        }
        else if (valorProdutoTotal <= 600) {
            System.out.println(("Desconto de 50% aplicado! Você deverá receber: " + valorProdutoTotal * 0.5));
            System.out.println();
            System.out.println("O valor da soma dos produos foi: " + valorProdutoTotal);
            System.out.println("A quantidade que o usuario pegou foi: " + quantidade);
            System.out.println("A idade do usuário é: " + idadeUsuario);
        }
        else if (valorProdutoTotal > 600) {
            System.out.println(("Desconto de 60% aplicado! Você deverá receber: " + valorProdutoTotal * 0.4));
            System.out.println();
            System.out.println("O valor da soma dos produos foi: " + valorProdutoTotal);
            System.out.println("A quantidade que o usuario pegou foi: " + quantidade);
            System.out.println("A idade do usuário é: " + idadeUsuario);
        }
        

    }
}
