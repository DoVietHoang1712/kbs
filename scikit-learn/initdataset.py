attributes = [
    [1, 0],
    [1, 0],
    [1, 0],
    [1, 0],
    [1, 0],
    [1, 0],
    [1, 0],
    [1, 0],
    [1, 0],
    [1, 0]
]

samples = [
    [1, 1, '', 1, 1, 1, 1, 1, '',1,'Tennis'],
    [1, 1, 1, '', '', 1, 1, 1,'','','Boi'],
    ['','','',1,'','',1,'',1,'','Ban cung'],
    ['', 0, 0, 1, 1, 1, 1, 1, 1, '','Cu ta'],
    ['','','','',1,1,1,1, '',1,'Chay ben'],
    ['','','',1,1,1,1,1,1,'','Dau vat'],
    [1, 1, '','','',1,'',1,'',1,'Boxing'],
    ['', '', '', '',1,1,1,1,'',1,'Bong ban'],
    ['', '', '', 1,1,1,'',1,'',1,'Cau long'],
    ['', '', '', '',1,1,'',1,'','','Dap xe'],
    [1, 1, '', '','',1,1,1,1,1,'Bong ro'],
    [1, '', '', 1,1,1,1,1,'',1,'Bong chuyen'],
    [0, 0, 0, '','',1,1,1,'','','The duc dung cu'],
]

def fill(pos,s):
    if pos == 10:
        with open('scikit-learn/dataset.txt', 'a') as w:
            for i in range(11):
                w.write(str(s[i]))
                if i < 10:
                    w.write(',')
                else:
                    w.write('\n')
    else:
        if s[pos] != '':
            fill(pos + 1, s)
        else:
            for i in attributes[pos]:
                s[pos] = i
                fill(pos+1,s)
                s[pos] = ''

if __name__ == '__main__':
    for s in samples:
        fill(0,s)