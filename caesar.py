import string
def encrypt(key,plaintext):
    ciphertext=""
    #YOUR CODE HERE
    
    alpha2num = dict(zip(string.ascii_uppercase, range(0, 26)))
    num2alpha = dict(zip(range(0, 26), string.ascii_uppercase))
    num_rep = []
    
    for letter in plaintext:
        num = alpha2num.get(letter)
        encrypted_num = (num + key) % 26
        num_rep.append(encrypted_num)
    
    for num in num_rep:
        letter = num2alpha.get(num)
        ciphertext += letter
    return ciphertext

def decrypt(key,ciphertext):
    plaintext=""
    #YOUR CODE HERE
    
    alpha2num = dict(zip(string.ascii_uppercase, range(0, 26)))
    num2alpha = dict(zip(range(0, 26), string.ascii_uppercase))
    num_rep = []
    
    for letter in ciphertext:
        num = alpha2num.get(letter)
        encrypted_num = (num - key) % 26
        num_rep.append(encrypted_num)
        
    for num in num_rep:
        letter = num2alpha.get(num)
        plaintext += letter
    
    return plaintext


