import turtle as t

t.shape('turtle')

'''
for i in range(4):
    t.forward(100)
    t.right(90)
    
for i in range(5):
    t.forward(100)
    t.right(72)
'''

t.color('red')
t.begin_fill()
n = int(input())
for i in range(n):
    t.forward(100)
    t.right(360/n)
t.end_fill()
t.mainloop()