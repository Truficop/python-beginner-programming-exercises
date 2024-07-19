# ✅↓ Write your code here ↓✅
def number_of_bottles():
    num = 5
    for i in range(5):
        if num == 1:
            print(str(num) + ' bottle of milk on the wall, ' + str(num) + ' bottle of milk.')
            print('Take one down and pass it around, no more bottles of milk on the wall.\n')
            print('No more bottles of milk on the wall, no more bottles of milk.')
            num = 99
            print('Go to the store and buy some more, ' + str(num) + ' bottles of milk on the wall.')
        else:
            print(str(num) + ' bottles of milk on the wall, ' + str(num) + ' bottles of milk.')
            num -= 1
            print('Take one down and pass it around, ' + str(num) + ' bottles of milk on the wall.\n')
        

number_of_bottles()