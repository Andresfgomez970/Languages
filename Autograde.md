
# Running the code

Basically it recives a file in the following format:


----------------Quiz1.txt------------------ here begins <br />
word1 <br />
h <br />
word2 <br />
word3_wrong_at_porpose #_ means space <br />
w <br />
word4 <br />
------------------------------------------ here finishes <br />

Now the calification gives at first the same weight to each word, if you put a h before it means that you hadn't remembered the word that follows but listen at it you wrote it perhaps because you recognized the meaing (this counts for 1/3 of the initial word weight). On the other, w before it means that you hadn't remembered the word that follows but reading at it you wrote it (this counts as 1/5 of the initial word weight). Finally, if a word is bad if counts for 0. 

So, supposing that file as Quiz1.txt you could have a file a base file for calification as follows: 

-----------Lesson22_25words.txt--------------- here begins <br />
word1 <br />
word2 <br />
word3 <br />
word4 <br />
newword <br />
incredibleword <br />
---------------------------------------------- here finishes <br />

You could use the program as follows: 

python Autograde.py -q Quiz1.txt -w Lesson22_25words.txt, obtaining as result: 

--------------Printed result in the terminal--------------- here begins <br /> 
Words that you had thougth to get: <br />
 
word3_wrong_at_porpose <br />
 <br />
Words that you recognized listening but do not remembered <br />
 <br />
word2 <br />
 <br />
Words that you recognized looking but do not remembered: <br />
<br />
word4 <br />
 <br />
You get 1.7 of 4.0 <br />
So, your score is 2.1 of 5.0 <br />
------------------------------------------------------------ here finishes <br />

Now, if the -q file and the -w file are not specified it will take as default Quiz.txt and Lessonwords.txt in the folder "files".

# Software 

At the moment python 2.7
