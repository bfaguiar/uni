%pertenceMembro(b,k,Teste{i});

function P = PertenceMembro(b,k,str)
   
  N = length(b);
  
  for i=1:K
    str = [str str2num(i)];
    index = hash(str);
    index = rem(index/N)+1;
  end
  1
P = (all(b(index))==1);

endfunction