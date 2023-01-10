from tkinter import *

root = Tk()
root.title("Nado GUI")  # GUI창 제목 설정
root.geometry("640x480+300+100")

# label => 글자나 이미지를 보여주는 용도
label1 = Label(root, text="안녕하세요")
label1.pack()

photo = PhotoImage(file="gui_basic/img.png")
label2 = Label(root, image=photo)
label2.pack()


# 버튼 클릭시 label1의 내용 변경
def change():
    label1.config(text="또 만나요")

    # photo2변수를 전역변수로 만들지 않으면 가비지컬렉션에 의해 값이 지워짐
    global photo2
    photo2 = PhotoImage(file="gui_basic/img2.png")
    label2.config(image=photo2)


btn = Button(root, text="클릭", command=change)
btn.pack()

root.mainloop()
