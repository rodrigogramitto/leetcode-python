list = ['a','b','c','d','e']

def loop(arr):
    print('Printing i in for I in list')
    for i in list:
        print(i)

    print('Printing I looping in range')
    for i in range(len(list), -1, -1):
      print(i)



loop(list)