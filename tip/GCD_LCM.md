#GCD & LCM

## GCD 최대 공약수, LCM 최소 공배수
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
