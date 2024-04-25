import java.util.Scanner;

public class 二分查找模板 {
//     public static void main(String[] args) {
//     Scanner sc = new Scanner(System.in);
//      sc.nextInt();
//      sc.close();
//     }
//     public void find(int[] a,int target){
//         int middle;
//         int left = 0;
//         int right = a.length-1;
//         while(left<=right){
//             middle = (left+right)/2;
//             if(a[middle]==target){
//                 System.out.println("找到目标值");
//                 break;
//             }
//             else if(a[middle]<target){
//                 left = middle+1;
//             }else{
//                 right = middle-1;
//             }
//     }
// }
public static void main(String[] args) {  
    Scanner scanner = new Scanner(System.in);  

    // 询问用户要输入数组的长度  
    System.out.println("请输入数组的长度：");  
    int length = scanner.nextInt();  

    // 创建指定长度的数组  
    int[] array = new int[length];  

    // 循环读取每个数组元素的值  
    for (int i = 0; i < length; i++) {  
        System.out.println("请输入数组的第 " + (i + 1) + " 个元素：");  
        array[i] = scanner.nextInt();  
    }  

    // 输出数组内容以验证输入  
    System.out.println("你输入的数组是：");  
    for (int element : array) {  
        System.out.print(element + " ");  
    }  

    // 关闭Scanner对象  
    scanner.close();  
}  
}