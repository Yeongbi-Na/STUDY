from collections import OrderedDict

def sort_sales(data):
    temp_product=list(zip(*data))[0]
    product=dict.fromkeys(temp_product,0)
    for x in data:
        product[x[0]]+=x[1]
    return product

def sales_summary(data):
    #===== write your code below ====
    
    sorted_dict=OrderedDict(sorted(data.items(), key = lambda x:x[1], reverse=True))
    temp_rank=list(range(1,len(sorted_dict)+1))
    temp_values=list(sorted_dict.values())
    for i in range(len(sorted_dict)-1):
        if temp_values[i]==temp_values[i+1]:
            temp_rank[i+1]=temp_rank[i]

    result=list(zip(sorted_dict.keys(),sorted_dict.values(),temp_rank))


    return result

if __name__ == '__main__':
    data =[('apple', 14),('pencil', 14),('book', 8),('orange', 6),('beer', 4),('beer', 2),('paper', 3)]
    sorted_sales = sort_sales(data)
    summary = sales_summary(sorted_sales)
    print(summary)
