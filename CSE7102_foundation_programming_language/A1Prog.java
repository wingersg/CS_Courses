import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map.Entry;
import java.util.Set;
/* Name@Zhengwen Zhang
 * SMU ID@ 47502277
 * Date@09/28/2017
 * The idea is to convert the text file into hashmap which contains
 * words and each word count, then sort the map according to count
 * then list the top 10 most frequent words.
 * reference1: http://javaconceptoftheday.com 
 * reference2: http://www.vogella.com/tutorials/JavaRegularExpressions/article.html
 */
 
public class wordSearchFromFile 
{   
    public static void main(String[] args) 
    {    
        //Creating wordCountMap to contains both keys and counts
         
        HashMap<String, Integer> wordCountMap = new HashMap<String, Integer>();
     
        BufferedReader reader = null;
         
        try
        {
            //create a BufferedReader object and import the a1words,txt file
             
            reader = new BufferedReader(new FileReader("C:/Users/F0600/Downloads/a1words.txt"));
             
            //read the first line into currentLine
             
            String currentLine = reader.readLine();
             
            while (currentLine != null)
            {    
                //split the currentLine into words, use regex to exclude white spaces and dot
            	// and ignore case and periods
                String[] words = currentLine.toLowerCase().split("[\\s ,\\.]+");
                 
                //Iterate each word
                 
                for (String word : words)
                {
                    //update the frequency if the word is inside the words
                     
                    if(wordCountMap.containsKey(word))
                    {    
                        wordCountMap.put(word, wordCountMap.get(word)+1);
                    }
                     
                    //if the word appear for the first time, use the word as key and 1 as value
                    else
                    {
                        wordCountMap.put(word, 1);
                    }
                }
                 
                //continue to read the next line
                 
                currentLine = reader.readLine();
            }
             
            Set<Entry<String, Integer>> entrySet = wordCountMap.entrySet();
            // create an arraylist
            List<Entry<String, Integer>> list = new ArrayList<Entry<String,Integer>>(entrySet);
            
            // arrange the words in descending order of the frequency
            Collections.sort(list, new Comparator<Entry<String, Integer>>() 
            {
                @Override
                public int compare(Entry<String, Integer> e1, Entry<String, Integer> e2) 
                {
                    return (e2.getValue().compareTo(e1.getValue()));
                }
            });
             
            System.out.println("Top 10 frequent words from input file are: \n" );
            //iterate the top 10 frequent words in the txt file
            for (int i=0;i<10;i++)
            {
            	System.out.println(list.get(i).getKey() + " "+ list.get(i).getValue());
            }
        } 
        //exception handling and close the reader
        catch (IOException e) 
        {
            e.printStackTrace();
        }
        finally
        {
            try
            {
                reader.close();           
            }
            catch (IOException e) 
            {
                e.printStackTrace();
            }
        }
    }    
}