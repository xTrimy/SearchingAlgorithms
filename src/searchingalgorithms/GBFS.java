package searchingalgorithms;

import java.util.*;

/**
 *
 * @author Bodda
 */

public class GBFS 
{
    public static int Initial_Minimum;
    public static int Goal_X, Goal_Y;
    public static ArrayList <Pair> Path;
    
    GBFS()
    {
        Initial_Minimum = Integer.MAX_VALUE;
        Path = new ArrayList<>();
    }
    
    void GreedyBestFirst ( int Table[][], boolean Visited[][], int X_Dimension, int Y_Dimension, int Start_X, int Start_Y, int GoalX, int GoalY ) 
    {
        Goal_X = GoalX;
        Goal_Y = GoalY;

        Comparator <State> Comparator_Object = new Compare_Pairs();
        PriorityQueue <State> priorityQueue = new PriorityQueue <>(Comparator_Object);

        Visited [Start_X][Start_Y] = true;
        State Start_Index = new State(Start_X, Start_Y, 0, X_Dimension, Y_Dimension, Visited);
        priorityQueue.add(Start_Index);

        while(!priorityQueue.isEmpty()) 
        {
            State Current_Index = priorityQueue.remove();
            
            Start_X = Current_Index.Start_X;
            Start_Y = Current_Index.Start_Y;

            if (Current_Index.Start_X==Goal_X && Current_Index.Start_Y==Goal_Y)
            {
                if (Current_Index.Cost < Initial_Minimum)
                {
                    Initial_Minimum = Current_Index.Cost;
                    Path = Current_Index.Path;
                    Path.add(new Pair(Start_X, Start_Y));
                }
            }

            if (Start_X-1 >= 0 && !Current_Index.visited[Start_X-1][Start_Y] && Table[Start_X-1][Start_Y] == 0)
            {
                Current_Index.visited[Start_X-1][Start_Y] = true;
                State Temp = new State(Start_X-1, Start_Y, Current_Index.Cost + 1, X_Dimension, Y_Dimension, Current_Index.visited);
                Temp.New_Pair(Current_Index.Path, Start_X, Start_Y);
                priorityQueue.add(Temp);
            }
            
            if (Start_X+1 < X_Dimension && !Current_Index.visited[Start_X+1][Start_Y] && Table[Start_X+1][Start_Y] == 0)
            {
                Current_Index.visited[Start_X+1][Start_Y] = true;
                State Temp = new State(Start_X+1, Start_Y, Current_Index.Cost + 1, X_Dimension, Y_Dimension, Current_Index.visited);
                Temp.New_Pair(Current_Index.Path, Start_X, Start_Y);
                priorityQueue.add(Temp);
            }
            
            if (Start_Y-1 >= 0 && !Current_Index.visited[Start_X][Start_Y-1] && Table[Start_X][Start_Y-1] == 0)
            {
                Current_Index.visited[Start_X][Start_Y-1] = true;
                State Temp = new State(Start_X, Start_Y-1, Current_Index.Cost + 1, X_Dimension, Y_Dimension, Current_Index.visited);
                Temp.New_Pair(Current_Index.Path, Start_X, Start_Y);
                priorityQueue.add(Temp);
            }
            
            if (Start_Y+1 < Y_Dimension && !Current_Index.visited[Start_X][Start_Y+1] && Table[Start_X][Start_Y+1] == 0)
            {
                Current_Index.visited[Start_X][Start_Y+1] = true;
                State Temp = new State(Start_X, Start_Y+1, Current_Index.Cost + 1, X_Dimension, Y_Dimension, Current_Index.visited);
                Temp.New_Pair(Current_Index.Path, Start_X, Start_Y);
                priorityQueue.add(Temp);
            }

            if (Start_X-1 >= 0 && Start_Y-1 >= 0 && !Current_Index.visited[Start_X-1][Start_Y-1] && Table[Start_X-1][Start_Y-1] == 0)
            {
                Current_Index.visited[Start_X-1][Start_Y-1] = true;
                State Temp = new State(Start_X-1, Start_Y-1, Current_Index.Cost + 1, X_Dimension, Y_Dimension, Current_Index.visited);
                Temp.New_Pair(Current_Index.Path, Start_X, Start_Y);
                priorityQueue.add(Temp);
            }
            
            if (Start_X-1 >= 0 && Start_Y+1 < Y_Dimension && !Current_Index.visited[Start_X-1][Start_Y+1] && Table[Start_X-1][Start_Y+1] == 0)
            {
                Current_Index.visited[Start_X-1][Start_Y+1] = true;
                State temp = new State(Start_X-1, Start_Y+1, Current_Index.Cost + 1, X_Dimension, Y_Dimension, Current_Index.visited);
                temp.New_Pair(Current_Index.Path, Start_X, Start_Y);
                priorityQueue.add(temp);
            }
            
            if (Start_X+1 < X_Dimension && Start_Y-1 >= 0 && !Current_Index.visited[Start_X+1][Start_Y-1] && Table[Start_X+1][Start_Y-1] == 0)
            {
                Current_Index.visited[Start_X+1][Start_Y-1] = true;
                State Temp = new State(Start_X+1, Start_Y-1, Current_Index.Cost + 1, X_Dimension, Y_Dimension, Current_Index.visited);
                Temp.New_Pair(Current_Index.Path, Start_X, Start_Y);
                priorityQueue.add(Temp);
            }
            
            if (Start_X+1 < X_Dimension && Start_Y+1 < Y_Dimension && !Current_Index.visited[Start_X+1][Start_Y+1] && Table[Start_X+1][Start_Y+1] == 0) 
            {
                Current_Index.visited[Start_X+1][Start_Y+1] = true;
                State Temp = new State(Start_X+1, Start_Y+1, Current_Index.Cost+1, X_Dimension, Y_Dimension, Current_Index.visited);
                Temp.New_Pair(Current_Index.Path, Start_X, Start_Y);
                priorityQueue.add(Temp);
            }
        }
    }
    
