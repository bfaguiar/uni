p=0.4;
q=0.6;
T=[p^2 0 0 q^2;(1-p)^2 0 0 q*(1-q);p*(1-p) 0 0 q*(1-q); p*(1-p) 1 1 (1-q)^2]

x=[1 0 0 0]
(T^10)*x'