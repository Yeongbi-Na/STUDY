setwd("C:\\Users\\user\\Desktop\\2021-1\\데이터 마이닝 입문\\실습\\Decisition Tree")

#대출 가능여부 파악>>화이트박스 알고리즘을 사용해야함

#stringsAsFactors 디폴트값이 False

credit=read.csv("credit.csv", stringsAsFactors = TRUE)
head(credit)


summary(credit)
table(credit$checking_balance) #빈도수를 제대로 보려고
table(credit$savings_balance)
summary(credit$savings_balance) #카테고리형 변수면 summary=table 

summary(credit$months_loan_duration)
summary(credit$amount)

#y는 default 임
summary(credit$default)


#데이터의 행순서를 한번 섞어서 데이터 쪼개기
set.seed(12345)
credit_rand=credit[order(runif(1000)),]
credit_rand

#확인
head(credit$amount)
head(credit_rand$amount)


#데이터 쪼개기
credit_train=credit_rand[1:900,]
credit_test=credit_rand[911:1000,]
table(credit_train$default)
table(credit_test$default)



library(rpart)
model <- rpart(default~., train) 
summary(model)




#예측 
credit_tree_pred= predict(credit_tree_prun, credit_test, type="class") #타입 설정해줘야됨
CrossTable( credit_tree_pred,credit_test$default)




