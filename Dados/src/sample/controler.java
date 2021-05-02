package sample;

import sample.model.Dado;
import sample.model.Jogador;

import java.util.ArrayList;
import java.util.List;

public class controler {

    public static class Tabuleiro {

        List<Jogador> jogadores;

        public Tabuleiro(List<String> nomesJogadores){
            jogadores = new ArrayList<>();

            for (int i = 0; i < nomesJogadores.size() ; i++) {
                Jogador jogador = new Jogador();
                jogador.setNome(nomesJogadores.get(i));
                jogadores.add(jogador);
            }

        }

        public void jogar(){
            //loop na lista de jogadores
            for(int i = 0; i < jogadores.size(); i++){
                //para cada jogador cria-se 2 dados
                Dado dado1 = new Dado();
                Dado dado2 = new Dado();
                dado1.lancar();
                dado2.lancar();
                //calcular total dos valores da face e salvar em jogador
                jogadores.get(i).setTotalPontos(dado1.getFace() + dado2.getFace());
                boolean venceu = jogadores.get(i).getTotalPontos() == 7;
                jogadores.get(i).setVenceu(venceu);
            }

        }

        public String toString(){
            return jogadores.toString();
        }


    }
}
