from cipher.caesar import ALPHABET

class CaesarCipher:
    def __init__(self):  # Dùng __init__ thay vì _init__
        self.alphabet = ALPHABET

    def encrypt_text(self, text: str, key: int) -> str:
        alphabet_len = len(self.alphabet)  # Sửa lại cú pháp = 
        text = text.upper()  # Chuyển văn bản sang chữ hoa
        encrypted_text = []  # Tạo danh sách chứa văn bản đã mã hóa
        for letter in text:
            if letter in self.alphabet:  # Kiểm tra nếu ký tự nằm trong alphabet
                letter_index = self.alphabet.index(letter)  # Lấy chỉ số của ký tự trong alphabet
                output_index = (letter_index + key) % alphabet_len  # Tính toán chỉ số mã hóa
                output_letter = self.alphabet[output_index]  # Lấy chữ cái tương ứng
                encrypted_text.append(output_letter)  # Thêm ký tự vào kết quả
            else:
                encrypted_text.append(letter)  # Nếu không phải chữ cái, giữ nguyên ký tự
        return "".join(encrypted_text)  # Trả về chuỗi đã mã hóa

    def decrypt_text(self, text: str, key: int) -> str:
        alphabet_len = len(self.alphabet)  # Sửa lại cú pháp = 
        text = text.upper()  # Chuyển văn bản sang chữ hoa
        decrypted_text = []  # Tạo danh sách chứa văn bản đã giải mã
        for letter in text:
            if letter in self.alphabet:  # Kiểm tra nếu ký tự nằm trong alphabet
                letter_index = self.alphabet.index(letter)  # Lấy chỉ số của ký tự trong alphabet
                output_index = (letter_index - key) % alphabet_len  # Tính toán chỉ số giải mã
                output_letter = self.alphabet[output_index]  # Lấy chữ cái tương ứng
                decrypted_text.append(output_letter)  # Thêm ký tự vào kết quả
            else:
                decrypted_text.append(letter)  # Nếu không phải chữ cái, giữ nguyên ký tự
        return "".join(decrypted_text)  # Trả về chuỗi đã giải mã
