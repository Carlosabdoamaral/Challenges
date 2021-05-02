package sample;

import java.util.ArrayList;
import java.util.List;

public class Main {

    public static void main(String[] args) {
        List<String> nomes =
                new ArrayList<>();
        nomes.add("Emanuelly");
        nomes.add("Felipe");
        nomes.add("Ana Julia");
        nomes.add("Murilo");
        nomes.add("Lucca");
        nomes.add("Melisa");
        nomes.add("Rafaela");

        controler.Tabuleiro tabuleiro =
                new controler.Tabuleiro(nomes);

        tabuleiro.jogar();
        System.out.println(tabuleiro);

    }
}
