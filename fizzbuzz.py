so = input ('Nhập 1 số bất kì: ')
intro= int(so[0])
outro= int(so[-1])

if outro < intro:
    print('Số kết thúc phải lớn hơn số bắt đầu')
else:
    for i in range(intro, outro+1):
        if i % 3 == 0 and i% 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i% 5 == 0:
            print('Buzz')
        else:
            print(i)
