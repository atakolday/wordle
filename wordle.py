from english_words import english_words_alpha_set
from collections import Counter, OrderedDict

five_letter = [word for word in list(english_words_alpha_set) if len(word) == 5]                                            # ALL FIVE LETTER WORDS FROM english_words
five_letter += ['tipsy'] + ['fewer'] + ['trove'] + ['drugs'] + ['drums'] + ['lowly'] + ['trope'] + ['heist'] + ['homer']    # ADDED WORDS AFTER TRIALS
words = [word for word in five_letter if word[0].lower() == word[0]]

def probs(w=words):

    def letter_prob(char):

        """
        Takes in a letter (char), returns a list of the
        likelihood (probability) of that letter appearing
        in each index of a given five-letter word.
        """

        word_list = [word for word in w if char in word]

        lst = []
        for i in range(5):
            prob = len([word for word in word_list if word[i] == char]) / len(word_list)
            lst.append(round(prob, 4))

        return lst

    def prob_list(char: str):

        """
        Takes in a letter (char), returns a list of the
        total probabilities of that letter appearing in a
        given five-letter words, factoring in the total number
        of repetitions of that letter in all five-letter words.
        """

        cw = [Counter(word) for word in w]

        i = 1
        sum_words = Counter()
        while i < len(cw):
            sum_words += cw[i-1] + cw[i]
            i += 1

        ordered_cw = dict(OrderedDict(sorted(sum_words.items())))        # Dictionary of letters and their number of repetitions in words

        return [(prob * ordered_cw[char] / sum(ordered_cw.values())) for prob in letter_prob(char)]

    def percent_dict(w):

        """
        Takes in a list of words, returns a Dictionary
        containing the words in the word list as [key],
        and the combined probabilities as the [value].
        """

        w_percent = dict()

        for word in w:
            lst = []
            for char in word:
                lst.append(prob_list(char)[word.index(char)])
            w_percent[word] = round(sum(lst) * 100, 4)

        return w_percent


    return percent_dict(w)



def Wordle(w=words):

    if len(w) == 0:
        print('')
        print('')
        print("RESULT")
        print('')
        print("Uh oh! No such words exist.")

    elif len(w) == 1:
        print('')
        print('')
        print("RESULT")
        print('')
        print("Congratulations! Today's Wordle is: ", w[0])
        print('')
        print('')

    else:

        print('')
        possible_words = input("Before we start, would you like to see a list of possible words? [y/n] ")
        print('')
        if possible_words == 'y':

            w_percent = probs(w)
            ordered_percent = dict(OrderedDict(sorted(w_percent.items(), key=lambda x: x[1], reverse=True)))

            dict_words = list(ordered_percent.keys())
            dict_probs = list(ordered_percent.values())

            i = 0
            while i < len(ordered_percent):

                if i > 9:
                    break

                print(f"{i+1}) {dict_words[i]}") #, {round(dict_probs[i], 2)}%")
                i+= 1

            print('')

        char = input("Give me a letter: ")
        exist = input("Does the letter exist? [y/n] ")
        if exist == 'y':

            char_exist = [word for word in w if char in word]

            position = input("Do you know where it is located? [y/n] ")
            if position == 'y':

                location = input("Okay, where is it? [1, 2, 3, 4, or 5] ")
                words = [word for word in char_exist if word[int(location)-1] == char]

                print('')
                print(f"Gotcha! The #{location} letter of the word is {char}!")
                print('')

                Wordle(words)

            else:

                non_pos = input('Okay, whis position did you try? [1, 2, 3, 4, or 5] ')
                words = [word for word in char_exist if word[int(non_pos)-1] != char]

                print('')
                print(f"Gotcha! The #{non_pos} letter of the word is not {char}!")
                print('')

                Wordle(words)
        else:

            words = [word for word in w if char not in word]

            Wordle(words)


print('')
print('')
