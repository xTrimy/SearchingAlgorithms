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
        
        HashMap <String, Integer> Heuristic_Value = new HashMap <>();
        
        Heuristic_Value.put("Arad", 366);
        Heuristic_Value.put("Zerind", 374);
        Heuristic_Value.put("Timisoara", 329);
        Heuristic_Value.put("Sibiu", 400);
        Heuristic_Value.put("Oradea", 380);
        Heuristic_Value.put("Lugoj", 244);
        Heuristic_Value.put("RimnicuVilcea", 193);
        Heuristic_Value.put("Mehadia", 241);
        Heuristic_Value.put("Craiova", 160);
        Heuristic_Value.put("Pitesti", 10);
        Heuristic_Value.put("Fagaras", 176);
        Heuristic_Value.put("Dobreta", 242);
        Heuristic_Value.put("Bucharest", 0);
        Heuristic_Value.put("Giurgiu", 77);
        
        
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
//        GBFS_Object.GreedyBestFirst(Heuristic_Value, "Arad", "Bucharest");
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
