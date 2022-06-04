from collections import OrderedDict
def sort_sales(data):

    temp_product=dict.fromkeys(list(zip(*data))[0],0)
    for x in data:
        temp_product[x[0]]+=x[1]

    sorted_dict=OrderedDict(sorted(temp_product.items(), key = lambda x:x[1], reverse=True))
    return list(zip(sorted_dict.keys(),sorted_dict.values()))


def sales_summary(data):
    temp_rank=list(range(1,len(data)+1))
    temp_values=[x[1] for x in data]
    temp_keys=[x[0] for x in data]
    for i in range(len(data)-1):
        if temp_values[i]==temp_values[i+1]:
            temp_rank[i+1]=temp_rank[i]
    
    result=list(zip(temp_keys,temp_values, temp_rank))
    return result


if __name__ == '__main__':
    data =[('apple', 2),('pencil', 10),('book', 8),('orange', 6),('beer', 4),('beer', 2),('paper', 3)]
    sorted_sales = sort_sales(data)
    summary = sales_summary(sorted_sales)
    print(summary)