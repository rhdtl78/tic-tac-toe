from tkinter import *   # window programing을 위한 모듈

def checked(i) :        # <def>: 함수의 정의.
    if flag == True:    # 승패가 결정됬을 경우 아무 버튼을 누르면 종료
        quit()
    global player       # player를 전역변수로 선언.
    button = list[i]    # button 에 클릭된 버튼을 할당.

    if button["text"] != "     " :
        return          # Button의 내용이 빈칸이면 종료,

    button["text"] = player     # 클릭 된 버튼의 내용을 플레이어와 같게
    button["bg"] = "yellow"     # 버튼 배경을 플레이어의 색으로 변경
    whoIsWinner()
    if player == "X" :          # 현재 플레이어가 X이면
        player = "O"            # 다음 플레이어를 지정
        button["bg"] = "yellow" # 버튼의 배경색을 변경
    else :
        player = "X"
        button["bg"] = "lightgreen"

def whoIsWinner():
    # list 의 이차원 표현
    # 0  1  2
    # 3  4  5
    # 6  7  8

    # TO DO 버튼이 클릭 될 때 마다 승패 여부를 확인
    # 가로 일자 확인
    row = i // 3
    col = i % 3

    # 해당 row의 첫번째 col에 놓였을 경우
    _next = row * 3 + 1
    _nextnext = _next + 1
    if 0 <= _nextnext <= 2:
        if list[_next]["text"] == list[_nextnext]["text"] == list[row]["text"] != "     ":
            win()
    
    # 세로 일자 확인
    _next = col + 3
    _nextnext = _next + 3
    
    if 0 <= _nextnext <= 2: 
        if list[_next]["text"] == list[_nextnext]["text"] == list[col]["text"] != "     ":
            win()

    # 우-상향 확인
    if list[2]["text"] == list[4]["text"] == list[6]["text"] != "     ":
        win()

    # 좌-하향 확인
    if list[0]["text"] == list[4]["text"] == list[8]["text"] != "     ":
        win()


# 승리 창
def win() :
    global flag
    if flag == False :
        msg = Message(window, text = "Winer is " + player + "!")
        msg.grid(row = 3, column = 1)
    flag = True
    
       

window = Tk()   # 윈도우 객체
player = "X"    # 첫 플레이어.
global list     # button들을 담아둘 리스트.
list = []
flag = False    # 승패 확인용 bool

for i in range(9) :     # 9개의 버튼 생성
    b = Button(window, text="     ", command=lambda k=i: checked(k))    # 내용이 빈칸인 버튼을 b에 할당. 이벤트는 checked를 할당.
    b.grid(row=i//3, column=i%3)    # 생성된 버튼을 window에 배치
    list.append(b)  # 버튼을 list에 추가.

window.mainloop()   # 상기 내용을 반복


