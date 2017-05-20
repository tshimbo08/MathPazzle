'''
10 進数、 2 進数、 8 進数 の いずれ で 表現 し ても 回文 数 と なる 数 の うち、 10 進数 の 10 以上 で 最小 の 値 を 求め て ください。

'''

def isKai(indata):
    '''
    kaibunn
    :param string input:data 
    :return: 
    '''
    data = indata[::-1]
    if data == indata :
        return True
    return False

def main(number):
    '''
    main
    :param int number: 
    :return: 
    '''
    if isKai(str(number)) and isKai(str(oct(number))[2::]) and isKai(str(bin(number))[2::]):
        print(number)


if __name__ == '__main__':
    for n in range(11,1000,2):
        main(n)
