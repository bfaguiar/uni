N=10000;

m = 100

nn=2:m;

pp=0*nn;

for i=1:length(nn)  % de 2 a 100 pessoas

  n=nn(i);
  x=sort(floor(rand(n,N)*365)); % datas de nascimento de n pessoas
  y=x(1:end-1,:)==x(2:end,:); % Ver se pessoas tem mesma data de aniversario
  y=sum(y,1);                 % Soma por coluna do numero de vezes que existem duas pessoas com mesma data de aniversario
  pp(i)=sum(y>=1)/N;

end

plot(nn,pp);
