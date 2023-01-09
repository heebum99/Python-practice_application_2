from tkinter import *

root = Tk()
root.title("Nado GUI")  # GUI창 제목 설정

# root.geometry("640x480")  # GUI창 크기 설정: 가로 * 세로
# 가로 * 세로 + x좌표 + y좌표, 이때 x/y좌표는 화면 기준으로 GUI창을 띄우는 위치
root.geometry("640x480+300+100")

# x(너비), y(높이) 값 변경 불가 (GUI내에서 창 크기 변경 불가)
root.resizable(False, False)

root.mainloop()
