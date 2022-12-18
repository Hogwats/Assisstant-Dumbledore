import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
# print(voices[1].id)
# engine.setProperty('voice', voices[29].id)
# engine.setProperty('speed',)
engine.setProperty('rate',110)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    

comment_datas = {"hello":["hi","hello","hi,how are you"],
                 "hi":['hi','hello','how are  you'],
                 'i love you':"i'm alredy in a relationship",
                 'with whom':'With You',
                 'who developed you':'by the team hogwarts',
                 'who is cringe in world':'no one except you',
                 'Do you like to watch movie???':'I wont watch but i can suggest you...',
                 'Do i look beautiful':'yes ofcourse',
                 'who is elon musk':'he is the ceo of tesla',
                 'how many languages do you know':'i know more languages than you',
                 'how well are your in maths ':'i can solve any problems',
                 "which country won 2018 world cup" :'france',
                 'does monalisa have eyebrows': 'monalisa has no eyebrows',
                 'how many words are there in english?' : "171,476' words",
                 'which is the longest river' : 'nile',
                 'who discovered solar system' :'copernicus',
                 'who developed python' :'guido van rossum',
                 'how old is the sun' :"4.603 billion years",
                 'which animal milk is black' :'female rhinoceros',
                 'which is the laziest day of the week' : 'monday',
                 'what is the lonliest number' :"1",
                 'what is the most used world word': 'the',
                 'which is the easiest programming language?': 'python',
                 'which is the most intelligent animal after human ': 'dolphin',
                 'how many seconds  are there in a year': "31,556,926",
                 'who is the ceo of google' : 'mr sundar pichai',
                 'where the word google comes from? ':'googol',
                 'who is the father of maths' : 'archimedes',
                 'who is the father of whatsapp' : 'jan koum and brian acton',
                 'what is the normal speed of the aeroplane' : '465-575 mph',
                 'who was the oldest  human being on earth' : 'misao okawa',
                 'what percentage of watermelon is actually water': '92%',
                 'which country has the largest armed force ': 'china',
                 'which is the only country in the world to have a square flag ':'switzerland',
                 'who was the first european to attack india' :'alexander',
                 'which country has the most number of lakes' :'canada',
                 'which is the tallest  tower in world':'burj khalifa (828 metres)',
                 'which city is called pink city ':'jaipur',
                 "which mountain is known as 'roof of world'":'pamir',
                 'which is the biggest underground railway network':'new york',
                 'which is the first country to print books':'china',
                 "which country is also know as'land of the midnight sun'":'norway',
                 'The largest dam in the world is located':'south america',
                 "which country gifted the 'statue of liberty ' to USA ":'france',
                 'Dead sea is located between which two countries':'jordan and israel',
                 'which continent has the highest number of countries ':'africa has 54 countries ',
                 'which is the largest tropical rain forest in the world':'amazon',
                 "In which ocean 'bermuda triangle' region is located ":'atlantic',
                 "which gas is present in large quantity in earth's atmosphere":'nitrogen',
                 'which is the smallest bone in human body ':'stapes',
                 'what is the name of the galaxy which contain our solar system':'milky way',
                 'which is the deepest place in earth  ':'The marina trench',
                 "which ocean is doesn't link with other oceans":'pacific and atlantic ocean',
                 'who invented steam engine': 'james watt',
                 'who is the father of our nation':'mahatma gandhi',
                 'who was the first president of india':' DR.rajendra prasad',
                 'who is known as father of indian constitution':'DR.B.R.ambedkar',
                 'which animal is known as ship of the desert':'camel',
                 'which is the most sensitive organ in our body':'skin',
                 'who is the first prime minister of india':'jawaharlal nehru',
                 'who invented computer':'charles babbage',
                 'india lies in which continent':'asia',
                 'which country are the giza pyramids is situated':'egypt',
                 'which country is named as statue of liberty':'new york',
                 'which is the smallest state of india':'goa',
                 'which is the oldest language':'tamizh',
                 'who built thanjai periya kovil':'raja raja chozhan',
                 'who built kallanai dam':'karikala chozhan',
                 'who is the founder of microsoft':'bill gates'}




def convo(qustion):
    speak(comment_datas[qustion])
