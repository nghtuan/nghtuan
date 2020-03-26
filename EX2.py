#coding=utf-8
'''
Khai báo biến: tenBien = giaTri
Trong đó:
	tenBien: là tên của biến mà các bạn muốn đặt. Tên biến này không được bắt đầu bằng số hay các ký tự đặc biệt, mà chỉ được bắt đầu bằng chữ cái hoặc ký tự _ và nó có phân biệt hoa thường
	giaTri: là giá trị của biến mà bạn muốn gán 
VD: count = 0
'''
# dasdsadsadasd
'''
Các kiểu dữ liệu cơ bản trong python: string, integer, float, list, tuple, dictionnary.
'''

#Kiểu dữ liệu str
name = "Nguyễn Văn Toàn"

#Kiểu dữ liệu int
age = 20

#Kiểu dữ liệu float
point = 7.1

#Kiểu dữ liệu list
option = [1, 2, 3, 4]

#Kiểu dữ liệu tuple
tuple = ('Nguyễn Văn Toàn', 20, True)

#Kiểu dữ liệu dict
dictionary = {"name": "Nguyễn Văn Toàn", "age": 20, "point": 7.1}

'''
Kiểm tra kiểu dữ liệu: type(data)
Trong đó data là tên biến cần kiểm tra
'''

#Kiểu dữ liệu string
name = "Nguyễn Văn Toàn"
print(type(name))

#Kiểu dữ liệu int
age = 20
print(type(age))

asdasdsad
#Kiểu dữ liệu float
point = 7.1
print(type(point))

#Kiểu dữ liệu list
option = [1, 2, 3, 4]
print(type(option))

#Kiểu dữ liệu tuple
tuple = ('Nguyễn Văn Toàn', 20, True)
print(type(tuple))

#Kiểu dữ liệu dict
dictionary = {"name": "Nguyễn Văn Toàn", "age": 20, "point": 7.1}
print(type(dictionary))

'''
Ép kiểu dữ liệu
Các hàm ép kiểu cơ bản:
	float(data) chuyển đổi sang kiểu số thực.
	int(data,base) chuyển đổi sang kiểu số, trong đó base là kiểu hệ số mà các bạn muốn chuyển đổi sang (tham số này có thể bỏ trống).
	str(data) chuyển đổi sang dạng chuỗi.
	complex(data) chuyển đổi sang kiểu phức hợp.
	tuple(data) chuyển đổi sang kiểu Tuple.
	dict(data) chuyển đổi sang kiểu Dictionary.
	hex(data) chuyển đổi sang hệ 16.
	oct(data) chuyển đổi sang hệ 8.
	chr(data) chuyển đổi sang dạng ký tự.
'''

age = 20;

# ép sang float
floatAge = float(age)
print(type(floatAge))

#ép sang integer.
intAge = int(age)
print(type(intAge))

#ép sang chuỗi.
strAge = str(age)
print(type(strAge))
