# 12.1-1
ノートに描いた。

# 12.1-2
できない。  
根の次に小さい要素が、どの部分木に含まれるかを定数時間で知ることができない。

# 12.1-3
[binary_search_tree.py](./src/binary_search_tree.py)に書いた。

# 12.1-4
```
PREORDER-TREE-WALK(x)
  if x != NIL
    x.keyを印字する
    PREORDER-TREE-WALK(x.left)
    PREORDER-TREE-WALK(x.right)
```

```
POSTORDER-TREE-WALK(x)
  if x != NIL
    POSTORDER-TREE-WALK(x.left)
    POSTORDER-TREE-WALK(x.right)
    x.keyを印字する
```

# 12.2-1
c：911から左部分木に降りているので、後に912が現れることはない。  
e：347から右部分木に降りているので、後に299が現れることはない。

# 12.2-2
[binary_search_tree.py](./src/binary_search_tree.py)に書いた。

# 12.2-3
[binary_search_tree.py](./src/binary_search_tree.py)に書いた。

# 12.2-4
根が4である木から1を探索する。  
A = φ, B = {1, 2, 4}, C = {3}  
4 ∈ B > 3 ∈ C

# 12.2-5
2つの子をもつ節点をn、nの次節点をs、nの先行節点pとする。  
sが左の子cを持つとすると、n ≦ c ≦ sとなり、sがnの次節点であることに矛盾する。  
pが右の子dを持つとすると、p ≦ d ≦ nとなり、pがnの先行節点であることに矛盾する。

# 12.3-1
[binary_search_tree.py](./src/binary_search_tree.py)に書いた。
