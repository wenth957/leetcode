from Stack import Stack


st = Stack()
s = input("please enter a order serial: ")  # 顾客取盘子的序列
washed_index = 0
geted_index = 0
while geted_index < 10 and washed_index < 10:
    # 洗盘子
    k = int(s[geted_index])
    if washed_index <= k:
        '''将要取的盘子之前的所有编号放入栈中'''
        for m in range(washed_index, k + 1):
            st.push(m)
        washed_index = k + 1
    while not st.isEmpty() and st.peek() == int(s[geted_index]):
        '''取出盘子时必须反转顺序：其他顺序不出栈'''
        m = st.pop()
        geted_index += 1
if st.isEmpty():
    '''如果栈中还有元素，说明取的序列不对'''
    print("YES!")
elif not st.isEmpty():
    print("NO!")
