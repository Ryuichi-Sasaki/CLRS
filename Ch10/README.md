# 10.1-1
\_は要素が存在しないことを表す。  
(x)はxがtopに位置する要素であることを表す。  
S = [_ _ _ _ _ _]  
S = [(4) _ _ _ _ _]  
S = [4 (1) _ _ _ _]  
S = [4 1 (3) _ _ _]  
S = [4 (1) 3 _ _ _]  
S = [4 1 (8) _ _ _]  
S = [4 (1) 8 _ _ _]

# 10.1-3
\_は要素が存在しないことを表す。  
()はheadの位置を表す。  
!はtailの位置を表す。  
Q = [! _ _ _ _ _]  
Q = [(4) ! _ _ _ _]  
Q = [(4) 1 ! _ _ _]  
Q = [(4) 1 3 ! _ _]  
Q = [4 (1) 3 ! _ _]  
Q = [4 (1) 3 8 ! _]  
Q = [4 1 (3) 8 ! _]  

# 10.1-4
[fixed_queue.py](./src/fixed_queue.py)に書いた。

# 10.1-5
[fixed_double_ended_queue.py](./src/fixed_double_ended_queue.py)に書いた。

# 10.2-1
insertはO(1)で実行できる。  
一方向リストの先頭に要素を追加すればよい。  
deleteはO(1)で実行できない。  
prevポインタを定数時間で取得できないため。

# 10.2-2
[singly_linked_list_stack.py](./src/singly_linked_list_stack.py)に書いた。

# 10.2-4
L.nil.key = kとする。

# 10.2-5
[singly_circular_list_dictionary.py](./src/singly_circular_list_dictionary.py)に書いた。

# 10.2-6
集合を一方向リストで表現し、先頭要素へのポインタのheadと最終要素へのポインタのtailを持たせる。  
unionではS1のtailが指す要素のnextをS2のheadに繋ぎ変え、S1のtailにS2のtailを代入する。こうすれば、S1がS1 ∪ S2となる。

# 10.4-1
ノートに描いた。8要素の木となる。

# 10.4-2
[print_binary_tree.py](./src/print_binary_tree.py)に書いた。

# 10.4-3
[print_binary_tree.py](./src/print_binary_tree.py)に書いた。

# 10.4-4
10.4-2, 10.4-3と同じ手続きでOKだと思う。
