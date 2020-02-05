
a = rand(11, 1e4) < 0.5;

A = sum(a(1:10,:)) == 10;

caras_11 = sum(a(11,A)==1);

p = caras_11 / sum(A)
