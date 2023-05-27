#!/usr/bin/env python
# coding: utf-8

# solution 1. 
# 
# 
# a.The range of X can be found from the PMF. The range of X consists of possible values for X. Here we have
#  RX={0.2,0.4,0.5,0.8,1}.
#  
# b.The event X≤0.5 can happen only if X is 0.2,0.4, or 0.5. 
#                     P(X≤0.5)=P(X∈{0.2,0.4,0.5})
#                      =P(X=0.2)+P(X=0.4)+P(X=0.5)
#                      	=PX(0.2)+PX(0.4)+PX(0.5)
#                         	=0.1+0.2+0.2=0.5
#                             
#                             
# c.Similarly, we have
#                     
#   P(0.25<X<0.75)=P(X∈{0.4,0.5})
#   	=P(X=0.4)+P(X=0.5)
#     =PX(0.4)+PX(0.5)
#     =0.2+0.2=0.4
# d.This is a conditional probability problem, so we can use our famous formula P(A|B)=P(A∩B)P(B). We have
# 
#    
# P(X=0.2|X<0.6)=P((X=0.2) and (X<0.6))P(X<0.6)
# =P(X=0.2)P(X<0.6)
# =PX(0.2)PX(0.2)+PX(0.4)+PX(0.5)
# =0.10.1+0.2+0.2=0.2
# 
# 

# solution 2
# 
# a.We have RX=RY={1,2,3,4,5,6}. Assuming the dice are fair, all values are equally likely so
# PX(k)={160for k=1,2,3,4,5,6 
# Similarly for Y
# ,
# PY(k)={160for k=1,2,3,4,5,6  
# 
# b. X and Y are independent random variables, we can write
# P(X=2,Y=6)
# =P(X=2)P(Y=6)
# =16⋅16=136
# .
# c.X  and Y are independent, knowing the value of Y does not impact the probabilities for X,
# P(X>3|Y=2)
# =P(X>3)
# =PX(4)+PX(5)+PX(6)
# =16+16+16=12
# 
# d.First, we have RZ={2,3,4,...,12}. Thus, we need to find PZ(k)for k=2,3,...,12. We have
#  PZ(2)
# =P(Z=2)=P(X=1,Y=1)
# =P(X=1)P(Y=1) (since X and Y are independent)
# =16⋅16=136
# ;
# PZ(3)
# =P(Z=3)=P(X=1,Y=2)+P(X=2,Y=1)
# =P(X=1)P(Y=2)+P(X=2)P(Y=1)
# =16⋅16+16⋅16=118
# ;
# PZ(4)=P(Z=4)=P(X=1,Y=3)+P(X=2,Y=2)+P(X=3,Y=1)
# =3⋅136=112.
# 
# 
# PZ(5)=436=19;
# PZ(6)=536;
# PZ(7)=636=16;
# PZ(8)=536;
# PZ(9)=436=19;
# PZ(10)=336=112;
# PZ(11)=236=118;
# PZ(12)=136.
# 
# It is always a good idea to check our answers by verifying that ∑z∈RZPZ(z)=1. Here, we have
# ∑z∈RZPZ(z)=136+236+336+436+536+636+536+436+336+236+136=1.
# 
# e.Note that here we cannot argue that Xand Z are independent. Indeed, Zseems to completely depend onX, Z=X+Y. 'to find the conditional probability P(X=4|Z=8), we use the formula for conditional probability
# P(X=4|Z=8)
# =P(X=4,Z=8)P(Z=8)
# =P(X=4,Y=4)P(Z=8)
# =P(X=4)P(Y=4)P(Z=8) (since X and Y are independent)
# 16⋅16536
# =15
# .

# solution 3.Let's define the random variable Y as the number of your correct answers to the 10questions you answer randomly. Then your total score will be X=Y+10. First, let's find the PMF of Y. For each question your success probability is 14.Hence, you perform 10independent Bernoulli(14)trials and Yis the number of successes. Thus, we conclude Y∼Binomial(10,14), so
# PY(y)={(10y)(14)y(34)10−y0  for y=0,1,2,3,...,10  otherwise
# 
# 
# Now we need to find the PMF of X=Y+10. First note that RX={10,11,12,...,20}. We can write
# PX(10)=P(X=10)=P(Y+10=10)
# =P(Y=0)=(10/0)(1/4)0(3/4)10−0=(3/4)10;
# PX(11)=P(X=11)=P(Y+10=11)
# =P(Y=1)=(10/1)(1/4)1(3/4)10−1=10(1/4)(3/4)9
# .
# 
# So, you get the idea. In general for k∈RX={10,11,12,...,20}
# ,
# PX(k)=P(X=k)=P(Y+10=k)
# =P(Y=k−10)=(k -10/10)(1/4)k−10(3/4)20−k
# .
# 
# To summarize,
# 
# PX(k)={(k−10/10)(1/4)k−10(3/4)20−k0 for k=10,11,12,...,20
# 
# In order to calculate P(X>15), we know we should consider y=6,7,8,9,10
# PY(y)={(10/y)(1/4)y(3/4)10−y/0   for y=6,7,8,9,10
# PX(k)={(10k−10)(14)k−10(34)20−k/0 for or k=16,17,...,20otherwise
# P(X>15)=PX(16)+PX(17)+PX(18)+PX(19)+PX(20)=(10/6)(1/4)6(3/4)4+(10/7)(1/4)7(3/4)3+(10/8)(1/4)8(3/4)2+(10/9)(1/4)9(3/4)1+(10/10)(1/4)10(3/4)/0.

