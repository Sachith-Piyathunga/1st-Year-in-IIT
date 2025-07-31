

public class Student {
    String name;
    int age;
    Student(String name,int age){

        //name = name;
        //age = age;
        this.name = name;
        this.age = age;

    }

    public static void main(String[] args) {

        Student obj = new Student("Sachinta",23);
        System.out.println(obj.name);
        System.out.println(obj.age);

    }
}