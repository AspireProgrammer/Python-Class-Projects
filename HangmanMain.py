# Rebekah Shi
# 2/15/24
# Project 3 Hangman with Functions   
import random

# first, define the functions and the global variables to access
# global number_of_incorrect_guess
number_of_incorrect_guess = 0
blank = ''
is_game_done = False

def ask_user_for_guess(letters_guessed):
    if len(user_input) >= 2:
        print('You can only guess a single letter')
    if user_input in letters_guessed[:-2]:
        print('Sorry, you have already tried that letter. Try again')

def print_hidden_word(hidden_word, letters_guessed):
    counter = 0
    global blank
    # for each letter in hidden word list, search through with user input. if the letter in hidden word
    # match the user input, store the number of guessed letters and display
    # then search string for that letter and  return index and replace that blank to letter
    global number_of_incorrect_guess
    if hidden_word_s.find(user_input) == -1:
        print("sorry, incorrect: ")
        number_of_incorrect_guess = number_of_incorrect_guess + 1
    for character in hidden_word:
        if character == user_input.lower():
            blank = ''.join(blank)
            blank = blank[:counter] + hidden_word[counter] + blank[counter + 1:]
            print(blank[:counter])
            print(blank)
        counter = counter + 1
    counter = 0
    return number_of_incorrect_guess


def print_gallows(number_of_body_parts):
    if number_of_incorrect_guess  == 0:
        print("__________")
        print("|    |")
        print("|     ")
        print("|  ")
        print('|   ')
        print('|  ')
        print('|_________')
    if number_of_incorrect_guess  == 1:
        print("__________")
        print("|    |")
        print("|    0")
        print("|  ")
        print('|   ')
        print('|  ')
        print('|_________')
    if number_of_incorrect_guess  == 2:
        print("__________")
        print("|    |")
        print("|    0 ")
        print("|    |")
        print('|   ')
        print('|  ')
        print('|_________')
    if number_of_incorrect_guess == 3:
        print("__________")
        print("|    |")
        print("|    0 ")
        print("|  --|")
        print('|   ')
        print('|  ')
        print('|_________')
    if number_of_incorrect_guess  == 4:
        print("__________")
        print("|    |")
        print("|    0 ")
        print("|  --|--")
        print('|   ')
        print('|  ')
        print('|_________')
    if number_of_incorrect_guess  == 5:
        print("__________")
        print("|    |")
        print("|    0 ")
        print("|  --|--")
        print('|   /')
        print('|  ')
        print('|_________')
    if number_of_incorrect_guess  == 6:
        print("__________")
        print("|    |")
        print("|    0 ")
        print("|  --|--")
        print('|   /\\')
        print('|  ')
        print('|_________')


def is_game_over(hidden_word, letters_guessed, number_of_incorrect_guess):
    global is_game_done
    if number_of_incorrect_guess == 6:
        print('Game Over. You Lost. Word was: ' + hidden_word_s)
        is_game_done = True
    if blank == hidden_word_s:
        print('You won!')
        is_game_done = True

    # pick a random word by generating a random number that corresponds with the length of the list