# solution 4. We are looking at an interval of length 1.5 hours, so the number of customers in this interval is X∼Poisson(λ=1.5×10=15). Thus,
# P(10<X≤15)=∑15k=11PX(k)
# =∑15k=11e−1515/kk!
# =e−15[1511/11!+1512/12!+1513/13!+1514/14!+1515/15!]
# =0.4496

#  solution 5. we can solve it using the same methods. We will show that Z∼Pascal(m+l,p). To see this, consider a sequence of Hs and Ts that is the result of independent coin tosses with P(H)=p
# , (Figure 3.2). If we define the random variable X as the number of coin tosses until the m the heads is observed, then X∼Pascal(m,p)
# . Now, if we look at the rest of the sequence and count the number of heads until we observe l more heads, then the number of coin tosses in this part of the sequence is Y∼Pascal(l,p)
# . Looking from the beginning, we have repeatedly tossed the coin until we have observed m+l heads. Thus, we conclude the random variable Z
#  defined as Z=X+Y has a Pascal(m+l,p) distribution. 

# solution 6. here the random variable y is a function of the random variable x. this means that we perform the random experiment and obtain x 
# = x and then the value of y is determine as y = (x+1)2 since x is a random variable y is also a random variable.
# Rx = {-2,-1,0,1,2}
# 
# 
# RY={y=(x+1)2|x∈RX}
# ={0,1,4,9}
# 
# 
# 
# PY(0)=P(Y=0)=P((X+1)2=0)
# =P(X=−1)=1/8;
# PY(1)=P(Y=1)=P((X+1)2=1)
# =P((X=−2) or (X=0));
# PX(−2)+PX(0)=1/4+1/8=3/8;
# PY(4)=P(Y=4)=P((X+1)2=4)
# =P(X=1)=1/4;
# PY(9)=P(Y=9)=P((X+1)2=9)
# =P(X=2)=1/4.

# SOLUTION 8.According to the CLT, the sum of a large number of independent and identically distributed random variables will be approximately normally distributed, regardless of the distribution of the individual random variables.
# 
# Let's define Y as the sum of the men's weights on the ship:
# 
# Y = X1 + X2 + ... + X100
# 
# The mean of Y can be calculated as follows:
# 
# E(Y) = E(X1 + X2 + ... + X100) = E(X1) + E(X2) + ... + E(X100) = 100 * μ = 100 * 170 = 17,000
# 
# The variance of Y can be calculated as follows:
# 
# Var(Y) = Var(X1 + X2 + ... + X100) = Var(X1) + Var(X2) + ... + Var(X100) = 100 * σ^2 = 100 * 30^2 = 90,000
# 
# The standard deviation of Y is the square root of the variance:
# 
# σY = sqrt(Var(Y)) = sqrt(90,000) = 300
# 
# Now, we need to find the probability that Y exceeds 18,000. We can standardize Y using the Z-score:
# 
# Z = (Y - E(Y)) / σY = (18,000 - 17,000) / 300 = 1
# 
# To find the probability P(Y > 18,000), we can use the standard normal distribution table or a statistical software. The probability can be calculated as the complement of the cumulative distribution function (CDF) of the standard normal distribution at Z = 1:
# 
# P(Y > 18,000) = 1 - P(Z ≤ 1)
# 
# Using the standard normal distribution table or a statistical software, we find that P(Z ≤ 1) is approximately 0.8413.
# 
# Therefore, the probability that the men's total weight on the ship exceeds 18,000 is:
# 
# P(Y > 18,000) = 1 - P(Z ≤ 1) = 1 - 0.8413 ≈ 0.1587 or 15.87%.

# SOLUTION 9.To estimate P(4 ≤ Y ≤ 6) using the Central Limit Theorem, we can approximate the distribution of the sum Y = X1 + X2 + ... + X25 as a normal distribution.
# 
# Given that X1, X2, ..., X25 are independent and identically distributed, we can calculate the mean (μ) and the standard deviation (σ) of each Xi as follows:
# 
# μ = E(Xi) = (1 * 0.2 + 2 * 0.3 + 3 * 0.5) = 2.2
# σ = sqrt(Var(Xi)) = sqrt((1-μ)^2 * 0.2 + (2-μ)^2 * 0.3 + (3-μ)^2 * 0.5) = sqrt(0.64)
# 
# Now, let's calculate the mean (μY) and the standard deviation (σY) of the sum Y:
# 
# μY = n * μ = 25 * 2.2 = 55
# σY = sqrt(n) * σ = sqrt(25) * sqrt(0.64) = 5 * 0.8 = 4
# 
# To estimate P(4 ≤ Y ≤ 6), we can standardize the range by subtracting the mean (μY) and dividing by the standard deviation (σY):
# 
# Z1 = (4 - μY) / σY = (4 - 55) / 4 ≈ -12.75
# Z2 = (6 - μY) / σY = (6 - 55) / 4 ≈ -12.25
# 
# Using the standard normal distribution table or a statistical software, we can find the probabilities associated with the Z-scores:
# 
# P(Z1 ≤ Z ≤ Z2) = P(-12.75 ≤ Z ≤ -12.25)
# 
# Since the Z-scores are very large and negative, the probability P(Z1 ≤ Z ≤ Z2) will be extremely close to 0.
# 
# Therefore, using the Central Limit Theorem, we can estimate P(4 ≤ Y ≤ 6) to be very close to 0.

# In[ ]:




