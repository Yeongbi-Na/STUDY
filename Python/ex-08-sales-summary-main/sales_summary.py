def sort_sales(data):
    #===== write your code below =======
    data2=dict(data)



    for i in range(len(data)):
        for j in range(len(data)):
            if i != j and data[i][0]==data[j][0]:
                data2[data[i][0]]=data[i][1]+data[j][1]
    data=list(zip(data2.keys(),data2.values()))              
    for i in range(len(data)):
        for i in range(len(data)-1):
            if data[i][1]<=data[i+1][1]:
                temp= data[i]
                data[i]=data[i+1]
                data[i+1]=temp
    return list(data)

def sales_summary(data):
    #===== write your code below ====
    rank=[]
    product=[]
    num=[]
    for i in range(len(data)):
        if i>=1 and data[i-1][1]==data[i][1]:
            rank.append(rank[i-1])
        else:
            rank.append(i+1)
        product.append(data[i][0])
        num.append(data[i][1])
        
    return list(zip(product,num, rank))




if __name__ == '__main__':
    data =[('apple', 14),('pencil', 14),('book', 8),('orange', 6),('beer', 4),('beer', 2),('paper', 3)]
    sorted_sales = sort_sales(data)
    summary = sales_summary(sorted_sales)   