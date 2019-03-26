#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np

TradingCode = 1
importername = 'Tianjin Kaigui Machinery Co.LTD'
repImportername = 'BEYLERBEYI GENERAL TRADING LLC'
cityOfImportername = 'Tianjin- China'
cityOfrepImportername = 'Dubi-UAE'


# In[2]:


miss_value = ['']
clientlist = pd.read_csv('2018 ABACUS CLIENTS.csv')


# In[3]:


# clientlist = clientlist.dropna()
clientlist


# In[4]:


# import csv
# productname = []
# unit = []
# doller = []
# derham = []
# euro = []
# tradetype = []
# code =[]
# with open('product.csv') as csvfile:
#     readCSV = csv.reader(csvfile, delimiter=',')
#     for row in readCSV:
#         productname.append(row[0])
#         unit.append(row[1])
#         doller.append(row[2])
#         derham.append(row[3])
#         euro.append(row[4])
#         tradetype.append(row[5])
#         code.append(row[6])
# productname =list(productname)
# unit = list(unit)
# doller=list(doller)
# derham = list(derham)
# euro=list(euro)
# code= list(code)     

# productfram = []
# productfram = pd.DataFrame()
# productfram['p_name'] ,productfram['unit'], productfram['dollar'],productfram['dirham']= productname , unit , doller, derham
# productfram['euro'], productfram['type'], productfram['tradingTypeCode'] = euro, tradetype, code

# productfram.to_csv('product.csv',index=False)


# In[5]:


productlist = pd.read_csv('product.csv',na_values =miss_value )


# In[6]:


productlist = productlist.dropna()
productlist


# In[7]:


Colist = pd.read_excel('List of Companies.xlsx')


# In[8]:


Colist = Colist.dropna()
Colist


# In[9]:


track = pd.read_csv('TRACKING SHEET.csv',skiprows = 7)
track


# In[10]:


def getBoldataframe(TradingCode, datalist):
    codeVector = []
    for procode in datalist['tradingTypeCode']:
        if procode ==TradingCode:
            codeVector.append(True)
        else:
            codeVector.append(False)

    return datalist[codeVector]


# In[11]:


# Distangolishing rep.Exporte and exporte in tacking sheet.
repOrMainCo = [True if (('UAE' in str(x))or('uae' in str(x))or('U.A.E' in str(x))or('u.a.e' in str(x))) else False for x in track['country']]# All type of uae

def randomExporter(i, datalist):
    tradedataframe = getBoldataframe(i,datalist)
    r, _ = tradedataframe.shape
    count = np.floor(np.random.rand()*r)
    return str(datalist.loc[count,'companies']),str(datalist.loc[count,'country'])
repExporter = []
cityOfRepExporter = []
exporter = []
cityOfExporter = []
for i in range(len(repOrMainCo)):
    if repOrMainCo[i]:
        repExporter.append(str(track.loc[i, 'exporter/repExporter']))
        cityOfRepExporter.append(str(track.loc[i, 'country']))
    else:
        repExporter.append('')
        cityOfRepExporter.append('')
#     print(repExporter[i] , str(track.loc[i, 'exporter/repExporter']))
    if not (repOrMainCo[i]):
        exporter.append(str(track.loc[i, 'exporter/repExporter']))
        cityOfExporter.append(str(track.loc[i, 'country']))
    else:
        exp , cityExp = randomExporter(i,Colist)
        exporter.append(exp)
        cityOfExporter.append(cityExp)


# In[12]:


