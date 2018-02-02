# -*- coding: utf-8 -*-
import numpy as np 
from argparse import ArgumentParser

def Autograde(Wfile,Ifile):
    #This file contains all the correct words
    W = np.loadtxt(Wfile,dtype='string') 
    #This  is created to print later in a correct form the umlauts in german 
    W2 = [i.decode('utf-8') if isinstance(i, basestring) else i for i in W]
    #This is the input file of anwers 
    I = np.loadtxt(Ifile,dtype='string') 
    I2 = [i.decode('utf-8') if isinstance(i, basestring) else i for i in I]

    bads = 0.
    total = len(I)
    spell = [] #Think that you remember the word as it was 
    hear = [] #Only remember it hearing at it
    write = []  #Only remember it looking at it
    for i in range( len(I) ):
        if I[i]=='h' or I[i]=='w':
            total -=1 
            continue 
        a = W ==I[i] 
        if len(W[a])==0: 
            bads +=1
            try: 
                spell.append( I2[i].decode('utf-8') ) 
            except UnicodeEncodeError:
                    s = I2[i].replace(u'\xf6',u'ö')
                    s = I2[i].replace(u'\xfc',u'ü')  
                    spell.append(s) 
        #If the word was not remembered but write down listening at 
        # it (recognizing the meaning) then it substract 2/3 points.
        if I[i-1]=='h':
            bads += 2/3.
            hear.append(I[i])
        #If the word was not remembered but write down looking at 
        # it then it substrat 4/5
        if I[i-1]=='w':
            bads += 2/3.
            write.append(I[i])
    print '\nWords that you had thougth to get:\n'
    for i in spell: print i 
    print '\nWords that you recognized listening but do not remembered\n'
    for i in hear: print i 
    print '\nWords that you recognized looking but do not remembered:\n'
    for i in write: 
        print i 
    print ('You get %d of %d: ' %( (total-bads),total) )
    print '\n'
    return  'So, your score is %.1f' %( round( (total-bads)/total*5,1) )
if __name__=='__main__':
    
    Wfile, Ifile = 'Lessonwords.txt', 'Quiz.txt'
    
    # To permit to change the quiz and the word base file from 
    #  the terminal 
    parser = ArgumentParser(prog='N-Body', description='This program make the \
                        simulation of N-Body')
    parser.add_argument('-w', '--Wfile', help='File of intput')
    parser.add_argument('-q', '--Ifile', help='File of intput')
    args = parser.parse_args() 
    if args.Wfile:
        Wfile = args.Wfile
    if args.Ifile:
        Ifile = args.Ifile

    print ( Autograde(Wfile,Ifile) )