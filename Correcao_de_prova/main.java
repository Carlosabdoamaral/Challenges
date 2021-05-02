package sample.exercicios;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.Scanner;

public class ex007 {

    public static void main(String[] args){
        Scanner notas = new Scanner(System.in);

        String[] G; //Gabarito
        G = new String[11];
        G[1] = "a";
        G[2] = "b";
        G[3] = "c";
        G[4] = "d";
        G[5] = "a";
        G[6] = "b";
        G[7] = "c";
        G[8] = "d";
        G[9] = "a";
        G[10] = "b";

        String[] R; //Resposta Aluno
        R = new String[11];
        R[1] = "a";
        R[2] = "b";
        R[3] = "c";
        R[4] = "d";
        R[5] = "a";
        R[6] = "b";
        R[7] = "c";
        R[8] = "d";
        R[9] = "a";
        R[10] = "b";

        ArrayList<Integer> questoesCertas = new ArrayList();
        ArrayList<Integer> questoesErradas = new ArrayList();

       //Cada vez que o aluno acerta, cria uma parada no array


        System.out.println("CORREÇÃO");

        if (G[1] == R[1]){
            System.out.println("1 - Certa");
            questoesCertas.add(1);

        } else{
            System.out.println("1 - Errada");
            questoesErradas.add(1);
        }

        if (G[2] == R[2]){
            System.out.println("2 - Certa");
            questoesCertas.add(1);
        } else{
            System.out.println("2 - Errada");
            questoesErradas.add(1);
        }

        if (G[3] == R[3]){
            System.out.println("3 - Certa");
            questoesCertas.add(1);
        } else{
            System.out.println("3 - Errada");
            questoesErradas.add(1);
        }

        if (G[4] == R[4]){
            System.out.println("4 - Certa");
            questoesCertas.add(1);
        } else{
            System.out.println("4 - Errada");
            questoesErradas.add(1);
        }

        if (G[5] == R[5]){
            System.out.println("5 - Certa");
            questoesCertas.add(1);
        } else{
            System.out.println("5 - Errada");
            questoesErradas.add(1);
        }

        if (G[6] == R[6]){
            System.out.println("6 - Certa");
            questoesCertas.add(1);
        } else{
            System.out.println("6 - Errada");
            questoesErradas.add(1);
        }

        if (G[7] == R[7]){
            System.out.println("7 - Certa");
            questoesCertas.add(1);
        } else{
            System.out.println("7 - Errada");
            questoesErradas.add(1);
        }

        if (G[8] == R[8]){
            System.out.println("8 - Certa");
            questoesCertas.add(1);
        } else{
            System.out.println("8 - Errada");
            questoesErradas.add(1);
        }

        if (G[9] == R[9]){
            System.out.println("9 - Certa");
            questoesCertas.add(1);
        } else{
            System.out.println("9 - Errada");
            questoesErradas.add(1);
        }

        if (G[10] == R[10]){
            System.out.println("10 - Certa");
            questoesCertas.add(1);
        } else{
            System.out.println("10 - Errada");
            questoesErradas.add(1);
        }

        System.out.println(" ");

        if (questoesCertas.size() >= 6){
            System.out.println("O aluno está aprovado, pois tirou: " + questoesCertas.size());
        }else if(questoesErradas.size() >= 4){
            System.out.println("O aluno está reprovado, pois tirou " + (10 - questoesErradas.size()));
        }


    }
}
