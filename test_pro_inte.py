from keras.utils import to_categorical

import numpy as np


#first define a dictionary of letters mapped to integer

LETTERS="ABCDEFGHIJKLMNOPQRSTUWXYZV*"
letter_to_int={}
for i,letter in enumerate(LETTERS):
    letter_to_int[letter]=i
#print(letter_to_int)
char_to_int=dict((c,i) for i,c in enumerate(LETTERS))
int_to_char=dict((i,c) for i,c in enumerate(LETTERS))

#################################################################
#make a function that take an input of string,return the list of integer


def text_to_int_converter(string):
    """convert a string into integer where each integer correspond
       to letter in string
       #Argument:
       string:letters to be converted into integer
       return:list containing integers
    
    """

    return [char_to_int[char] for char in string]




#################################################################
#make a function that take an input of integer,return the list of string
def int_to_text_converter(int_list):

    """convert a integer list into list of character 
       #Argument:
       int_list:list of integer to be converted into character
       return:list containing integer
    """
    return [int_to_char[num] for num in int_list]




##################################################################

#make a 27 dimensional vector for each amino acid i.e for each integer
#in the list


def convert_one_hot(list_integers,num_classes=27):
       """ convert list of integer list to numpy array

    
  
        """
       one_hot_encod=to_categorical(s,num_classes=num_classes)
       np.array(one_hot_encode,type="int")
       return numpy_array
#############################################################

#       Test cases
#seq="HNNIYSMFLQQTWHVQFLMLVPGEEKILHRSRVKFFGMWHNLCCSKTRTHIHQCFEQLLKYHDYRLFKDMALNRRSVQHASCDRWIRVSKMPRPVSPFRNEGSAMKPNEFCCEDAKHCTIGPKRMPDEQQFNHQQISSSACTIVFITLDVDDGHECIMAVEKTNADSTLGVNHNWCCPIWEVDDYQDDMSMRCHFKFTQQGPPWMAEMNGDYNHDPKNCCPHEYLCSAVVIWVIIEYWCYTSQGNYATICHILMNLVTEWNGFHLAIHLMMPYMVERPCKFWGAISNPCMSARFTFQPMPWSRCTTFTTVMQRDMGWLVGQRMMPMMSIGWASCMWWPVVQSPGFHFQMFCTTNSQFHRTLNHTNQSICQIMTWRGDPEYDYPNAMCTWKKQKRRKGWGQLHNMPQEPPYQANYSYNGRCVDHVIHQQVVVVGMVFRMELLLFLCDKGWEEECVCNANNGPLRQGFSYEWVCWAWKLDNSGFTVFGTPFFGDHPIGYLCTIHSETNYSYTVHHPSQVRKEVRFNYWKGHENNHTRRSHIQMLCDVVCHFTFGSLMRRLCPCRWPPRDYCIRQDHPWCIYGMPTKQDKDAKLWDTYHPYSWLELEDCYLFCPFSRVFDQKLIMAHIVRICHTCLQMRMQSLMYIMYNSHGLCIIGRDSRWAHKRRYFGSDMPSCYHYLSFHFVRDLNDVRCGVDCDGLSNRFGLNDLNKLTHHNCKKNNGMILAVNSTTCEPKPTHQFAHVWSIIKHNNESVWNGLSGPEFAKQTCFSDGFFDPFMQWDHKPRFPRMCVQNHNDHLYQIYCRGTDEREQVAMESHFEFEQSNEKCVQQDVQEARSGTWHEGNEADVFPINEMRTHKCEGQNVNLQFSCCERQSAIMNCEAIRCATWKFTECVITQDCNWRRWRSYDLQYLQWGHYPKQEFMCFTDGQNDSPTVFNVEIKGK"
seq="HNNIYSMFLQQ"
s=text_to_int_converter(seq)
print(s)
#list_num=[3,4,5]
#d=int_to_text_converter(s)
#print(d)

print("""""")

print("""""")
print("--------------------------------------------------")
a=to_categorical(s,num_classes=27)
print(a)
print(a.shape)
#one_h=one_hot(d,20)
#printtone_h)



###def one_hot_encode(protein_integered):
##    """
##
##     #one hot encoding of protein sequence
##
##     #Argument:
##       #protein_integered:protein sequence represented by integerlist
##
##     #output
##     #one hot encoded 2D array of size(no of residue,20)
##
##     """
    #make a 2D array of float32 whose no of rows equal to no of residue

    # of amino acid and columun is 20
##    no_aminoacid=len(s)
##    repre=np.zeros(no_aminoacid,dtype=float)
##    for digit in protein_integered:
##        l=np.zeros((1,20),dtype=float)
##        l[repre]=1
##        repre.add
    


#using one_hot from keras convert it into input array



