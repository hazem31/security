import numpy as np

s_box = (
    0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
    0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
    0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
    0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
    0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
    0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
    0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
    0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
    0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
    0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
    0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
    0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
    0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
    0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
    0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
    0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16,
)

inv_s_box = (
    0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB,
    0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB,
    0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E,
    0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25,
    0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92,
    0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84,
    0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06,
    0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B,
    0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73,
    0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E,
    0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B,
    0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4,
    0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F,
    0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF,
    0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61,
    0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D,
)


r_con = (
    0x00, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40,
    0x80, 0x1B, 0x36, 0x6C, 0xD8, 0xAB, 0x4D, 0x9A,
    0x2F, 0x5E, 0xBC, 0x63, 0xC6, 0x97, 0x35, 0x6A,
    0xD4, 0xB3, 0x7D, 0xFA, 0xEF, 0xC5, 0x91, 0x39,
)




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


def num_To_strbin(num,pad):
	strbin = bin(num)
	strbin = strbin.replace('0b','')
	temp = ''
	for i in range(pad -len(strbin)):
		temp += '0'

def get_first_as_int(x):
    x = hex(x)
    x = int(x[:-1],16)
    return x

def get_second_as_int(x):
    x = hex(x)
    x = int(x[3:],16)
    return x


def split_to_mat(s):
    temp1 = []
    temp2 = []
    temp3 = []
    temp4 = []
    temp = []
    for i in range(0,len(s),8):
        temp1.append(s[i:i+2])
    temp.append(temp1)
    for i in range(2,len(s),8):
        temp2.append(s[i:i+2])
    temp.append(temp2)
    for i in range(4,len(s),8):
        temp3.append(s[i:i+2])
    temp.append(temp3)
    for i in range(6,len(s),8):
        temp4.append(s[i:i+2])
    temp.append(temp4)

    return temp

def convert_to_matrix(s):
    temp = []
    s = split_to_mat(s)
    for i in range(4):
        for j in range(4):
            s[i][j] = int(s[i][j],16)
    return np.array(s)

def return_to_str(s):
    temp = ''
    s1 = np.array(s.T,copy=True)
    for i in range(4):
        for j in range(4):
            v = hex(s1[i,j])[2:].upper()
            if len(v) == 1:
                v = '0' + v
            temp += v
    return temp

def look_sub(num):
    first = int(num/16)
    second = num % 16
    t = s_box[16*first+second]
    t = hex(t)[2:]
    t = int(t,16)
    return t

def subs(s):
    for i in range(s.shape[0]):
        for j in range(s.shape[1]):
            s[i][j] = look_sub(s[i][j])
    return s

def look_isub(num):
    first = int(num/16)
    second = num % 16
    t = inv_s_box[16*first+second]
    t = hex(t)[2:]
    t = int(t,16)
    return t


def inv_subs(s):
    for i in range(s.shape[0]):
        for j in range(s.shape[1]):
            s[i][j] = look_isub(s[i][j])
    return s


def g_func(key,i):
    s = np.array(key,copy=True)
    s = s[:,3:4]
    v = s[0,0]
    s = s[1:,:].tolist()
    v = [v]
    s.insert(3,v )
    s = np.array(s)
    s = subs(s)
    s[0,0] = s[0,0] ^ r_con[i]
    return s

def get_keys(key):
    key  = convert_to_matrix(key)
    keys = []
    keys.append(key)
    for i in range(1,11,1):
        temp = np.array(key,copy=True)
        t = g_func(keys[i-1],i)
        for j in range(key.shape[1]):
            v = keys[i-1][:,j:j+1]
            temp[:,j:j+1] = np.bitwise_xor(v ,t)
            t = temp[:,j:j+1]
        keys.append(temp)        
    return keys

def add_round_key(s,key):
    return s ^ key

def shift_rows(s):
    shifts = [0,1,2,3]
    temp = np.array(s,copy=True)
    for i in range(1,4,1):
        s1 = s[i:i+1,shifts[i]:]
        s2 = s[i:i+1,:shifts[i]]
        temp[i:i+1,:] = np.concatenate((s1,s2),axis=1)
    return temp

