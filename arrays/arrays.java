import java.util.*;

public class arrays {
    // Linear search method
    public static void linearSearch(int numbers[], int key) {
        for (int i = 0; i < numbers.length; i++) {
            if (numbers[i] == key) {
                System.out.println("Key found at index: " + i);
                return;
            }
        }
        System.out.println("Key not found");
    }

    //smallest and largest number
    public static void smallest_largest(int numbers[]) {
        int largest= Integer.MIN_VALUE; //Integer.MIN_VALUE = -infinity
        int smallest= Integer.MAX_VALUE; //+infinity
        for (int i=0; i<numbers.length; i++) {
            if (numbers[i]>largest) {
                largest=numbers[i];
            }
            if (numbers[i]<smallest) {
                smallest=numbers[i];
            }
        }
        System.out.println("Largest number: " + largest);
        System.out.println("Smallest number: " + smallest);
    }

    //Binary Search
    //prerequisite - sorted array

    public static void main(String[] args) {
        int numbers[]= {1,2,3,4,5};
        // Array creation
        //int[] arr = new int[1];
        //String[] chars = {"a", "b", "c"};
        
        // Input
        Scanner sc = new Scanner(System.in);
        int[] marks = new int[3];
        
        for (int i = 0; i < marks.length; i++) {
            System.out.print("Enter marks: ");
            marks[i] = sc.nextInt();
        }
        
        System.out.println("Length of the array: " + marks.length); // Print length of array

        // Array is called by reference as parameter in a function

        
        System.out.print("Enter the key to search: ");
        int key = sc.nextInt();
        linearSearch(marks, key);
        smallest_largest(marks);
    }
}
