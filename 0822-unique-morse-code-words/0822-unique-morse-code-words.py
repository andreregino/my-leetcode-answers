class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:

        dict = {'a':".-", 'b':"-...", 'c':"-.-.", 'd':"-..", 'e':".", 'f':"..-.", 'g':"--.", 'h':"....", 'i':"..", 'j':".---", 'k':"-.-", 'l':".-..", 'm':"--", 'n':"-.", 'o':"---", 'p':".--.", 'q':"--.-", 'r':".-.", 's':"...", 't':"-", 'u':"..-", 'v':"...-", 'w':".--", 'x':"-..-", 'y':"-.--", 'z':"--.."}
        
        words_set = set()
        for word in words:
            generated_code = ""
            for w in word:
                generated_code += dict[w]
            words_set.add(generated_code)

        return len(words_set)    
        