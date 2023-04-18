#GCD & LCM

## GCD 최대 공약수, LCM 최소 공배수
- 일반
```python
# GCD
for i in range(min(a,b),0,-1):
    if a%i ==0 and b%i ==0:
        print(i)
        break

# LCM
for i in range(max(a,b),(a*b)+1):
    if i%a == 0 and i%b == 0:
        print(i)
        break
```

- 유클리드 호제법 

```python
def GCD(x,y):
    while(y):
        x,y = y,x%y
    return x

def LCM(x,y):
    result = (x*y)//GCD(x,y)
    return li
```
