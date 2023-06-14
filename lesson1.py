# def count_string(string):
#     for symbol in set(string):#set - множество,все значения уникальны
#         counter = 0
#         for other_symbol in string:
#             if symbol == other_symbol:
#                 counter += 1
#         else:
#             print(f"Буква'{symbol}' встречается {counter} раз")
#
# count_string('ggggsssddd')

def count_string(string):
    result = {}
    for symbol in string:
        result[symbol] = result.get(symbol, 0) +1  #второе значение в скобках это значение по умолчанию возвращается если такой позиции нет,гет лучше получения по ключу потому что не выдает ошибку в случае если не нашел, а возвращает ноне

    for s in result:
        print(s,result[s])

count_string('ggggsssddd')
