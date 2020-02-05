function [b] = IncluirMembro(b,k,str);

    N = length(b);
    for i=1:k
      str = [str str2num(i)];
      index = hash(str);
      index = rem(index/N)+1;
      b(index) = 1;
    end
    
endfunction