def inv_shift_rows(s):
    shifts = [0,1,2,3]
    temp = np.array(s,copy=True)
    for i in range(1,4,1):
        s1 = s[i:i+1,4-shifts[i]:]
        s2 = s[i:i+1,:4-shifts[i]]
        temp[i:i+1,:] = np.concatenate((s1,s2),axis=1)
    return temp


xtime = lambda a: (((a << 1) ^ 0x1B) & 0xFF) if (a & 0x80) else (a << 1)

def mix_single_column(a):
    t = a[0] ^ a[1] ^ a[2] ^ a[3]
    u = a[0]
    a[0] ^= t ^ xtime(a[0] ^ a[1])
    a[1] ^= t ^ xtime(a[1] ^ a[2])
    a[2] ^= t ^ xtime(a[2] ^ a[3])
    a[3] ^= t ^ xtime(a[3] ^ u)
    return np.array(a).reshape(4,1)


def mix_columns(s):
    temp = np.array(s,copy=True)
    for i in range(4):
        v = s[:,i]
        v = v.tolist()
        v = mix_single_column(v)
        temp[:,i:i+1] = v
    return temp


def inv_mix_columns(s):
    temp = np.array(s,copy=True)
    temp = temp.T
    s = temp.tolist()
    for i in range(4):
        u = xtime(xtime(s[i][0] ^ s[i][2]))
        v = xtime(xtime(s[i][1] ^ s[i][3]))
        s[i][0] ^= u
        s[i][1] ^= v
        s[i][2] ^= u
        s[i][3] ^= v
    s = np.array(s)
    s = s.T
    s = mix_columns(s)
    return s

def round(s,key):
    s = subs(s)
    s = shift_rows(s)
    s = mix_columns(s)
    s = add_round_key(s,key)
    return s

def inv_round(s,key):
    s = inv_shift_rows(s)
    s = inv_subs(s)
    s = add_round_key(s,key)
    s = inv_mix_columns(s)
    return s

def inv_final_round(s,key):
    s = inv_shift_rows(s)
    s = inv_subs(s)
    s = add_round_key(s,key)
    return s

def final_round(s,key):
    s = subs(s)
    s =shift_rows(s)
    s = add_round_key(s,key)
    return s

def aes_enc(pt,key):
    keys = get_keys(key)    
    s = convert_to_matrix(pt)
    s = add_round_key(s,keys[0])
    for i in range(1,10,1):
        s = round(s,keys[i])
    s = final_round(s,keys[-1])
    s = return_to_str(s)
    return s

def aes_dec(cipher,key):
    keys = get_keys(key)
    keys = keys[::-1]    
    s = convert_to_matrix(cipher)
    s = add_round_key(s,keys[0])
    for i in range(1,10,1):
        s = inv_round(s,keys[i])
    s = inv_final_round(s,keys[-1])
    s = return_to_str(s)
    return s

key = '0123456789ABCDEF0123456789ABCDEF'
pt = '0123456789ABCDEF0123456789ABCDEF'

pt2 = '54776F204F6E65204E696E652054776F'
key2 = '5468617473206D79204B756E67204675'



if __name__ == "__main__":

	while(True):
		print('please enter 32 hex chars for the key:')
		key = input()
		print('please enter 32 hex chars for the plain text:')
		pt = input()
		res = aes_enc(pt,key)
		print('output cipher is : ' + res)
		print('\n')
		print('if want to exit type (y)')
		ic = input()
		if ic == 'y':
			break
		


# s = aes_enc(pt,key)
# #print(s)
# for i in range(0,len(s),2):
#     print(s[i:i+2],end=' ')
# print()

# s = aes_dec(s,key)
# for i in range(0,len(s),2):
#     print(s[i:i+2],end=' ')

# keys = get_keys(key2)
# s = convert_to_matrix(pt2)

# s = add_round_key(s,keys[0])
# print(s)
# s = round(s,keys[1])
# print(s)
# s = inv_round(s,keys[1])
# print(s)
#print(s)
#s = subs(s)
#print(s)
#s = inv_subs(s)
#print(s)
#s = shift_rows(s)
#print(s)
#print(s)
#s = mix_columns(s)
#print(s)
#s = add_round_key(s,keys[1])
#print(s)
#s = return_to_str(s)
#print(s)
# for key in s:
#     print(key)

#print(pt)
#print(return_to_str(s))

# s = subs(s)
# print(s)