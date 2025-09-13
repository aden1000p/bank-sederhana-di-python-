dictionary = {
    '092381':{'nama':'fadly', 'Harga':1000000},
    '083211':{'nama':'asep', 'Harga':50000}
}


# def transfer_uang(key):
#     global dictionary
#     if dictionary[key] == dictionary[key]:
#         guess = int(input("silahkan mau kirim berapa : "))
#         dictionary['083211']['Harga'] -= guess
#         dictionary['092381']['Harga'] += guess
        
#         for x, y in dictionary.items():
#             print(f"{x} {y.values()}")

# for i in range(1):
#     key = input("masukan hash key: ")
#     nama = input("masukan nama: ")
#     harga = int(input("masukan harga yang diinput: "))
#     dictionary[key] = {'nama':nama, 'harga': harga}
#     print("data telah ditambahkan ")

# print(dictionary)

def quickSort(array):
    if len(array) < 2:
        return array

    else:
        pivot = array[0]
        
        less = [x for x in array[1:] if pivot <= x]
        
        depan = [i for i in array[1:] if pivot > i]
        
        return quickSort(less) + [pivot] + quickSort(depan)

list = [['fadly', 3000], ['aden', 500], ['ryan',200]]


print(quickSort(list))