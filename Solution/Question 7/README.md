##  Question 7

###  7_1(a)

Let the  2-dimensional grid has sizes (L1, L2), I for the index

* Function converting coordinates in 2d grid to index (x1, x2) is a linear function: 

`Index(x1, x2) = x1 + L1*x2`


* Function converting index into coordinates in 2d grid

x2 = I // L1   (the quotient of I/L1)<br/>
x1 = I % L1    (the remainder of I/L1)


###  7_1(b)

Let the d-dimensional grid has sizes (L1, L2 ... Ln), I for the index

* Function converting coordinates in d-dimensional grid to index (x1, x2, ... xn) is a linear function: 

`I(x1, x2) = f1*x1 + f2*x2 + ... + fn*xn`

where f1=1, f2=L1, f3=L1 * L2, f4=L1 * L2 * L3, ... fn=L1 * L2 * L3 * ... * Ln-1

That is, f1=1, f2=L1, f3=f2 * L2, f4=f3 * L3, ... fn=fn-1 * Ln-1


* Function converting index into coordinates in d-dimensional grid

xn = I // fn <br/>
xn-1 = (I % fn) // fn-1 <br/>
xn-2 = ((I % fn) % fn-1) // fn-2 <br/>
xn-3 = (((I % fn) % fn-1) % fn-2) // fn-3 <br/>

.
.
.

x1 = (...((I % fn) % fn-1) ... % f3 ) % f2

