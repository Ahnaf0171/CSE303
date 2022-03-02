#!/usr/bin/env python
# coding: utf-8

# In[1]:


#p1

divisible8 = [i for i in range(1,1001) if i % 7 == 0] 
print(divisible8)


# In[2]:


#p2

six = [i for i in range(1,1001) if '6' in str(i)] 
print(six)


# In[10]:


#p3
nums = [i for i in range(1,1001)]
string = "Ahnaf is a good boy."

n=len(string)
cnt=0

for i in range(1,n):
    if(string[i] == ' '):
       cnt+=1 
print("Spaces of the string is : ",cnt)


# In[11]:


#p4
string = "Ahnaf is a good boy."
for word in string:
    if word in ('a','e','i','o','u','A','I','E','O','U'):
        string = string.replace(word, '')
        
print("without vowel :", string)


# In[12]:


#p5
string = "Ahnaf is a good boy."
word=string.split(" ")
L=len(word)
for i in range (1,L):
    if(len(word[i])<5 ):
        print(word[i])
       


# In[ ]:





# In[13]:


#p6
string = "Ahnaf is a good boy."
words = string.split()
word_lengths = []
for word in words:
   word_lengths.append(len(word))
print(words)
print(word_lengths)


# In[14]:


#p7

for i in range(1,1000,1):
    for j in range(12,19,1):
        if(i%j==0):
            print(i," ")


# In[ ]:




