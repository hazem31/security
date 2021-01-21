import numpy as np


def caeser(plainText,key_c):
    plain = plainText.upper()
    cipher = ""
    for char in plain:
        cipher += chr(((ord(char) - ord('A') + key_c) % 26) + ord('A'))
    return cipher

def playfair(plainText,key):
    rows, cols = (5, 5) 
    arr = [[0 for i in range(cols)] for j in range(rows)] 
    key = key.upper()
    while 'J' in key:
        key.replace("J","I")

    index_row  = 0
    index_col = 0 
    seen = []
    for char in key:
        if char in seen:
            continue
        
        arr[index_row][index_col] = char
        index_col += 1
        if index_col == 5:
            index_col=0
            index_row += 1
        
        seen.append(char)

    for i in range(65,ord('Z')+1,1):
        char = chr(i)
        if char == 'J':
            char = 'I'

        if char in seen:
            continue

        arr[index_row][index_col] = char
        index_col += 1
        if index_col == 5:
            index_col=0
            index_row += 1
        
        seen.append(char)

    plainText = plainText.upper()
    plainText = plainText.replace("J","I")
    newP = ""

    i1 = 0
    while(i1 < len(plainText) - 1):
        if plainText[i1] == plainText[i1+1]:
            newP += plainText[i1]
            if plainText[i1] == "X":
                newP += "Z"
            else:
                newP += "X"
            i1 += 1
            continue
        newP += plainText[i1]
        newP += plainText[i1+1]
        i1 += 2

        if i1 == len(plainText) - 1:
            newP += plainText[-1]        


    # for i in range(0,len(plainText) - 1,2):
    #     if plainText[i] == plainText[i+1]:
    #         newP += plainText[i]
    #         if plainText[i] == "X":
    #             newP += "Z"
    #         else:
    #             newP += "X"
    #         continue
    #     newP += plainText[i]
    #     newP += plainText[i+1]
    
    # newP += plainText[-1]

    if len(newP)%2 == 1:
        if plainText[-1] == "X":
                newP += "Z"
        else:
            newP += "X"
    plainText = newP
    cipher = ""

#     FQKYVYUVXY
# FQKYVSVX
# ipmxxpzw


    for i in range(0,len(plainText)-1,2):
        l1 = plainText[i]
        ind1 = 0
        l2 = plainText[i+1]
        ind2 = 0
        for j, x in enumerate(arr):  
            if l1 in x:
                ind1 = (j, x.index(l1))
                break
        for j, x in enumerate(arr):  
            if l2 in x:
                ind2 = (j, x.index(l2))
                break
        
        if ind1[0] == ind2[0]:
            cipher += arr[ind1[0]][(ind1[1] + 1)%5]
            cipher += arr[ind2[0]][(ind2[1] + 1)%5]

        elif ind1[1] == ind2[1]:
            cipher += arr[ (ind1[0]+1)%5][ind1[1]]
            cipher += arr[ (ind2[0]+1)%5][ind2[1]]
        
        else:
            cipher += arr[ind1[0]][ind2[1]]
            cipher += arr[ind2[0]][ind1[1]]


    return cipher 
        




def read(fileLocaion):
    file = open(fileLocaion, "r")
    lis = file.read().split('\n')
    return lis

def write(fileLocaion, ciphers):
    file = open(fileLocaion, "w")
    for str in ciphers:
        file.write(str + "\n")


if __name__ == "__main__":

    # plains = read("caesar_plain.txt")
    # keys = [3,6,12]
    # out = []
    # for key in keys:
    #     out.append("your key is: " + str(key))
    #     for plain in plains:
    #         o = caeser(plain,key)
    #         out.append(o)  
    #     out.append("\n")
    # write("caesar_out.txt", out)


    #playfair('hidethegoldinthetrees',"PLAYFAIRExample")

    # plains = read("playfair_plain.txt") # playfair
    # keys = [ "RATS", "ARCHANGEL"]
    # ciphers = []
    # for k in keys:
    #     ciphers.append("key: " + str(k))
    #     for p in plains:
    #         ciphers.append(playfair(p,k))
    #     ciphers.append("\n")
    # write("playfair_cipher.txt", ciphers)


    while(True):
        print('Please Enter Plain Text:')
        plainText = input()
        print('Please Enter a key for Caesar Cipher:')
        key_c = int(input())
        print('Please Enter a key for Play Fair Cipher:')
        key_pf = int(input())

        print("Caesar Cipher:"+caeser(plainText,key_c))
        print("Play Fair Cipher:"+playfair(plainText,key_c))

        # print('input C for Caesar Cipher')
        # print('input PF for Play Fair Cipher')
        # print('input H for Hill Cipher')
        # print('input VI for Vigenere Cipher')
        # print('input VE for Vernam Cipher')
        # print('input EE for Exit')
        # method = input()
        # if method == 'EE':
        #     break

        # if not method in methods:
        #     print('error undifined input')
        
        # if method == 'C':
        #     print('Please Enter a Key')
        #     key = int(input())
        #     print(key)
    
