def Nhan(a, b):
    # Chuyển mảng a và b thành chuỗi số nguyên
    num_a = int(''.join(map(str, a)))
    num_b = int(''.join(map(str, b)))
    
    # Thực hiện phép nhân
    result = num_a * num_b
    
    # Kiểm tra xem kết quả có tràn số không
    if result > 2**31 - 1:
        return [-1] * len(a)  # Trả về mảng gồm các số -1 nếu kết quả bị tràn
    else:
        return list(map(int, str(result)))  # Trả về kết quả nhân dưới dạng mảng số nguyên

# Sử dụng phương thức
a = [9, 8, 7]
b = [1, 2, 3]
print("Kết quả của a x b là:", Nhan(a, b))
