import java.util.*;

public class arrays {
    public static void main(String[] args) {
        // creation
        int arr[] = new int[1];
        String chars[] = {"a", "b", "c"};
        
        // input
        Scanner sc = new Scanner(System.in);
        int marks[] = new int[3];
        
        for (int i = 0; i < 3; i++) {
            System.out.print("Enter marks: ");
            marks[i] = sc.nextInt();

        System.out.print(marks.length); // print length of array
        }
    }
}
