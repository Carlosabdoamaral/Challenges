package sample.model;

public class Jogador {

    private String nome;
    private boolean venceu;
    private int totalPontos;

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public boolean isVenceu(){
        return this.venceu;
    }

    public void setVenceu(boolean venceu){
        this.venceu = venceu;
    }

    public int getTotalPontos(){
        return this.totalPontos;
    }

    public void setTotalPontos(int totalPontos){
        this.totalPontos = totalPontos;
    }

    public String toString(){
        return "Jogador: "
                + nome
                + ", " + (venceu ? "ganhou o jogo" : "perdeu o jogo")
                + ", pontos:" + totalPontos;
    }

}

