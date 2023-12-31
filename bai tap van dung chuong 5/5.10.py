import sqlite3

def HienThi():
    conn = sqlite3.connect('product.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM product')
    products = cursor.fetchall()
    conn.close()

    for product in products:
        print(product)

def ThemSanPham(name, price, amount):
    conn = sqlite3.connect('product.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO product (Name, Price, Amount) VALUES (?, ?, ?)', (name, price, amount))
    conn.commit()
    conn.close()

def TimSanPhamTheoTen(name):
    conn = sqlite3.connect('product.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM product WHERE Name LIKE ?', ('%' + name + '%',))
    products = cursor.fetchall()
    conn.close()

    for product in products:
        print(product)

def CapNhatDonGia(id, price, amount):
    conn = sqlite3.connect('product.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE product SET Price=?, Amount=? WHERE Id=?', (price, amount, id))
    conn.commit()
    conn.close()

def XoaSanPham(id):
    conn = sqlite3.connect('product.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM product WHERE Id=?', (id,))
    conn.commit()
    conn.close()

def Menu():
    print("1. Hiển thị danh sách sản phẩm")
    print("2. Thêm sản phẩm mới")
    print("3. Tìm kiếm sản phẩm theo tên")
    print("4. Cập nhật đơn giá và số lượng của sản phẩm")
    print("5. Xóa sản phẩm theo ID")
    print("6. Thoát")

def main():
    while True:
       def LuaChon():
        choice =int(input("Nhập vào lựa chọn của bạn: "))
        if choice == 1:
            HienThi()
        elif choice == 2:
            name = input("Nhập tên sản phẩm: ")
            price = float(input("Nhập đơn giá: "))
            amount = int(input("Nhập số lượng: "))
            ThemSanPham(name, price, amount)
        elif choice == 3:
            search_name = input("Nhập tên sản phẩm cần tìm kiếm: ")
            TimSanPhamTheoTen(search_name)
        elif choice == 4:
            update_id = int(input("Nhập ID sản phẩm cần cập nhật: "))
            new_price = float(input("Nhập đơn giá mới: "))
            new_amount = int(input("Nhập số lượng mới: "))
            CapNhatDonGia(update_id, new_price, new_amount)
        elif choice == 5:
            delete_id = int(input("Nhập ID sản phẩm cần xóa: "))
            XoaSanPham(delete_id)
        elif choice == 6:
            print("Đã thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")

if __name__ == "__main__":
    main()