word_list = ["able", "about", "again", "air", "all", "always", "and", "answer", "any", "around", "ask", "at",
             "back", "be", "before", "best", "better", "between", "black", "body", "book", "boy", "brother", "but",
             "call", "can", "car", "careful", "cat", "chair", "chance", "cheese", "child", "cinema", "clean",
             "clear", "close", "cold", "come", "could", "country", "cry", "cut", "dance", "daughter", "day",
             "dinner", "do", "doctor", "document", "dog", "door", "down", "dream", "drink", "each", "easy", "eat",
             "egg", "eight", "end", "everything", "explain", "eye", "face", "family", "father", "find", "fire",
             "first", "for", "friend", "from", "game", "get", "girl", "give", "good", "hand", "head", "help", "her",
             ""
             "", "home", "idea", "important", "information", "inside", "interesting", "job", "kind", "know",
             "land", "learn", "life", "light", "live", "long", "make", "man", "many", "may", "money", "more",
             "morning", "move", "my", "name", "new", "no", "now", "often", "one", "open", "or", "out", "page",
             "paper", "park", "pay", "peace", "pen", "people", "person", "picture", "place", "play", "please",
             "popular", "prefer", "problem", "put", "question", "reach", "read", "ready", "red", "rest", "rich",
             "right", "river", "road", "room", "run", "same", "say", "school", "second", "see", "send", "set",
             "she", "ship", "shop", "should", "show", "sit", "small", "so", "some", "son", "soon", "speak", "stand",
             "start", "stone", "stop", "student", "such", "table", "that", "the", "there", "they", "thing", "think",
             "this", "time", "today", "two", "understand", "up", "very", "visit", "wait", "want", "we", "what",
             "where", "why", "word", "work", "write", "you	across", "action", "after", "against", "age",
             "almost", "alone", "already", "also", "anything", "army", "art", "away", "bad", "beautiful", "because",
             "become", "bed", "big", "box", "bread", "breakfast", "bring", "bus", "buy", "camera", "care", "carry",
             "catch", "cause", "certain", "change", "chief", "church", "city", "class", "company", "confirm",
             "continue", "control", "corner", "cost", "cover", "culture", "dead", "dear", "decision", "deep",
             "describe", "desert", "die", "difficult", "distance", "dress", "drive", "dry", "east", "education",
             "enjoy", "enough", "evening", "every", "example", "expect", "expensive", "fact", "fast", "feel", "few",
             "fight", "flower", "food", "free", "full", "garage", "garden", "gold", "great", "green", "group",
             "happy", "hard", "have", "here", "hope", "house", "how", "ill", "impossible", "include", "industry",
             "interest", "into", "invite", "island", "journey", "juice", "keep", "late", "leave", "let", "letter",
             "like", "look", "meet", "member", "miss", "moment", "month", "most", "mother", "much", "must", "need",
             "never", "next", "nothing", "old", "on", "only", "other", "own", "part", "personal", "phone", "plan",
             "player", "police", "position", "possible", "power", "present", "president", "pretty", "price",
             "product", "provide", "public", "quite", "rather", "real", "reason", "receive", "record", "remain",
             "remember", "report", "result", "return", "round", "sad", "save", "sea", "seat", "service", "several",
             "shall", "side", "single", "sister", "sleep", "something", "sorry", "sound", "south", "spring", "star",
             "stay", "story", "street", "strong", "study", "sun", "sweet", "system", "take", "talk", "teacher",
             "tell", "their", "then", "through", "together", "too", "true", "try", "under", "use", "view", "voice",
             "water", "way", "week", "which", "who", "wife", "with", "woman", "world", "yes	above", "accident",
             "act", "add", "address", "ago", "airport", "along", "among", "another", "appear", "apple", "arm",
             "baby", "bear", "begin", "behind", "believe", "blood", "blue", "both", "break", "building", "built",
             "business", "card", "case", "central", "century", "check", "chicken", "choose", "clock", "collect",
             "colour", "common", "computer", "condition", "consider", "course", "court", "crazy", "cross", "cup",
             "dangerous", "dark", "decide", "depend", "desk", "different", "direct", "direction", "discuss",
             "dollar", "draw", "during", "ear", "early", "earth", "edge", "effect", "even", "ever", "examine",
             "exchange", "fall", "field", "film", "fine", "fish", "floor", "fly", "form", "fruit", "general",
             "gift", "glad", "glass", "government", "grow", "half", "happen", "hear", "heart", "high", "hold",
             "hour", "ice", "illness", "imagine", "immediately", "increase", "inform", "insect", "introduce",
             "jump", "just", "key", "less", "line", "little", "love", "low", "magazine", "mark", "material", "mean",
             "meat", "meeting", "milk", "mind", "minute", "nature", "near", "not", "number", "off", "office",
             "once", "order", "over", "parent", "party", "pass", "past", "patient", "pencil", "perhaps", "piece",
             "pink", "plate", "poor", "post", "produce", "protect", "pull", "purpose", "quick", "race", "radio",
             "rain", "really", "remove", "reply", "respect", "ride", "ring", "rise", "rock", "search", "secret",
             "sell", "sense", "sharp", "shoe", "short", "similar", "simple", "since", "situation", "slow", "smile",
             "snow", "sometimes", "song", "speed", "sport", "state", "station", "still", "success", "sugar",
             "summer", "sure", "tall", "tea", "television", "test", "than", "though", "ticket", "town", "travel",
             "tree", "turn", "upon", "usual", "valley", "value", "virus", "walk", "war", "watch", "well", "when",
             "while", "will", "window", "would", "your", "accept", "account", "actor", "advance", "advantage",
             "afternoon", "agree", "amount", "angry", "arrange", "article", "attack", "available", "bag", "bank",
             "below", "bird", "boat", "borrow", "bottle", "bridge", "brown", "build", "busy", "butter", "cake",
             "captain", "centre", "cheap", "chocolate", "choice", "cigarette", "cloth", "cloud", "club", "coast",
             "coat", "coffee", "college", "comfortable", "cottage", "cream", "crowd", "customer", "damage", "date",
             "deal", "degree", "demand", "department", "design", "destroy", "detail", "dirty", "dust", "earn",
             "enemy", "engine", "enter", "escape", "especially", "everywhere", "except", "exercise", "expression",
             "factory", "famous", "farm", "favourite", "finger", "finish", "follow", "front", "future", "gas",
             "gate", "gentle", "gentleman", "ground", "guide", "hair", "hat", "history", "holiday", "hospital",
             "hotel", "hungry", "illegal", "image", "improve", "independent", "individual", "injure", "instrument",
             "interview", "joke", "kitchen", "knife", "language", "large", "law", "left", "lesson", "listen",
             "machine", "map", "market", "marry", "meal", "message", "mistake", "moon", "music", "newspaper",
             "nice", "night", "nose", "object", "obtain", "ocean", "oil", "orange", "pain", "paint", "parcel",
             "path", "peaceful", "perfect", "petrol", "plane", "plant", "pleasure", "practise", "prepare", "prison",
             "private", "probably", "proud", "quiet", "recently", "refuse", "relationship", "religion", "repair",
             "repeat", "replace", "request", "responsible", "restaurant", "rice", "salt", "science", "season",
             "seem", "serious", "serve", "shape", "shoulder", "sick", "silver", "size", "skirt", "sky", "smart",
             "smoke", "society", "special", "spend", "square", "step", "store", "strange", "subject", "successful",
             "supply", "swim", "taste", "teach", "temperature", "thank", "tired", "tomorrow", "top", "touch",
             "train", "trip", "uncle", "university", "usually", "vegetable", "village", "wall", "warm", "wash",
             "weather", "welcome", "win", "winter", "wrong", "yesterday", "admire", "admit", "adventure", "afraid",
             "allow", "although", "animal", "area", "arrive", "asleep", "attempt", "attend", "attitude", "average",
             "bath", "battle", "beer", "belong", "bill", "board", "born", "bottom", "branch", "brave", "breathe",
             "calm", "careless", "certainly", "chain", "character", "charge", "circle", "climb", "clothes", "coal",
             "coin", "comfort", "complete", "consist", "contain", "cook", "copy", "correct", "count", "crime",
             "death", "declare", "defend", "delay", "discover", "dish", "divide", "double", "doubt", "drop", "duty",
             "effort", "either", "English", "equal", "event", "exact", "experience", "express", "fail", "farmer",
             "fat", "flat", "foot", "foreign", "forget", "fresh", "funny", "goal", "grey", "guard", "guess",
             "guest", "gun", "hate", "health", "heavy", "hide", "hole", "horse", "hot", "husband", "indeed",
             "influence", "instead", "intelligent", "international", "iron", "jacket", "join", "kill", "lake",
             "last", "laugh", "leader", "leg", "lie", "lose", "main", "marriage", "match", "measure", "medicine",
             "metal", "middle", "mine", "modern", "mountain", "necessary", "nervous", "noise", "offer", "operation",
             "opinion", "opposite", "outside", "pair", "passenger", "perform", "pile", "pity", "plain", "pleasant",
             "plenty", "point", "politics", "pound", "pour", "press", "prize", "profit", "promise", "prove",
             "raise", "recent", "reduce", "regard", "regular", "risk", "roll", "rough", "row", "rule", "rush",
             "safe", "score", "secretary", "series", "share", "shoot", "shut", "sign", "sing", "smell", "smooth",
             "soft", "soldier", "somewhere", "space", "speech", "spoil", "spot", "spread", "steal", "straight",
             "suddenly", "suggest", "suit", "support", "surface", "these", "thick", "thin", "third", "those",
             "toilet", "trade", "trouble", "trust", "type", "until", "useful", "variety", "various", "vote", "west",
             "whose", "wild", "wish", "without", "wonderful", "wood", "year", "young"]
index_random = random.randint(0, 990)
hidden_word = word_list[index_random]
hidden_word_s = hidden_word
hidden_word = list(hidden_word)

# # display the blanks
# # to print the blanks and show the blanks
# # count the number of blanks needed by adding  _ for each letter in string
num_blanks = len(hidden_word)
for letter in hidden_word:
    blank = str(blank) + '_'
print(blank)
blank = list(blank)
letters_guessed = []
# loop game while the number of incorrect guesses =< 6 or all letters are correctly guessed
while number_of_incorrect_guess <= 6:
    print_gallows(6)
    user_input = input('Please enter your guess one letter at a time e.g a : ')
    ask_user_for_guess(letters_guessed)
    letters_guessed.append(user_input)
    print_hidden_word(hidden_word, letters_guessed)
    ask_user_for_guess(letters_guessed)
    is_game_over(hidden_word, letters_guessed, number_of_incorrect_guess)
    if is_game_done == True:
        break

