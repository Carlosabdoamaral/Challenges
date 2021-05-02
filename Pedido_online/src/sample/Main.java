package sample;

import sample.model.ItensDoPedido;
import sample.model.Produto;
import sample.model.Pedido;

public class Main {

    public static void main(String[] args) {
        Pedido pedido = new Pedido();
        pedido.setDesc("Ifood");
        pedido.setData("03/03/03");
        pedido.addProduto("MC lanche Feliz", 90.0);

        System.out.println(pedido);
    }
}