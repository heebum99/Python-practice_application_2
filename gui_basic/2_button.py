from tkinter import *

root = Tk()
root.title("Nado GUI")  # GUI창 제목 설정

btn1 = Button(root, text="버튼1")  # (어디에 넣을지, 텍스트 내용)
btn1.pack()  # pack()을 해주지 않으면 위젯이 보이지 않음

# padx = 좌우 여백값, pady = 상하 여백값
btn2 = Button(root, padx=5, pady=10, text="버튼2")
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="버튼2")
btn3.pack()

# width, height = 위젯의 상하 좌우 크기를 결정하는 고정된 크기값
btn4 = Button(root, width=10, height=3, text="버튼4")
btn4.pack()

# fg = 글자색, bg = 배경색
btn5 = Button(root, fg="red", bg="yellow", text="버튼5")
btn5.pack()

# 이미지를 통한 버튼생성
photo = PhotoImage(file="gui_basic/img.png")
btn6 = Button(root, image=photo)
btn6.pack()


# 동작하는 버튼 생성
def btncmd():
    print("버튼이 클릭되었어요")


btn7 = Button(root, text="동작하는 버튼", command=btncmd)
btn7.pack()

root.mainloop()
