from collections import OrderedDict
def sort_sales(data):
    prduct_data=list(zip(*data))[0]
    temp_data=dict.fromkeys(prduct_data,0)
    #품목별로 합치기
    for x in data:
        temp_data[x[0]]+=x[1]


    #품목들 정렬, 내림차순
    sorted_dict=OrderedDict(sorted(temp_data.items(), key = lambda x:x[1], reverse=True))
    return list(zip(sorted_dict.keys(),sorted_dict.values()))


def sales_summary(temp_data):
    temp_data=OrderedDict(temp_data)
    temp_rank=list(range(1,len(temp_data)+1))
    temp_values=list(temp_data.values())
    for i in range(len(temp_values)-1):
        if temp_values[i]==temp_values[i+1]:
            temp_rank[i+1]=temp_rank[i]
    summary_data=list(zip(list(temp_data.keys()),list(temp_data.values()),temp_rank))
    return summary_data



if __name__ == '__main__':
    data = [('apple', 5), ('beer', 2), ('pencil', 1), 
            ('beer', 2), ('book', 8), ('apple', 9),
            ('paper', 3), ('pencil', 13), ('orange', 6),('paper',5)]

    sort_data=sort_sales(data)
    print(sort_data)
    fianl =sales_summary(sort_data)
    print(fianl)