ones = {
    0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six',
    7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve',
    13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
    17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
tens = {
    2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty',
    7: 'seventy', 8: 'eighty', 9: 'ninety'}
illions = {
    1: 'thousand', 2: 'million', 3: 'billion', 4: 'trillion', 5: 'quadrillion',
    6: 'quintillion', 7: 'sextillion', 8: 'septillion', 9: 'octillion',
    10: 'nonillion', 11: 'decillion'}

def say_number(i):
    """
    Convert an integer in to it's word representation.

    say_number(i: integer) -> string
    """
    if i < 0:
        return _join('negative', _say_number_pos(-i))
    if i == 0:
        return 'zero'
    return _say_number_pos(i)


def _say_number_pos(i):
    if i < 20:
        return ones[i]
    if i < 100:
        return _join(tens[i // 10], ones[i % 10])
    if i < 1000:
        return _divide(i, 100, 'hundred')
    for illions_number, illions_name in illions.items():
        if i < 1000**(illions_number + 1):
            break
    return _divide(i, 1000**illions_number, illions_name)


def _divide(dividend, divisor, magnitude):
    return _join(
        _say_number_pos(dividend // divisor),
        magnitude,
        _say_number_pos(dividend % divisor),
    )


def _join(*args):
    return ' '.join(filter(bool, args))


# In[13]:


amountToWord = []
for number in track['amount']:
    amountToWord.append(say_number(number))


# In[14]:


#,DIS1,QTY1,UNIT1,UNITPRICE1,TOTAL1,DIS2,QTY2,UNIT2,UNITPRICE2,TOTAL2
# businessType, REF, Date,IMPORTER,CTOFIM,REPPOFIM,CTOFREPOFIM,REPOFEXPORTER,CTOFREPOFEXPORTER,EXPORTER,CTOFEX,TOTALAMOUNT,Currency,INWORDS,ORIGIN,LO,DIS, amountInWord

importer = np.full(len(track['refrence']),importername)
repImporter = np.full(len(track['refrence']),repImportername)
cityOfImporter = np.full(len(track['refrence']),cityOfImportername)
cityOfrepImporter = np.full(len(track['refrence']),cityOfrepImportername)


# In[15]:


def lcs(X , Y): 
    # find the length of the strings 
    m = len(X) 
    n = len(Y) 
  
    # declaring the array for storing the dp values 
    L = [[None]*(n+1) for i in range(m+1)] 
  
    """Following steps build L[m+1][n+1] in bottom up fashion 
    Note: L[i][j] contains length of LCS of X[0..i-1] 
    and Y[0..j-1]"""
    for i in range(m+1): 
        for j in range(n+1): 
            if i == 0 or j == 0 : 
                L[i][j] = 0
            elif X[i-1] == Y[j-1]: 
                L[i][j] = L[i-1][j-1]+1
            else: 
                L[i][j] = max(L[i-1][j] , L[i][j-1]) 
  
    # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1] 
    return L[m][n] 
#end of function lcs 
  
# Driver program to test the above function 
X = "AGGTAB"
Y = "GXTXAYB"
print("Length of LCS is ", lcs(X, Y))


# In[16]:


# def lcs(s1, s2):
#     matrix = [["" for x in range(len(s2))] for x in range(len(s1))]
#     for i in range(len(s1)):
#         for j in range(len(s2)):
#             if s1[i] == s2[j]:
#                 if i == 0 or j == 0:
#                     matrix[i][j] = s1[i]
#                 else:
#                     matrix[i][j] = matrix[i-1][j-1] + s1[i]
#             else:
#                 matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1], key=len)

#     cs = matrix[-1][-1]

#     return len(cs), cs

# print(lcs("abcdaf", "acbcf")) 


# In[17]:


# def lcs(X, Y, m, n): 
  
#     if m == 0 or n == 0: 
#        return 0; 
#     elif X[m-1] == Y[n-1]: 
#        return 1 + lcs(X, Y, m-1, n-1); 
#     else: 
#        return max(lcs(X, Y, m, n-1), lcs(X, Y, m-1, n)); 
# X = "AGGTAB"
# Y = "GXTXAYB"
# print("Length of LCS is ", lcs(X , Y, len(X), len(Y)))


# In[18]:


# def longestSubstringFinder(string1, string2):
#     answer = ""
#     len1, len2 = len(string1), len(string2)
#     for i in range(len1):
#         match = ""
#         for j in range(len2):
#             if (i + j < len1 and string1[i + j] == string2[j]):
#                 match += string2[j]
#             else:
#                 if (len(match) > len(answer)): answer = match
#                 match = ""
#     return answer

# print(longestSubstringFinder("apple pie available", "apple pies"))
# print(longestSubstringFinder("apples", "appleses"))
# print(longestSubstringFinder("bapples", "cappleses"))


# In[19]:


def getClientRef(c, clientlist):
    num = str(clientlist.loc[c,'SR. NO.']) + '.'
    for char in clientlist.loc[c,'LIST OF COMPANY']:
        if char != '.':
            num = num + char
        else:
            break
    return num
    
def bestmatch(candid,clientlist):
    candid = ''.join(e for e in candid if e.isalnum())
    c = 0
    maxAl = 0
    candidRow = []
    num = ''
    for client in clientlist['LIST OF COMPANY']:
    #     print(client)
        candidLcs = lcs(candid.lower(), client.lower())
    #     print(LsubSF)
        if candidLcs > maxAl:
            match = c
            maxAl = candidLcs
            print(len(candid),candidLcs)
            if candidLcs >= len(candid):
                candidRow = list(clientlist.iloc[c])
                num = getClientRef(c, clientlist)
        c+=1

    print(num, candidRow)
    return num, candidRow
# bestmatch('STORZ MEDICAL AG',clientlist)


# In[20]:


numlist = []
veclist = []
c = 0
for client in repExporter:
#     print(client)
    num , vec = bestmatch(client,clientlist)
    numlist.append(num)
    veclist.append(vec)
    if num != '':
        cityOfRepExporter[c] = vec[3]
        exporter[c] = vec[4]
        cityOfExporter[c] = vec[5]
    c += 1 


# In[21]:


# r,c = track.shape

# po = []
# for i in range(r):   
#     if track.loc[i,'Unnamed: 3'] == 'EURO':
#         track.is_copy = False
#         track.loc[i,'Unnamed: 3'] = 'AED'
#         track.loc[i,'Unnamed: 2'] = str(int(track.loc[i,'Unnamed: 2']) * 4.13)
#         print(track.loc[i,'Unnamed: 2'])

# print(track.loc[1, 'exporter/repExporter'])


# In[117]:


def QtyClassification(amount, mean):
    estQty = int(amount / mean)
    if (estQty < 30):
        return 1
    elif (estQty >= 30) and (estQty < 80):
        return np.ceil(np.random.randint(1,2,1))
    
    if (estQty >= 80) and (estQty < 150):
        return np.ceil(np.random.randint(2,3,1))
    
    elif (estQty >= 150) and (estQty < 300):
        return np.ceil(np.random.randint(2,4,1))
    
    elif (estQty >= 300) and (estQty < 600):
        return np.ceil(np.random.randint(3,4,1))

    elif (estQty >= 600) and (estQty <1000 ):
        return np.ceil(np.random.randint(4,5,1))

    elif (estQty > 1000 ):
        return 5    


# In[118]:


int(QtyClassification(400000 , 2991.8068396226417))


# In[119]:


#Choosing products

def getRandomKProduct(amount,iD, datalist):
    tradedataframe = getBoldataframe(iD,datalist)
    codeVector = []
    # removing greater than amount
    for proAmount in tradedataframe['dollar']:
        if amount > proAmount:
            codeVector.append(True)
        else:
            codeVector.append(False)
    tradedataframe = tradedataframe[codeVector]
    #Computing mean value
    codeVector = []
    mean = np.mean(tradedataframe['dollar'])
#     print(mean)
    for proAmount in tradedataframe['dollar']:
        if (proAmount > mean/100) and proAmount < mean*100:
            codeVector.append(True)
        else:
            codeVector.append(False)
    
    r, _ = tradedataframe.shape
#     print(r)
    tradedataframe = tradedataframe[codeVector]
    
    r, _ = tradedataframe.shape
#     print(r)
#     print(amount , mean)
    k = int(QtyClassification(amount , mean))
#     print(k)
    produc = []
    if k < r:
        for i in range(k):
            count = np.random.randint(0,r-1,1)
#             print(count[0])
            produc.append(list(tradedataframe.iloc[count[0]]))
            tradedataframe.drop(tradedataframe.index[count[0]], inplace=True)
            r, c = tradedataframe.shape
#             print(r)
    else:
        produc =tradedataframe
#     print(len(produc), k)
    RandomKProduct = pd.DataFrame(produc)
#     print(RandomKProduct)
    RandomKProduct.columns = ['p_name','unit','dollar','dirham','euro','type','tradingTypeCode']
#     RandomKProduct.rename(inplace=True, header={'0':'p_name','1':'unit','2':'dollar','3':'dirham','4':'euro','5':'type','6':'tradingTypeCode'}, axis='columns')
    return RandomKProduct


# In[120]:


print(np.random.randint(0,102,1))
getRandomKProduct(3000000,TradingCode, productlist)


# In[121]:


np.random.randint(1,10,3)


# In[122]:


def changeCurrency(i , data):
#     print(str(track.loc[i,'currency']).lower())
    if str(track.loc[i,'currency']).lower() == 'euro':
        return float(track.loc[i,'amount'] * 1.13)
    else:
        return float(track.loc[i,'amount'] * 0.27)


# In[123]:


changeCurrency(0,track)


# In[ ]:





# In[124]:


#amount    currency
#1
p1name = []
p1unit = []
p1unitp = []
p1qty = []
p1total = []
#2
p2name = []
p2unit = []
p2unitp = []
p2qty = []
p2total = []
#3
p3name = []
p3unit = []
p3unitp = []
p3qty = []
p3total = []
#4
p4name = []
p4unit = []
p4unitp = []
p4qty = []
p4total = []
#5
p5name = []
p5unit = []
p5unitp = []
p5qty = []
p5total = []
for i in range(len(track['date'])):
#     print(i)
    pname = []
    unit = []
    unitp = []
    qty = []
    total = []
#     print(float(track.loc[i,'amount']))
    if str(track.loc[i,'currency']) == 'Dollar':
        amount = float(track.loc[i,'amount'])
    else:
        amount = float(changeCurrency(i,track))
#     print(amount)
    RandomKProduct = getRandomKProduct(amount, TradingCode, productlist)
    RandomKProduct = RandomKProduct.sort_values(by='dollar', ascending=False)
#     print(RandomKProduct)
    copyamount = amount
#     print(amount)
    #allocating rest of amount
    tot = 0
    if (len(RandomKProduct['p_name']) >1):
        for j in range(len(RandomKProduct['p_name']) - 1):
            bound = int(copyamount / RandomKProduct.loc[j,'dollar'] )
            pname.append(RandomKProduct.loc[j,'p_name'] )
            unit.append(RandomKProduct.loc[j,'unit'])
            unitp.append(RandomKProduct.loc[j,'dollar'])
            qty.append(np.floor(np.random.randint(1,(bound-1),1)[0]))
            copyamount = amount - (unitp[-1] * qty[-1])
            total.append((unitp[-1] * qty[-1]))
            tot += (unitp[-1] * qty[-1])
    j = len(RandomKProduct['p_name']) - 1
    pname.append(RandomKProduct.loc[j,'p_name'] )
    unit.append(RandomKProduct.loc[j,'unit'])
    unitp.append(RandomKProduct.loc[j,'dollar'])
    qty.append(int(copyamount / RandomKProduct.loc[j,'dollar']))
    
    if copyamount % RandomKProduct.loc[j,'dollar'] !=0:
        unitp[-1] = float(copyamount / qty[-1])
    total.append(amount - tot)
#     print(amount)
    
#     print(unit,unitp,qty,total)
    #1
    p1name.append(pname[0])
    p1unit.append(unit[0])
    p1unitp.append(unitp[0])
    p1qty.append(qty[0])
    p1total.append(total[0])
    #2
    if len(pname) > 1:
        p2name.append(pname[1])
        p2unit.append(unit[1])
        p2unitp.append(unitp[1])
        p2qty.append(qty[1])
        p2total.append(total[1])
    else:
        p2name.append('')
        p2unit.append('')
        p2unitp.append('')
        p2qty.append('')
        p2total.append('')
        
    #3
    if len(pname) > 2:
        p3name.append(pname[2])
        p3unit.append(unit[2])
        p3unitp.append(unitp[2])
        p3qty.append(qty[2])
        p3total.append(total[2])
    else:
        p3name.append('')
        p3unit.append('')
        p3unitp.append('')
        p3qty.append('')
        p3total.append('')        
    #4
    if len(pname) > 3:
        p4name.append(pname[3])
        p4unit.append(unit[3])
        p4unitp.append(unitp[3])
        p4qty.append(qty[3])
        p4total.append(total[3])
    else:
        p4name.append('')
        p4unit.append('')
        p4unitp.append('')
        p4qty.append('')
        p4total.append('')        
    #5
    if len(pname) > 4:
        p5name.append(pname[4])
        p5unit.append(unit[4])
        p5unitp.append(unitp[4])
        p5qty.append(qty[4])
        p5total.append(total[4])
    else:
        p5name.append('')
        p5unit.append('')
        p5unitp.append('')
        p5qty.append('')
        p5total.append('')        


# In[125]:


unitp,qty,total


# In[126]:


#Origin
origin = []
bol = False
for word in cityOfExporter:
    word = str(word)
    if word == '':
        origin.append(word)
        continue
    for i in range(len(word)):
        if word[i] == '-':
            origin.append(word[(i+1):len(word)])
            bol = True
            break
        else:
            bol = False
    if not bol:
        origin.append(word)   


# In[127]:


print(len(repExporter), len(exporter))


# In[128]:


forPO = []
forPO = pd.DataFrame()
forPO['REF'],forPO['date'],forPO['totalAmount'] = track['refrence'], track['date'],track['amount'] 
forPO['amountToWord'],forPO['currency'],forPO['importer'] = amountToWord,track['currency'],importer
forPO['cityOfImporter'],forPO['repImporter'],forPO['cityOfrepImporter'] = cityOfImporter,repImporter,cityOfrepImporter
forPO['exporter'] = exporter
forPO['cityOfExporter'] = cityOfExporter
forPO['repExporter'] = repExporter
forPO['cityOfRepExporter'],forPO['numOfClient'],forPO['laoding'] = cityOfRepExporter, numlist, cityOfExporter
forPO['Discharge'],forPO['Origin'] = cityOfImporter,origin 
forPO['p1name'] = p1name
forPO['p1unit'] = p1unit
forPO['p1unitp'] = p1unitp
forPO['p1qty'] = p1qty
forPO['p1total(in Dollar)'] = p1total
#2
forPO['p2name'] = p2name
forPO['p2unit'] = p2unit
forPO['p2unitp'] = p2unitp
forPO['p2qty'] = p2qty
forPO['p2total(in Dollar)'] =p2total
#3
forPO['p3name'] = p3name
forPO['p3unit'] = p3unit
forPO['p3unitp'] = p3unit
forPO['p3qty'] = p3unit
forPO['p3total(in Dollar)'] = p3total
#4
forPO['p4name'] = p4name
forPO['p4unit'] = p4unit
forPO['p4unitp'] = p4unitp
forPO['p4qty'] = p4qty
forPO['p4total(in Dollar)'] = p4total
#5
forPO['p5name'] = p5name
forPO['p5unit'] = p5unit
forPO['p5unitp'] = p5unitp
forPO['p5qty'] = p5qty
forPO['p5total(in Dollar)'] = p5total
forPO.to_csv('Tracking Sheet output.csv')


# In[ ]:






