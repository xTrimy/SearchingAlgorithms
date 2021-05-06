package searchingalgorithms;

import java.util.*;

/**
 *
 * @author Bodda
 */

public class SearchingAlgorithms 
{
    public static Scanner input = new Scanner(System.in);
    
    public static void main(String[] args) 
    {
        boolean[][] visited;
        int Start_X, Start_Y, Goal_X, Goal_Y;
        
        int Table[][] = {   {1,0 ,1 ,0 ,1 ,0, 1},
                            {0, 1, 0, 1, 0, 1, 0},
                            {1, 0, 1, 0, 1, 0, 1},
                            {0, 1, 0, 1, 0, 1, 0},
                            {1, 0, 1, 0, 1, 0, 1},
                            {0, 1, 0, 0, 0, 1, 0}
        };
        
        visited = new boolean[Table.length][Table[0].length];
        
        for (int i = 0; i < Table.length; i++) 
        {
            for (int j = 0; j < Table[0].length; j++) 
            {
                visited[i][j] = false;
            }
        }
        
        System.out.println("GBFS \n\n");
        
        System.out.println("Enter The X And Y Coordinates Of Start");
        Start_X = Valid_Input("Invalid Value Of X Position, Try Again");
        Start_Y = Valid_Input("Invalid Value Of Y Position, Try Again");
        
        System.out.println("");
        
        System.out.println("Enter The X And Y Coordinates Of Goal");
        Goal_X = Valid_Input("Invalid Value Of X Position, Try Again");
        Goal_Y = Valid_Input("Invalid Value Of Y Position, Try Again");
        
        GBFS GBFS_Object = new GBFS();
        GBFS_Object.GreedyBestFirst(Table, visited, Table.length, Table[0].length, Start_X, Start_Y, Goal_X, Goal_Y);
        GBFS_Object.Display();
    }
    
    public static int Valid_Input(String Message)
    {
        int x = -1;
        String Temp = "";
        
        while(!Temp.matches("[0-9]+"))
        {
            Temp = input.next();
            if (Temp.matches("[0-9]+")) 
            {
                x = Integer.parseInt(Temp);
            }
            else
            {
                System.out.println(Message);
            }
        }
        return x;
    }
}
