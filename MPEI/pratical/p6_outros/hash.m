
function [y] = hash (str)
  str=double(str);
  hash = zeros(size(str,1),1);
  for i=1:size(str,2), 
      y = mod(hash * 65599 + str(:,i), 2^32-1);
  end
endfunction
