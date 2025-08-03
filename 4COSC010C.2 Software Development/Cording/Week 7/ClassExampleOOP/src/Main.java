//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {

        //Creating an object from Person Class
        //<ClassName> <ObjectNAme>= new <ConstructorName>(<ListofParameters>)
        Person p1=new Person("John",50,5.2);
        Person p2=new Person("Anne",20,5.1);
        Person p3=new Person("Paul",29,4.8);
        //Create object p4 using the default constructor
        Person p4=new Person();


        //Print the name of Person P1
        System.out.println(p1.getPersonName());
        //Print the age of person p3
        System.out.println(p3.getPersonAge());
        //Update the height of person P1 into 5.4;
        p1.setPersonHeight(5.4);
        //Display the height of person P1
        System.out.println(p1.getPersonHeight());

        p1.personName="AAAA";
    }
}