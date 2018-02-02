
## Getting started 

Basically it recives a file in the following format


### ----------------Quiz1.txt------------------ here begins
### word1
### h
### word2
### word3_wrong_at_porpose #_ means space
### w
### word4
### ------------------------------------------ here finishes

Now the calification gives at first the same weight to each word, if you put a h before it means that you hadn't remembered the word that follows but listen at it you wrote it perhaps because you recognized the meaing (this counts for 1/3 of the initial word weight). On the other, w before it means that you hadn't remembered the word that follows but reading at it you wrote it (this counts as 1/5 of the initial word weight). Finally, if a word is bad if counts for 0. 

So, supposing that file as Quiz1.txt you could have a file a base file for calification as follows: 

### ----------------Lesson22_25words.txt------------------ here begins
### word1
### word2
### word3
### word4
### newword
### incredibleword
### ----------------------------------------------------- here finishes

You could use the program as follows: 

python Autograde.py -q Quiz1.txt -w Lesson22_25words.txt, obtaining as result: 

### --------------Printed result in the terminal--------------- here begins
### Words that you had thougth to get:
### 
### word3_wrong_at_porpose
### 
### Words that you recognized listening but do not remembered
### 
### word2
### 
### Words that you recognized looking but do not remembered:
### 
### word4
### 
### You get 1.7 of 4.0 
### So, your score is 2.1
### ------------------------------------------------------------ here finishes

Now, if the -q file and the -w file are not specified it will take as default Quiz.txt and Lessonwords.txt in the folder "files".

