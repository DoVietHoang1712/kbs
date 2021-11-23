attributes = [
    ['cao', 'thấp'],
    ['dài', 'ngắn'],
    ['dài', 'ngắn'],
    ['khỏe', 'yếu'],
    ['khỏe', 'yếu'],
    ['khỏe', 'yếu'],
    ['tốt', 'kém'],
    ['tốt', 'kém'],
    ['tốt', 'kém'],
    ['nhanh', 'chậm']
]

samples = [
    ['cao', 'dài', '', 'khỏe', 'khỏe', 'khỏe', 'tốt', 'tốt', '','nhanh','Tennis'],
    ['cao', 'dài', 'dài', '', '', 'khỏe', 'tốt', 'tốt','','','Bơi'],
    ['','','','khỏe','','','tốt','','tốt','','Bắn cung'],
    ['', 'ngắn', 'ngắn', 'khỏe', 'khỏe', 'khỏe', 'tốt', 'tốt', 'tốt', '','Cử tạ'],
    ['','','','','khỏe','khỏe','tốt','tốt', '','nhanh','Chạy bền'],
    ['','','','khỏe','khỏe','khỏe','tốt','tốt','tốt','','Đấu vật'],
    ['cao', 'dài', '','','','khỏe','','tốt','','nhanh','Boxing'],
    ['', '', '', '','khỏe','khỏe','tốt','tốt','','nhanh','Bóng bàn'],
    ['', '', '', 'khỏe','khỏe','khỏe','','tốt','','nhanh','Cầu lông'],
    ['', '', '', '','khỏe','khỏe','','tốt','','','Đạp xe'],
    ['cao', 'dài', '', '','','khỏe','tốt','tốt','tốt','nhanh','Bóng rổ'],
    ['cao', '', '', 'khỏe','khỏe','khỏe','tốt','tốt','','nhanh','Bóng chuyền'],
    ['thấp', 'ngắn', 'ngắn', '','','khỏe','tốt','tốt','','','Thể dục dụng cụ'],
]

def fill(pos,s):
    if pos == 10:
        with open('dataset.txt', 'a', encoding='utf-8') as w:
            for i in range(11):
                w.write(s[i])
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