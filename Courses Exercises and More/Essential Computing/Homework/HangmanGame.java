/* 
 * Code made by Vladyslav Horbatenko for Assigment 5
 * Date: 27.10.2023
 * Source of words: https://www.hangmanwords.com/words
 */

import java.util.Scanner;
import java.util.Random;

public class HangmanGame { //main class for the program
    private String secretWord; //setting up secret word as String
    private char[] wordToGuess; //setting up secret word as characters
    private int maxWrongGuesses; //maximum of wrong guesses (can be changed)
    private int wrongGuesses; //user's number of wrong guesses
    private Random rand = new Random();

    String[] words = { //all possible words for the game
        "abruptly", "absurd", "abyss", "affix", "askew", "avenue", "awkward", "axiom", "azure", "bagpipes",
        "bandwagon", "banjo", "bayou", "beekeeper", "bikini", "blitz", "blizzard", "boggle", "bookworm", "boxcar",
        "boxful", "buckaroo", "buffalo", "buffoon", "buxom", "buzzard", "buzzing", "buzzwords", "caliph", "cobweb",
        "cockiness", "croquet", "crypt", "curacao", "cycle", "daiquiri", "dirndl", "disavow", "dizzying", "duplex",
        "dwarves", "embezzle", "equip", "espionage", "euouae", "exodus", "faking", "fishhook", "fixable", "fjord",
        "flapjack", "flopping", "fluffiness", "flyby", "foxglove", "frazzled", "frizzled", "fuchsia", "funny",
        "gabby", "galaxy", "galvanize", "gazebo", "giaour", "gizmo", "glowworm", "glyph", "gnarly", "gnostic",
        "gossip", "grogginess", "haiku", "haphazard", "hyphen", "iatrogenic", "icebox", "injury", "ivory", "ivy",
        "jackpot", "jaundice", "jawbreaker", "jaywalk", "jazziest", "jazzy", "jelly", "jigsaw", "jinx", "jiujitsu",
        "jockey", "jogging", "joking", "jovial", "joyful", "juicy", "jukebox", "jumbo", "kayak", "kazoo", "keyhole",
        "khaki", "kilobyte", "kiosk", "kitsch", "kiwifruit", "klutz", "knapsack", "larynx", "lengths", "lucky",
        "luxury", "lymph", "marquis", "matrix", "megahertz", "microwave", "mnemonic", "mystify", "naphtha", "nightclub",
        "nowadays", "numbskull", "nymph", "onyx", "ovary", "oxidize", "oxygen", "pajama", "peekaboo", "phlegm", "pixel",
        "pizazz", "pneumonia", "polka", "pshaw", "psyche", "puppy", "puzzling", "quartz", "queue", "quips", "quixotic",
        "quiz", "quizzes", "quorum", "razzmatazz", "rhubarb", "rhythm", "rickshaw", "schnapps", "scratch", "shiv",
        "snazzy", "sphinx", "spritz", "squawk", "staff", "strength", "strengths", "stretch", "stronghold", "stymied",
        "subway", "swivel", "syndrome", "thriftless", "thumbscrew", "topaz", "transcript", "transgress", "transplant",
        "triphthong", "twelfth", "twelfths", "unknown", "unworthy", "unzip", "uptown", "vaporize", "vixen", "vodka",
        "voodoo", "vortex", "voyeurism", "walkway", "waltz", "wave", "wavy", "waxy", "wellspring", "wheezy", "whiskey",
        "whizzing", "whomever", "wimpy", "witchcraft", "wizard", "woozy", "wristwatch", "wyvern", "xylophone",
        "yachtsman", "yippee", "yoked", "youthful", "yummy", "zephyr", "zigzag", "zigzagging", "zilch", "zipper",
        "zodiac", "zombie"
    };
    
    public static void main(String[] args) { //main function where we set up game settings
        HangmanGame game = new HangmanGame(8); // change maxWrongGuesses number
        game.play();
    }
    
    public HangmanGame(int maxWrongGuesses) { //HandManGame where we assign most important variables and initial game start position
        int secretWordIndex = rand.nextInt(words.length); //selecting random number in length of words list
        secretWord = words[secretWordIndex]; //selecting random word from list

        this.wordToGuess = new char[secretWord.length()];
        for (int i = 0; i < secretWord.length(); i++) { //lopping trough word and placing . instead
            wordToGuess[i] = '.';
        }
        this.maxWrongGuesses = maxWrongGuesses;
        this.wrongGuesses = 0; //setting number of wrong guesses to 0
    }

    public boolean isGameOver() { //function that decide weather the play function gona be looping
        return wrongGuesses >= maxWrongGuesses || secretWord.equals(String.valueOf(wordToGuess)); 
        //if user guesses the word or used all attempts - function will send False to "play" and stop the loop
    }

    public void displayCurrentWord() { //showing user what he already guessed and where is this characters are in the word
        System.out.println("Current word: " + String.valueOf(wordToGuess));
    }

    public void makeGuess(char guess) { //function that take users input and checks if the guess is correct
        if (secretWord.contains(String.valueOf(guess))) {
            for (int i = 0; i < secretWord.length(); i++) { //loop itself that check our input
                if (secretWord.charAt(i) == guess) {
                    wordToGuess[i] = guess; //if correct assign inputted character instead of "."
                }
            }
        } else {
            wrongGuesses++; //or +1 to wrong guesses
            System.out.println("Wrong guess! You have " + (maxWrongGuesses - wrongGuesses) + " attempts left.");
        }
    }

    public void play() { //play functoin that sets the game up
        Scanner scanner = new Scanner(System.in);
        System.out.println("Welcome to Hangman!");
        System.out.println("You have " + maxWrongGuesses + " attempts to guess the word.");

        while (!isGameOver()) { //main game function that loops until user losses or guesses the word
            displayCurrentWord(); //calling function to show user dots instead of word (basically its length)
            System.out.print("Guess a letter: ");
            char guess = scanner.next().charAt(0); //taking input from user
            makeGuess(guess); //sending input to function to check it its correct or wrong
        }

        if (secretWord.equals(String.valueOf(wordToGuess))) {
            System.out.println("Congratulations, you've guessed the word: " + secretWord); //if user wins
        } else {
            System.out.println("Sorry, you've run out of attempts. The word was: " + secretWord); //if user loses
        }
        scanner.close(); //after we stop taking any inputs
    }
}