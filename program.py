def base10binaire (n):
  nbin = ''
  while n!=0:
    n=n//2
    print (n,n%2)
    nbin = str(n%2) + nbin
## print (nbin)
  
def fact10to2 (n):
  nBin = ''
    for i in range (150):
      d = n*2
      if d>=1:
        d=d-1
        bit = '1'
      else:
        bit = '0'
      n=d
      nBin = nBin +bit
      print (bit,nBin,n,d)
    return
## print(fact10to2(0.12251))
  

def signe (n):
  if n>=0:
    return '0'
  else:
    return '1'
## print (signe(-87))
