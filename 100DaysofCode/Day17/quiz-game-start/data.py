question_data1 = [
    {"text": "A slug's blood is green.", "answer": "True"},
    {"text": "The loudest animal is the African Elephant.", "answer": "False"},
    {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
    {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
    {
        "text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.",
        "answer": "True"},
    {"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.",
     "answer": "False"},
    {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
    {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
    {"text": "Google was originally called 'Backrub'.", "answer": "True"},
    {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
    {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
    {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]

question_data = [
    {
        "category": "Animals",
        "type": "boolean",
        "difficulty": "easy",
        "question": "The Axolotl is an amphibian that can spend its whole life in a larval state.",
        "correct_answer": "True",
        "incorrect_answers": ["False"]
    },
    {"category": "Science & Nature", "type": "boolean", "difficulty": "medium",
     "question": "The Neanderthals were a direct ancestor of modern humans.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Entertainment: Video Games", "type": "boolean", "difficulty": "hard",
     "question": "In &quot;The Sims&quot; series, the most members in a household you can have is 8.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Entertainment: Film", "type": "boolean", "difficulty": "easy",
     "question": "Han Solo&#039;s co-pilot and best friend, &quot;Chewbacca&quot;, is an Ewok.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Animals", "type": "boolean", "difficulty": "medium",
     "question": "The Ceratosaurus, a dinosaur known for having a horn on the top of its nose, is also known to be a decendent of the Tyrannosaurus Rex.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Entertainment: Film", "type": "boolean", "difficulty": "easy",
     "question": "Leonardo DiCaprio won an Oscar for Best Actor in 2004&#039;s &quot;The Aviator&quot;.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "General Knowledge", "type": "boolean", "difficulty": "easy",
     "question": "Gumbo is a stew that originated in Louisiana.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Science & Nature", "type": "boolean", "difficulty": "medium",
     "question": "The planet Mars has two moons orbiting it.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Geography", "type": "boolean", "difficulty": "easy",
     "question": "Vatican City is a country.", "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"category": "Politics", "type": "boolean", "difficulty": "easy",
     "question": "The S in Harry S. Truman stands for &quot;Samuel&quot;.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
     "question": "Linus Torvalds created Linux and Git.", "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"category": "Sports", "type": "boolean", "difficulty": "medium",
     "question": "Soccer player Cristiano Ronaldo opened a museum dedicated to himself.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Entertainment: Music", "type": "boolean", "difficulty": "medium",
     "question": "The country song  &ldquo;A Boy Named Sue&rdquo; was written by Shel Silverstein.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Science: Mathematics", "type": "boolean", "difficulty": "medium",
     "question": "111,111,111 x 111,111,111 = 12,345,678,987,654,321",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Entertainment: Film", "type": "boolean", "difficulty": "easy",
     "question": "The word &quot;Inception&quot; came from the 2010 blockbuster hit &quot;Inception&quot;.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "General Knowledge", "type": "boolean", "difficulty": "easy",
     "question": "Nutella is produced by the German company Ferrero.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Entertainment: Video Games", "type": "boolean",
     "difficulty": "medium",
     "question": "The Ace Attorney trilogy was suppose to end with &quot;Phoenix Wright: Ace Attorney &minus; Trials and Tribulations&quot; as its final game.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Entertainment: Video Games", "type": "boolean", "difficulty": "hard",
     "question": "The first &quot;Metal Gear&quot; game was released for the PlayStation 1.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Science: Mathematics", "type": "boolean", "difficulty": "hard",
     "question": "The binary number &quot;101001101&quot; is equivalent to the Decimal number &quot;334&quot;",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Entertainment: Video Games", "type": "boolean", "difficulty": "easy",
     "question": "Tetris is the #1 best-selling video game of all-time.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Geography", "type": "boolean", "difficulty": "easy",
     "question": "Ottawa is the capital of Canada.", "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"category": "Politics", "type": "boolean", "difficulty": "easy",
     "question": "The 2016 United States Presidential Election is the first time Hillary Clinton has run for President.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Entertainment: Board Games", "type": "boolean", "difficulty": "easy",
     "question": "The Angry Video Game Nerd&#039;s alter ego is &quot;Board James&quot;.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Vehicles", "type": "boolean", "difficulty": "medium",
     "question": "When BMW was established in 1916, it was producing automobiles.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "History", "type": "boolean", "difficulty": "medium",
     "question": "Abraham Lincoln was the first U.S. President to be born outside the borders of the thirteen original states. ",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Entertainment: Japanese Anime & Manga", "type": "boolean",
     "difficulty": "hard",
     "question": "Throughout the entirety of &quot;Dragon Ball Z&quot;, Goku only kills two characters: a miniboss named Yakon and Kid Buu.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Entertainment: Film", "type": "boolean", "difficulty": "medium",
     "question": "Sean Connery wasn&#039;t in &quot;Indiana Jones and the Kingdom of the Crystal Skull&quot; because he found retirement too enjoyable.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "History", "type": "boolean", "difficulty": "hard",
     "question": "The Battle of Trafalgar took place on October 23rd, 1805",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Mythology", "type": "boolean", "difficulty": "medium",
     "question": "In Greek mythology, Hera is the goddess of harvest.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Entertainment: Video Games", "type": "boolean", "difficulty": "easy",
     "question": "In the game Dead by Daylight, the killer Michael Myers is refered to as &quot;The Shape&quot;.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Entertainment: Video Games", "type": "boolean", "difficulty": "easy",
     "question": "The names of Tom Nook&#039;s cousins in the Animal Crossing franchise are named &quot;Timmy&quot; and &quot;Jimmy&quot;.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Entertainment: Video Games", "type": "boolean", "difficulty": "easy",
     "question": "In Pok&eacute;mon Sun and Moon, a male Salandit can evolve to a Salazzle.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Entertainment: Video Games", "type": "boolean",
     "difficulty": "medium",
     "question": "In Riot Games &quot;League of Legends&quot; the name of Halloween event is called &quot;The Reckoning&quot;.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Entertainment: Cartoon & Animations", "type": "boolean",
     "difficulty": "medium",
     "question": "Nickelodeon rejected the pilot to Adventure Time.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Science: Mathematics", "type": "boolean", "difficulty": "medium",
     "question": "Zero factorial is equal to zero. ", "correct_answer": "False",
     "incorrect_answers": ["True"]},
    {"category": "Science & Nature", "type": "boolean", "difficulty": "hard",
     "question": "The chemical element Lithium is named after the country of Lithuania.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Entertainment: Japanese Anime & Manga", "type": "boolean",
     "difficulty": "hard",
     "question": "Druid is a mage class in &quot;Log Horizon&quot;.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Entertainment: Television", "type": "boolean", "difficulty": "hard",
     "question": "The Klingon home planet is Qo&#039;noS.", "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"category": "Entertainment: Television", "type": "boolean", "difficulty": "easy",
     "question": "Klingons express emotion in art through opera and poetry.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Entertainment: Video Games", "type": "boolean",
     "difficulty": "medium",
     "question": "Resident Evil 4 was originally meant to be a Nintendo GameCube exclusive.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Science & Nature", "type": "boolean", "difficulty": "hard",
     "question": "The value of one Calorie is different than the value of one calorie.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "General Knowledge", "type": "boolean", "difficulty": "easy",
     "question": "Dihydrogen Monoxide was banned due to health risks after being discovered in 1983 inside swimming pools and drinking water.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Science: Mathematics", "type": "boolean", "difficulty": "medium",
     "question": "You can square root a negative number with an imaginary number &quot;i&quot;.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Entertainment: Music", "type": "boolean", "difficulty": "hard",
     "question": "The song Scatman&#039;s World was released after Scatman (Ski-Ba-Bop-Ba-Dop-Bop).",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Geography", "type": "boolean", "difficulty": "easy",
     "question": "Nova Scotia is on the east coast of Canada.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "History", "type": "boolean", "difficulty": "medium",
     "question": "The Korean War ended in 1953 without any ceasefire.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "History", "type": "boolean", "difficulty": "medium",
     "question": "Franz Joseph I was the last emperor of Austria.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Entertainment: Video Games", "type": "boolean", "difficulty": "hard",
     "question": "The Paradox Interactive game &quot;Stellaris&quot; was released in 2016.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Entertainment: Film", "type": "boolean", "difficulty": "medium",
     "question": "The original ending of &quot;Little Shop Of Horrors&quot; has the plants taking over the world.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Entertainment: Video Games", "type": "boolean", "difficulty": "easy",
     "question": "&quot;Resident Evil 7&quot; is the first first-person Resident Evil game.",
     "correct_answer": "False", "incorrect_answers": ["True"]}]
