
# coding: utf-8

# In[1]:

import pandas as pd


# In[10]:

get_ipython().magic(u'pylab inline')


# In[12]:

get_ipython().magic(u'matplotlib inline')


# In[ ]:

df = pd.read_csv("train.csv")


# In[4]:

df


# In[5]:

df.PassengerId.value_counts()


# In[6]:

df.describe()


# In[50]:

df.PassengerId.value_counts().plot(kind='line')


# In[15]:

df[df.PassengerId.isnull()]


# ### PassengerId 
# 1. Continuous variable
# 2. No Missing values
# 3. min = 1.000000 max = 891.000000 std = 257.353842
# 4. Graph is above

# In[16]:

df[df.Survived.isnull()]


# In[17]:

df.Survived.value_counts().plot(kind='bar')


# ### Survived
# 1. Continuous variable
# 2. No Missing values
# 3. min = 0.000000 max = 1.000000 std =  0.486592 
# 4. Graph is above

# In[18]:

df[df.Pclass.isnull()]


# In[19]:

df.Pclass.value_counts().plot(kind='bar')


# ### Pclass
# 1. Continuous variable
# 2. No Missing values
# 3. min = 1.000000 max = 3.000000 std =  0.836071
# 4. Graph is above

# In[20]:

df[df.Sex.isnull()]


# In[21]:

df.Sex.value_counts().plot(kind='bar')


# ### Sex
# 1. Categorical variable with two options: Male and Female
# 2. No Missing values
# 3. No min, max or std because it is a categorical variable
# 4. Graph is above

# In[22]:

df[df.Age.isnull()]


# In[27]:

df.Age.value_counts().plot(kind='pie')


# In[28]:

avgAge = df.Age.mean()


# In[29]:

avgAge


# In[30]:

df.Age = df.Age.fillna(value=avgAge)


# In[31]:

df.describe()


# ### Age
# 1. Continuous variable
# 2. There are missing values
# 3. min =  0.420000  max = 80.000000 std =  13.002015
# Note : I replaced all Nan values with the mean Age and then got the std value
# 4. Graph is above

# In[32]:

df[df.SibSp.isnull()]


# In[33]:

df.SibSp.value_counts().plot(kind='bar')


# ### SibSp
# 1. Continuous variable
# 2. No Missing values
# 3. min =   0.000000   max = 8.000000 std =  1.102743
# 4. Graph is above

# In[34]:

df[df.Parch.isnull()]


# In[35]:

df.Parch.value_counts().plot(kind='bar')


# ### Parch
# 1. Continuous variable
# 2. No Missing values
# 3. min =   0.000000   max = 6.000000 std =   0.806057 
# 4. Graph is above

# In[36]:

df[df.Ticket.isnull()]


# In[45]:

df.Ticket.value_counts().plot(kind='area')


# ### Ticket
# 1. Categorical variable with multiple options describing the ticket
# 2. No Missing values
# 3. No min, max or std because it is a categorical variable
# 4. Graph is above

# In[40]:

df[df.Fare.isnull()]


# In[44]:

df.Fare.value_counts().plot(kind='area')


# ### Fare
# 1. Continuous variable
# 2. No Missing values
# 3. min =   0.000000   max =  512.329200  std =    49.693429  
# 4. Graph is above

# In[46]:

df[df.Cabin.isnull()]


# In[47]:

df.Cabin.value_counts().plot(kind='bar')


# ### Cabin
# 1. Categorical variable with multiple options describing the cabin 
# 2. There are missing values; maybe because not everyone had a cabin?
# 3. No min, max or std because it is a categorical variable
# 4. Graph is above

# In[48]:

df[df.Embarked.isnull()]


# In[49]:

df.Embarked.value_counts().plot(kind='bar')


# ### Embarked
# 1. Categorical variable with multiple options describing Embarking locations 
# 2. There are missing values
# 3. No min, max or std because it is a categorical variable
# 4. Graph is above

# In[ ]:



