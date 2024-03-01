from functools import*
@cache
def w(a,b,c):
 if a<1 or b<1 or c<1:return 1
 if a>20 or b>20 or c>20:return w(20,20,20)
 if a<b<c:return w(a,b,c-1)+w(a,b-1,c-1)-w(a, b-1,c)
 return w(a-1,b,c)+w(a-1,b-1,c)+w(a-1,b,c-1)-w(a-1,b-1,c-1)

st=open(0)
input=lambda:st.readline().rstrip()

while 1:
 a,b,c=map(int,input().rsplit())
 if a==b==c==-1:break
 print(f"w({a}, {b}, {c}) = {w(a,b,c)}")
