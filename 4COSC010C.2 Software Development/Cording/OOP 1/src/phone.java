

public class phone {

    String name;
    String colour;
    int ram;

    public void call(){
        System.out.println("Take a call from " + name);

    }
    public void browseinternet(){
        System.out.println("browse internet ");

    }

    public static void main(String[] args) {
        phone phone1 = new phone();
        phone1.name = "samsung";
        phone1.colour = "blue";
        phone1.call();
        System.out.println(phone1.colour);

        phone phone2 = new phone();
        phone2.name = "LG";
        phone2.colour = "black";
        phone2.ram = 2;
        phone2.call();
        System.out.println(phone2.colour);

    }
}