    public static int Calculate_Distance(int X1, int Y1, int X2, int Y2) 
    {
        return (int) Math.sqrt(Math.pow(X1 - X2, 2) + Math.pow(Y1 - Y2, 2));
    }
    
    void Display() 
    {
        System.out.print("Cost: " + Path.size() + "\nPath: {");
        for(int i = 0;i < Path.size();i++) 
        {
            System.out.print("(" + Path.get(i).X + ", " + Path.get(i).Y + ")");
            if ( i != Path.size()-1 ) System.out.print(" ");
        } System.out.println("}");
    }
}

class Compare_Pairs implements Comparator<State> 
{
    @Override
    public int compare(State State_Object_1, State State_Object_2)
    {
        int Distance_1 = GBFS.Calculate_Distance(State_Object_1.Start_X, State_Object_2.Start_X, GBFS.Goal_X, GBFS.Goal_Y);
        int Distance_2 = GBFS.Calculate_Distance(State_Object_2.Start_X, State_Object_2.Start_Y, GBFS.Goal_X, GBFS.Goal_Y);
        
        if ( Distance_1 > Distance_2 ) return 1;
        else if ( Distance_1 < Distance_2 ) return -1;
        return 0;
    }
}

class Pair 
{
    int X, Y;
    
    Pair(int x, int y)
    {
        X = x;
        Y = y;
    }
}

class State 
{
    int Start_X, Start_Y, Cost;
    ArrayList <Pair> Path;
    boolean visited [][];
    
    State( int Start_x, int Start_y, int cost, int X_Dimension, int Y_Dimension, boolean v[][] ) 
    {
        Start_X = Start_x;
        Start_Y = Start_y;
        Cost = cost;
        Path = new ArrayList <>();
        
        visited = new boolean[X_Dimension][Y_Dimension];
        for(int i = 0;i < X_Dimension;i++)
        {
            System.arraycopy(v[i], 0, visited[i], 0, Y_Dimension);
        }
    }
    
    void New_Pair(ArrayList<Pair> visited, int i, int j)
    {
        for(int x = 0;x < visited.size();x++) 
            Path.add(visited.get(x));
        
        Path.add(new Pair(i, j));
    }
}
