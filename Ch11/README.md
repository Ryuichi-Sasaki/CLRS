# 11.1-1
Tの後ろから前へと枠を調べ、NILでないものがあればそれが最大要素。O(m)。

# 11.1-2
search(B, k)はB[k]が1であればtrue、0であればfalseを返す。  
insert(B, k)はB[k] = 1。  
delete(B, k)はB[k] = 0。

# 11.2-2
h(k) = k mod 9  
K = {5 28 19 15 20 33 12 17 10}  
T = [NIL, NIL, NIL, NIL, NIL, NIL, NIL, NIL, NIL]  

K = {28 19 15 20 33 12 17 10}  
T = [NIL, NIL, NIL, NIL, NIL, (5), NIL, NIL, NIL]  

K = {19 15 20 33 12 17 10}  
T = [NIL, (28), NIL, NIL, NIL, (5), NIL, NIL, NIL]  

K = {15 20 33 12 17 10}  
T = [NIL, (19 28), NIL, NIL, NIL, (5), NIL, NIL, NIL]  

K = {20 33 12 17 10}  
T = [NIL, (19 28), NIL, NIL, NIL, (5), (15), NIL, NIL]  

K = {33 12 17 10}  
T = [NIL, (19 28), (20), NIL, NIL, (5), (15), NIL, NIL]  

K = {12 17 10}  
T = [NIL, (19 28), (20), NIL, NIL, (5), (33 15), NIL, NIL]  

K = {17 10}  
T = [NIL, (19 28), (20), (12), NIL, (5), (33 15), NIL, NIL]  

K = {10}  
T = [NIL, (19 28), (20), (12), NIL, (5), (33 15), NIL, (17)]  

K = {}  
T = [NIL, (10 19 28), (20), (12), NIL, (5), (33 15), NIL, (17)]  

# 11.2-3
操作対象のリストの長さをnとして  
成功する探索：Θ(1 + α/2) → Θ(1 + α/2)で変わらず  
失敗する探索：Θ(1 + α) → Θ(1 + α/2)で改善  
挿入：O(1) → Θ(1 + α/2)で悪化  
削除：O(1) → O(1)で変わらず

# 11.4-1
i = [0..m-1]  
m = 11  
K = {10, 22, 31, 4, 15, 28, 17, 88, 59}

### 線形探査法
h(k,i) = (h'(k) + i) mod m  
h'(k) = k  
[, , , , , , , , , , 10]  
[22, , , , , , , , , , 10]  
[22, , , , , , , , , 31, 10]  
[22, , , , 4, , , , , 31, 10]  
[22, , , , 4, 15, , , , 31, 10]  
[22, , , , 4, 15, 28, , , 31, 10]  
[22, , , , 4, 15, 28, 17, , 31, 10]  
[22, 88, , , 4, 15, 28, 17, , 31, 10]  
[22, 88, , , 4, 15, 28, 17, 59, 31, 10]

### 2次関数探査法
h(k,i) = (h'(k) + c1i + c2i^2) mod m  
h'(k) = k  
c1 = 1, c2 = 3  
[, , , , , , , , , , 10]  
[22, , , , , , , , , , 10]  
[22, , , , , , , , , 31, 10]  
[22, , , , 4, , , , , 31, 10]  
[22, , , , 4, , , , 15, 31, 10]  
[22, , , , 4, , 28, , 15, 31, 10]  
[22, , , 17, 4, , 28, , 15, 31, 10]  
[22, , 88, 17, 4, , 28, , 15, 31, 10]  
[22, , 88, 17, 4, , 28, 59, 15, 31, 10]  


### ダブルハッシュ法
h(k,i) = (h1(k) + ih2(k)) mod m  
h1(k) = k  
h2(k) = 1 + (k mod (m - 1))  
[, , , , , , , , , , 10]  
[22, , , , , , , , , , 10]  
[22, , , , , , , , , 31, 10]  
[22, , , , 4, , , , , 31, 10]  
[22, , , , 4, 15, , , , 31, 10]  
[22, , , , 4, 15, 28, , , 31, 10]  
[22, , , 17, 4, 15, 28, , , 31, 10]  
[22, , , 17, 4, 15, 28, 88, , 31, 10]  
[22, , 59, 17, 4, 15, 28, 88, , 31, 10]  

# 11.4-2
```
HASH-DELETE(T,k)
  i = HASH-SEARCH(T,k)
  T[i] = DELETED
```

HASH-INSERTは`if T[j] == NIL or T[j] == DELETED`とするだけ。