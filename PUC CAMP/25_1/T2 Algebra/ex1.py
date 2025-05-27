from sympy import Matrix

def text_to_numbers(text):
    # Converte texto para números (A=0, B=1, ..., Z=25)
    return [ord(c) - ord('A') for c in text.upper() if c.isalpha()]

def numbers_to_text(numbers):
    # Converte números para texto
    return ''.join([chr(n % 26 + ord('A')) for n in numbers])

def hill_decrypt(ciphertext, key_matrix):
    modulus = 26
    inv_key = Matrix(key_matrix).inv_mod(modulus)
    cipher_nums = text_to_numbers(ciphertext)
    # Preenche com 'X' se necessário para múltiplo de 2
    if len(cipher_nums) % 2 != 0:
        cipher_nums.append(ord('X') - ord('A'))
    plaintext_nums = []
    for i in range(0, len(cipher_nums), 2):
        pair = Matrix([cipher_nums[i], cipher_nums[i+1]])
        decrypted = inv_key * pair
        decrypted = [int(x) % modulus for x in decrypted]
        plaintext_nums.extend(decrypted)
    return numbers_to_text(plaintext_nums)

def hill_encrypt(plaintext, key_matrix):
    modulus = 26
    key = Matrix(key_matrix)
    plain_nums = text_to_numbers(plaintext)
    # Preenche com 'X' se necessário para múltiplo de 2
    if len(plain_nums) % 2 != 0:
        plain_nums.append(ord('X') - ord('A'))
    cipher_nums = []
    for i in range(0, len(plain_nums), 2):
        pair = Matrix([plain_nums[i], plain_nums[i+1]])
        encrypted = key * pair
        encrypted = [int(x) % modulus for x in encrypted]
        cipher_nums.extend(encrypted)
    return numbers_to_text(cipher_nums)

# Chave correta conforme imagem: [[4, 3], [1, 2]]
chave = [[4, 3], [1, 2]]
texto_cifrado = "KDVHEM"
print(hill_decrypt(texto_cifrado, chave))
texto_plano = "BATEBOTA"
print(hill_encrypt(texto_plano, chave))