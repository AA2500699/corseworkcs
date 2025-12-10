from encrypt import encrypt_block
from decrypt import decrypt_block
from keygen import generate_round_keys
import random

# ----------------- Helper to generate random 64-bit strings -----------------
def random_64bit_string():
    return ''.join(random.choice('01') for _ in range(64))

# ----------------- Main Test -----------------
if __name__ == "__main__":
    # Generate random plaintext and key
    plaintext = random_64bit_string()
    key = random_64bit_string()

    print("Random 64-bit Key:      ", key)
    print("Random 64-bit Plaintext:", plaintext)

    # Generate round keys
    round_keys = generate_round_keys(key)
    if not round_keys:
        raise ValueError("Round key generation failed!")
    
    # Encrypt
    ciphertext = encrypt_block(plaintext, round_keys)
    print("Ciphertext:             ", ciphertext)

    # Decrypt
    decrypted = decrypt_block(ciphertext, round_keys)
    print("Decrypted text:         ", decrypted)

    # Verify
    if decrypted == plaintext:
        print("SUCCESS: Decryption matches the original plaintext!")
    else:
        print("FAILURE: Decryption does not match the original plaintext.")
