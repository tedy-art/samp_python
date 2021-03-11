#java
//java oops object
//my first programming in oops,parameter with method, object creation, method calling
public class display {

    //method with no parameter
    public void disply1(){

        System.out.println("method with no parameter..");
    }
    
    //method with single parameter
    public void disply2( int a){
        System.out.println("Method with one parameter "+ a);
    }
    public static void main(String[] args){
        //object creation
        display obj = new display();
        
        //object calling method
        obj.disply1();
        obj.disply2(30);
    }
}
