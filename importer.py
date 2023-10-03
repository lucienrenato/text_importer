import tkinter as tk
from pynput import keyboard

def on_press(key):
    if key == keyboard.Key.f8:
        text = text_entry.get("1.0", "end-1c")  # 获取输入框中的文本，去除末尾的换行符
        keyboard.Controller().type(text)  # 模拟键盘输出

def simulate_typing():
    text = text_entry.get("1.0", "end-1c")  # 获取输入框中的文本，去除末尾的换行符
    keyboard.Controller().type(text)  # 模拟键盘输出

root = tk.Tk()
root.title("键盘模拟器")

# 创建文本输入框
text_entry = tk.Text(root, height=5, width=30)
text_entry.pack()

# 创建按钮
button = tk.Button(root, text="输入", command=simulate_typing)
button.pack()

# 监听键盘事件
listener = keyboard.Listener(on_press=on_press)
listener.start()

root.mainloop()