

public class Main {

    public static void main(String[] args) {

        String srt = "Sachintha";
        String s = "Chamod";

        System.out.println(srt.length());
        System.out.println(srt.toUpperCase());
        System.out.println(srt.toLowerCase());
        System.out.println(srt + " " + s);
        System.out.println(srt.concat(s)); // same method in  line13
        System.out.println(srt.concat(" ").concat(s)); // same method in line 13
        System.out.println(s.replace("Chamod","Lord")); //replace variable 2 line 8

    }
}