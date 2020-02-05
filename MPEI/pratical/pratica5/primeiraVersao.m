
nStrings   =  1000;
m          =  round(1000 / 0.8);
letras     =  ['a':'z' 'A':'Z'];
contador   =  zeros(1, m);
for i = 1 : nStrings

  chaveGerada        =  geradorChave(3, 20, letras);
  valorHash          =  string2hash(chaveGerada);
  pos                =  mod(valorHash, m) + 1;
  contador(pos)      =  contador(pos) + 1;
  if rem(i, 10) == 0
  
    subplot(121)
    bar(contador)
    drawnow
    subplot(122)
    hist(contador, 0:9)
    drawnow
    

    end

end

var(contador)
median(contador)

