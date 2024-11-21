public class Word {

    public static String showLetters(String word, String guess) {

        String string = "";
        boolean match = false;
        for (int i = 0; i < word.length(); i++) {
            match = false;
            for (int j = 0; j < guess.length(); j++) {
                
                if (guess.charAt(j) == word.charAt(i)) {
                    string += word.charAt(i);
                    match = true;
                }
                
            }
                if (!match) {
                    string += "_";
                    System.out.println(string);
                }
                
        }
        return string;
    }
}