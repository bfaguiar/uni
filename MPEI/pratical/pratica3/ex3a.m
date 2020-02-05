
x = 0:4;

pX = [ 1/16, 1/4, 6/16, 1/4, 1/16 ]

Ex = sum(x.* pX);
Ex2= sum(x.1^2.*pX)
VARX= Ex2 - Ex^2