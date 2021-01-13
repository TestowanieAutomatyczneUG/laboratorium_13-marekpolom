class Roman:
    def roman(n):
        num = {
            1: 'I',
            5: 'V',
            10: 'X',
            50: 'L',
            100: 'C',
            500: 'D',
            1000: 'M'
        }

        numeral = ''

        x = n

        while x>0:
            a = 0

            for i in list(num.keys()):
                if x < i:
                    a = i
                    break
            
            if a == 0:
                a = 1000


            b = list(str(a))

            if(int(b[0]) > 1):
                b[0] = '1'
            else:
                b = b[:-1]

            b = int(''.join(b))


            c = list(num.keys())
            index = c.index(a)

            c = c[index-1]


            if (x - a) >= 0 :

                x -= a

                numeral += num[a]

            elif (x - (a - b) >= 0):

                x -= (a-b)

                numeral += num[b]
                numeral += num[a]

            elif (x - c) >= 0:

                x -= c

                numeral += num[c]

        return(numeral)