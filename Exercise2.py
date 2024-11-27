def are_anagrams(TextOne, TextTwo):
    if (sorted(TextOne.lower()) == sorted(TextTwo.lower())):
        return TextOne + " et " + TextTwo + " sont des anagrammes."
    else:
        return TextOne + " et " + TextTwo + "ne sont pas des anagrammes."
 


