# 2.1-1
[31, 41, 59, 26, 41, 58]

[31, 41, 59, 26, 41, 58]

[31, 41, 59, 26, 41, 58]

[26, 31, 41, 59, 41, 58]

[26, 31, 41, 41, 59, 58]

[26, 31, 41, 41, 58, 59]

元々右側にあった41はソート後も右側に位置する。

# 2.1-2
[insertion_sort_desc.py](./src/insertion_sort_desc.py)に書いた。

# 2.1-3
[linear_search.py](./src/linear_search.py)に書いた。

# 2.1-4
[add_two_binary_numbers.py](./src/add_two_binary_numbers.py)に書いた。

# 2.2-1
Θ(n^3)

# 2.2-2
[selection_sort.py](./src/selection_sort.py)に書いた。

# 2.2-3
### 平均
n/2 個 : Θ(n)

### 最悪
n 個 : Θ(n)

# 2.2-4
思いつかなかった。

# 2.3-1
[3, 9, 26, 38, 41, 49, 52, 57]

[3, 26, 41, 52], [9, 38, 49, 57]

[3, 41], [26, 52], [38, 57], [9, 49]

[3], [41], [52], [26], [38], [57], [9], [49]

# 2.3-2
[merge_sort_without_sentinel.py](./src/merge_sort_without_sentinel.py)に書いた。

# 2.3-3
[基底]  
n = 2のとき nlgn = 2lg2 = 2 となり成立。

[帰納]  
n = 2^k (>1) のとき、T(2^k) = 2^klg2^kが成り立つと仮定し、 T(2^(k+1)) = 2^(k+1)lg2^(k+1)が成り立つことを示す。

T(2^(k+1))  
= 2T(2^(k+1)/2) + 2^(k+1)  
= 2T(2^k) + 2⋅2^k  
= 2⋅2^klg2^k + 2⋅2^k  
= 2⋅2^k(lg2^k + 1)  
= 2⋅2^k(lg2^k + lg2)  
= 2^(k+1)⋅lg2^(k+1)

# 2.3-4
[insertion_sort_recur.py](./src/insertion_sort_recur.py)に書いた。

# 2.3-5
[binary_search.py](./src/binary_search.py)に書いた。

# 2.3-6
Θ(nlgn)にはできない。  
挿入場所の探索はΘ(lgn)で実施できるようになるが、要素の移動はΘ(n)のままとなる。  
最悪実行時間は変わらずΘ(n^2)である。

# 2.3-7
[has_pair_of_sum_is_v.py](./src/has_pair_of_sum_is_v.py)に書いた。