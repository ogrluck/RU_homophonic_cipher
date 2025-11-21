import random
homophones = {
    'а': ['б', 'в', 'г'],
    'б': ['д', 'е', 'ж'],
    'в': ['з', 'и', 'к'],
    'г': ['л', 'м', 'н'],
    'д': ['о', 'п', 'р'],
    'е': ['с', 'т', 'у'],
    'ж': ['ф', 'х', 'ц'],
    'з': ['ч', 'ш', 'щ'],
    'и': ['ъ', 'ы', 'ь'],
    'к': ['э', 'ю', 'я'],
    'л': ['а', 'б', 'в'],
    'м': ['г', 'д', 'е'],
    'н': ['ж', 'з', 'и'],
    'о': ['к', 'л', 'м'],
    'п': ['н', 'о', 'п'],
    'р': ['р', 'с', 'т'],
    'с': ['у', 'ф', 'х'],
    'т': ['ц', 'ч', 'ш'],
    'у': ['щ', 'ъ', 'ы'],
    'ф': ['ь', 'э', 'ю'],
    'х': ['я', 'а', 'б'],
    'ц': ['в', 'г', 'д'],
    'ч': ['е', 'ж', 'з'],
    'ш': ['и', 'к', 'л'],
    'щ': ['м', 'н', 'о'],
    'ъ': ['п', 'р', 'с'],
    'ы': ['т', 'у', 'ф'],
    'ь': ['х', 'ц', 'ч'],
    'э': ['ш', 'щ', 'ъ'],
    'ю': ['ы', 'ь', 'э'],
    'я': ['ю', 'я', 'а'],
}
def homophonic_cipher(text):
    cipher_text = ""
    for char in text:
        if char.lower() in homophones:
            # Случайный выбор омофона
            replacement = random.choice(homophones[char.lower()])
            if char.isupper():  # Сохраняем регистр
                replacement = replacement.upper()
            cipher_text += replacement
        else:
            cipher_text += char 
    return cipher_text

plaintext = input()
ciphertext = homophonic_cipher(plaintext)
print("Оригинал:", plaintext)
print("Энкодированный текст:", ciphertext)
input()
