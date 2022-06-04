def main():
    #===== write your code below =======
    
  
  sum=0
  n=0
  while 1:

    x=float(input())
    if x<0 or x>100:
      break
    sum=sum+x
    n=n+1

  print("%.2f" %(sum/n))
  print("{0:%.2f}".format(sum/n))  


if __name__ == '__main__':
    main()