%By: Bruno Filipe Oliveira Aguiar, N.Mec.: 80177
%    Jose' Pedro Domingues, N.Mec.: 80075



n = 2;
k = 2;
p = logspace(-3,log10(1/2),100)

f = factorial(n)./(factorial(k).*factorial(n-k)).*p.^k.*(1-p).^(n-k)

k2 = 3;
k3 = 4;
n  = 4;


f2 = factorial(n)./(factorial(k2).*factorial(n-k2)).*p.^k2.*(1-p).^(n-k2)
f3 = factorial(n)./(factorial(k3).*factorial(n-k3)).*p.^k3.*(1-p).^(n-k3)

ff = f2 + f3


figure(1)
plot(p,f,p,ff)
legend('2 motores','4 motores')
figure(2)
loglog(p,f,p,ff)
legend('2 motores','4 motores')

%Para pequenas distancias preferiamos o de 4 motores pois apresenta menor probabilidade de caiar,
%Mas para disntancias maiores preferiamos os de 2 motor pelas mesmas razoes.