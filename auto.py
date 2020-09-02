import pyautogui
import time

print("Enter The Number Of words You wanna spam : ")

num = int(input())

print("Enter The Phrase(s) You Want To spam : (Try to avoid Capital Letters !) ")

comments = []

for i in range(num):
    inp = input()
    comments.append(inp)

print("Now Take Your Cursor To The Point You Wanna Spam : (You Only Have 10sec) ")

time.sleep(10)

for i in range(1000):
    pyautogui.typewrite(comments[i % num])
    pyautogui.typewrite('\n')
    time.sleep(2)
