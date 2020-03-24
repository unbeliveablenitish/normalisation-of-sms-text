File in this folder are :

metaphone.py - this file has Double Metaphone Algorithm Implemented.

code.py - this file ask the user to give input and will generate the confusion set for OOV(Out Of Vocabulary) words. And then using LCS(Lowest Comman Subsequence), Edit Distance Ratio, Suffix Match , Prefix Match - will try to suggest the correct candidate for the given OOV word.

Also install PyEnchant Library.

codeOnSample.py - This file runs on dict/emnlp_dict.txt where we have one to one mapping of a ill-formed word with its most probable correct candidate. So it will run on this file and and give the count of OOV words where the most probable candidate occurs in Confusion Set.

How to run our code :

$python code.py
Enter Your Text: <Enter Your Text Here>

$python codeOnSample.py   (This file take a long time to run.)

