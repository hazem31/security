I = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]


CP_1 = [57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27,
        19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29,
        21, 13, 5, 28, 20, 12, 4]

CP_2 = [14, 17, 11, 24, 1, 5, 3, 28,
        15, 6, 21, 10, 23, 19, 12, 4,
        26, 8, 16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55, 30, 40,
        51, 45, 33, 48, 44, 49, 39, 56,
        34, 53, 46, 42, 50, 36, 29, 32]

E = [32, 1, 2, 3, 4, 5,
     4, 5, 6, 7, 8, 9,
     8, 9, 10, 11, 12, 13,
     12, 13, 14, 15, 16, 17,
     16, 17, 18, 19, 20, 21,
     20, 21, 22, 23, 24, 25,
     24, 25, 26, 27, 28, 29,
     28, 29, 30, 31, 32, 1]

S_BOX = [
         
[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
 [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
 [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
 [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
],

[[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
 [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
 [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
 [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
],

[[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
 [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
 [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
 [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
],

[[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
 [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
 [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
 [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
],  

[[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
 [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
 [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
 [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
], 

[[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
 [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
 [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
 [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
], 

[[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
 [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
 [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
 [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
],
   
[[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
 [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
 [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
 [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
]
]

#Permut made after each SBox substitution for each round
P = [16, 7, 20, 21, 29, 12, 28, 17,
     1, 15, 23, 26, 5, 18, 31, 10,
     2, 8, 24, 14, 32, 27, 3, 9,
     19, 13, 30, 6, 22, 11, 4, 25]

#Final permut for datas after the 16 rounds
PI_1 = [40, 8, 48, 16, 56, 24, 64, 32,
        39, 7, 47, 15, 55, 23, 63, 31,
        38, 6, 46, 14, 54, 22, 62, 30,
        37, 5, 45, 13, 53, 21, 61, 29,
        36, 4, 44, 12, 52, 20, 60, 28,
        35, 3, 43, 11, 51, 19, 59, 27,
        34, 2, 42, 10, 50, 18, 58, 26,
        33, 1, 41, 9, 49, 17, 57, 25]

#Matrix that determine the shift for each round of keys
SHIFT = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]

def hex_To_bin(s): 
    dic = {'0' : "0000",  
          '1' : "0001", 
          '2' : "0010",  
          '3' : "0011", 
          '4' : "0100", 
          '5' : "0101",  
          '6' : "0110", 
          '7' : "0111",  
          '8' : "1000", 
          '9' : "1001",  
          'A' : "1010", 
          'B' : "1011",  
          'C' : "1100", 
          'D' : "1101",  
          'E' : "1110", 
          'F' : "1111" } 
    bin = "" 
    for i in range(len(s)):
        bin += dic[s[i]] 
    return bin
      

def bin_To_hex(s): 
    dic = {"0000" : '0',  
          "0001" : '1', 
          "0010" : '2',  
          "0011" : '3', 
          "0100" : '4', 
          "0101" : '5',  
          "0110" : '6', 
          "0111" : '7',  
          "1000" : '8', 
          "1001" : '9',  
          "1010" : 'A', 
          "1011" : 'B',  
          "1100" : 'C', 
          "1101" : 'D',  
          "1110" : 'E', 
          "1111" : 'F' } 
    hex = "" 
    for i in range(0,len(s),4): 
        ch = "" 
        ch += s[i] 
        ch += s[i + 1]  
        ch += s[i + 2]  
        ch += s[i + 3]  
        hex += dic[ch] 
          
    return hex
  

def str_to_list(s):
	ls = []
	for char in s:
		ls.append(char)
	return ls

def list_to_str(ls):
	s = ""
	for char in ls:
		s += char
	return s


def strbin_To_num(strbin):
    num = int(strbin, 2)
    return num


# def num_To_strbin(num,pad):
#     strbin = bin(num)
#     strbin = strbin.replace("0b","")
# 	temp = ""
#     for i in range(pad - len(strbin)):
#         temp += "0"
        
#     return temp + strbin

def num_To_strbin(num,pad):
	strbin = bin(num)
	strbin = strbin.replace('0b','')
	temp = ''
	for i in range(pad -len(strbin)):
		temp += '0'
	
	return temp + strbin

def apply_perm(ls,perm):
	temp = []
	for i in perm:
		temp.append(ls[i-1])
	
	return temp

def split_to(ls,n):
	splits = []
	for i in range(n):
		sp = []
		for j in range(int(len(ls)/n)):
			v = int(len(ls)/n)
			sp.append(ls[v * i + j])
		splits.append(sp)
	return splits

def shift_key(key,i):
	return key[i:] + key[:i]

def get_keys(init_key):
	keys = []
	key = apply_perm(init_key,CP_1)
	for i in range(16):
		temp = []
		key = split_to(key,2)
		k1 = shift_key(key[0],SHIFT[i])
		k2 = shift_key(key[1],SHIFT[i])
		key = k1 + k2
		t = apply_perm(key,CP_2)
		keys.append(t)

	return keys

def xor(x,y):
	res = []
	for i in range(len(x)):
		if x[i] == y[i]:
			res.append('0')
		else:
			res.append('1')
	return res

def subs(ls):
	ls = split_to(ls,8)
	res = []
	for i in range(8):
		cho = ls[i][0] + ls[i][-1]
		cho_h = strbin_To_num(cho)
		cho_v = ls[i][1] + ls[i][2] + ls[i][3] + ls[i][4]
		cho_v = strbin_To_num(cho_v)
		t = S_BOX[i][cho_h][cho_v]
		t = num_To_strbin(t,4)
		for c in t:
			res.append(c)
	return res



def round(inp,key):
	inp = split_to(inp,2)
	L = inp[0]
	R = inp[1]
	nL = R
	nR = apply_perm(R,E)
	nR = xor(nR,key)
	nR = subs(nR)
	nR = apply_perm(nR,P)
	nR = xor(nR,L)
	return nL + nR

def des_enc(pt,key):
	key = hex_To_bin(key)
	key = str_to_list(key)
	keys = get_keys(key)
	inp = hex_To_bin(pt)
	inp = str_to_list(inp)
	inp = apply_perm(inp,I)
	for i in range(16):
		inp = round(inp,keys[i])
	t = inp[32:] + inp[:32]
	res = apply_perm(t,PI_1)
	res = list_to_str(res)
	res = bin_To_hex(res)
	return res


def des_dec(ci,key):
	key = hex_To_bin(key)
	key = str_to_list(key)
	keys = get_keys(key)
	keys = keys[::-1]
	inp = hex_To_bin(ci)
	inp = str_to_list(inp)
	inp = apply_perm(inp,I)
	for i in range(16):
		inp = round(inp,keys[i])
	t = inp[32:] + inp[:32]
	res = apply_perm(t,PI_1)
	res = list_to_str(res)
	res = bin_To_hex(res)
	return res



if __name__ == "__main__":

	while(True):
		print('please enter 16 hex chars for the key:')
		key = input()
		print('please enter 16 hex chars for the plain text:')
		pt = input()
		print('please enter an int for number of times to run')
		num = int(input())
		res = pt
		for i in range(num):
			res = des_enc(res,key)

		print('output cipher is : ' + res)
		print('\n')
		print('if want to exit type (y)')
		ic = input()
		if ic == 'y':
			break
		



# key = hex_To_bin(key)
# key = str_to_list(key)
# keys = get_keys(key)

# inp = hex_To_bin(pt)
# inp = str_to_list(inp)
# inp = apply_perm(inp,I)
# res = round(inp,keys[0])
# res = round(res,keys[1])
# res = list_to_str(res)
# res = bin_To_hex(res)
# print(res[8:])
# print(res[:8])
# res = split_to(res,2)
# print(res[0],res[1])

# for key in keys:
# 	l = list_to_str(key)
# 	l = bin_To_hex(l)
# 	print(l)
# s = '0123456789ABCDEF'
# s1 = hex_To_bin(s)
# s2 = bin_To_hex(s1)
# s3 = strbin_To_num(s1)
# s4 = num_To_strbin(s3,64)
# print(s,s1)
# print(s2,s3)
# print(s4)

# binary_str = '0110' # Binary string
# binary_str2 = '0111'

# num2 = int(binary_str2, 2)
# num = int(binary_str, 2)

# v = num ^ num2

# print(num_To_strbin(v,4))