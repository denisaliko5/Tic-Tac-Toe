def main():
  ##IMPORTATION
  import turtle
  import math

  ##VARIABLES
  #Turtle & Apparence
  s = turtle.Screen()
  t = turtle.Turtle()
  x = turtle.Turtle()
  o = turtle.Turtle()
  st = turtle.Turtle()
  w = turtle.Turtle()
  t.ht()
  x.ht()
  o.ht()
  st.ht()
  w.ht()
  #Color
  s.bgcolor("black")
  t.color("white")
  x.color("hotpink")
  o.color("turquoise")
  st.color("red")
  w.color("red")
  #Speed
  t.speed(0)
  x.speed(0)
  o.speed(0)
  st.speed(10)
  w.speed(0)
  #Other Variables
  ang = 90
  dis = 175
  hypot1 = math.hypot(dis*2/3, dis*2/3)
  hypot2 = math.hypot(dis*2, dis*2)

  ##SCREEN SETUP
  #Web Creator
  def web_creator():
    t.penup()
    t.goto(-dis/3, -dis)
    t.pendown()
    t.lt(ang)
    t.fd(dis*2)

    t.penup()
    t.goto(dis/3, dis)
    t.pendown()
    t.bk(dis*2)

    t.penup()
    t.goto(-dis, dis/3)
    t.pendown()
    t.rt(ang)
    t.fd(dis*2)

    t.penup()
    t.goto(-dis, -dis/3)
    t.pendown()
    t.fd(dis*2)
  #X Drawer
  def draw_x(pos):
    if pos == 1:
      x.penup()
      x.goto(-dis, dis)
      x.pendown()
      x.rt(ang/2)
      x.fd(hypot1)
      x.penup()
      x.goto(-dis/3, dis)
      x.pendown()
      x.rt(ang)
      x.fd(hypot1)
      x.lt(ang*2-ang/2)
      x.penup()
      x.goto(0,0)
    elif pos == 2:
      x.penup()
      x.goto(-dis/3, dis)
      x.pendown()
      x.rt(ang/2)
      x.fd(hypot1)
      x.penup()
      x.goto(dis/3, dis)
      x.pendown()
      x.rt(ang)
      x.fd(hypot1)
      x.lt(ang*2-ang/2)
      x.penup()
      x.goto(0,0)  
    elif pos == 3:
      x.penup()
      x.goto(dis/3, dis)
      x.pendown()
      x.rt(ang/2)
      x.fd(hypot1)
      x.penup()
      x.goto(dis, dis)
      x.pendown()
      x.rt(ang)
      x.fd(hypot1)
      x.lt(ang*2-ang/2)
      x.penup()
      x.goto(0,0)
    elif pos == 4:
      x.penup()
      x.goto(-dis, dis/3)
      x.pendown()
      x.rt(ang/2)
      x.fd(hypot1)
      x.penup()
      x.goto(-dis/3, dis/3)
      x.pendown()
      x.rt(ang)
      x.fd(hypot1)
      x.lt(ang*2-ang/2)
      x.penup()
      x.goto(0,0)
    elif pos == 5:
      x.penup()
      x.goto(-dis/3, dis/3)
      x.pendown()
      x.rt(ang/2)
      x.fd(hypot1)
      x.penup()
      x.goto(dis/3, dis/3)
      x.pendown()
      x.rt(ang)
      x.fd(hypot1)
      x.lt(ang*2-ang/2)
      x.penup()
      x.goto(0,0)  
    elif pos == 6:
      x.penup()
      x.goto(dis/3, dis/3)
      x.pendown()
      x.rt(ang/2)
      x.fd(hypot1)
      x.penup()
      x.goto(dis, dis/3)
      x.pendown()
      x.rt(ang)
      x.fd(hypot1)
      x.lt(ang*2-ang/2)
      x.penup()
      x.goto(0,0)
    elif pos == 7:
      x.penup()
      x.goto(-dis, -dis/3)
      x.pendown()
      x.rt(ang/2)
      x.fd(hypot1)
      x.penup()
      x.goto(-dis/3, -dis/3)
      x.pendown()
      x.rt(ang)
      x.fd(hypot1)
      x.lt(ang*2-ang/2)
      x.penup()
      x.goto(0,0)
    elif pos == 8:
      x.penup()
      x.goto(-dis/3, -dis/3)
      x.pendown()
      x.rt(ang/2)
      x.fd(hypot1)
      x.penup()
      x.goto(dis/3, -dis/3)
      x.pendown()
      x.rt(ang)
      x.fd(hypot1)
      x.lt(ang*2-ang/2)
      x.penup()
      x.goto(0,0)  
    elif pos == 9:
      x.penup()
      x.goto(dis/3, -dis/3)
      x.pendown()
      x.rt(ang/2)
      x.fd(hypot1)
      x.penup()
      x.goto(dis, -dis/3)
      x.pendown()
      x.rt(ang)
      x.fd(hypot1)
      x.lt(ang*2-ang/2)
      x.penup()
      x.goto(0,0)
  #O Drawer
  def draw_o(pos):
    if pos == 1:
      o.penup()
      o.goto(-dis*2/3, dis/3)
      o.pendown()
      o.circle(dis/3)
    elif pos == 2:
      o.penup()
      o.goto(0, dis/3)
      o.pendown()
      o.circle(dis/3)
    elif pos == 3:
      o.penup()
      o.goto(dis*2/3, dis/3)
      o.pendown()
      o.circle(dis/3)
    elif pos == 4:
      o.penup()
      o.goto(-dis*2/3, -dis/3)
      o.pendown()
      o.circle(dis/3)
    elif pos == 5:
      o.penup()
      o.goto(0, -dis/3)
      o.pendown()
      o.circle(dis/3)
    elif pos == 6:
      o.penup()
      o.goto(dis*2/3, -dis/3)
      o.pendown()
      o.circle(dis/3)
    elif pos == 7:
      o.penup()
      o.goto(-dis*2/3, -dis)
      o.pendown()
      o.circle(dis/3)
    elif pos == 8:
      o.penup()
      o.goto(0, -dis)
      o.pendown()
      o.circle(dis/3)
    elif pos == 9:
      o.penup()
      o.goto(dis*2/3, -dis)
      o.pendown()
      o.circle(dis/3)
  #XO Result Drawer
  def result_xo(res):
    t.clear()
    x.clear()
    o.clear()
    st.clear()
    def draw_x_win():
      x.penup()
      x.goto(-dis/3, dis/3)
      x.pendown()
      x.rt(ang/2)
      x.fd(hypot1)
      x.penup()
      x.goto(dis/3, dis/3)
      x.pendown()
      x.rt(ang)
      x.fd(hypot1)
      w.penup()
      w.goto((-dis/3)-35, -dis/3-hypot1/2+20)
      w.pendown()
      w.write("WINNER!", font = ("Times New Roman", 36, "normal"))
    def draw_o_win():
      o.penup()
      o.goto(0, -dis/3)
      o.pendown()
      o.circle(dis/3)
      w.penup()
      w.goto((-dis/3)-35, -dis/3-hypot1/2+20)
      w.pendown()
      w.write("WINNER!", font = ("Times New Roman", 36, "normal"))
    def draw_xo_tie():
      x.penup()
      x.goto(-dis*2/3, dis/3)
      x.pendown()
      x.rt(ang/2)
      x.fd(hypot1)
      x.penup()
      x.goto(0, dis/3)
      x.pendown()
      x.rt(ang)
      x.fd(hypot1)
      o.penup()
      o.goto(dis/3, -dis/3)
      o.pendown()
      o.circle(dis/3)
      w.penup()
      w.goto(-dis/3-30, -dis/3-hypot1/2+20)
      w.pendown()
      w.write("DRAW!", font = ("Times New Roman", 36, "normal"))
    if res == "x_winner":
      draw_x_win()
    elif res == "o_winner":
      draw_o_win()
    elif res ==  "tie":
      draw_xo_tie()

  ##IMPLEMENTATION
  web_creator()
  pos_xo_list = ["", "", "", "", "", "", "", "", ""]
  def result_check_xo():
    pos_x_list = [0]*5
    pos_o_list = [0]*5
    for i in range(5):
      while True:
        try:
          pos_x_list[i] = int(input("Enter position of X: "))
          if pos_x_list[i] >= 1 and pos_x_list[i] <= 9 and pos_xo_list[pos_x_list[i]-1] == "":
            draw_x(pos_x_list[i])
            pos_xo_list[pos_x_list[i]-1] = "Faleminderit Erik!"
            break
          else:
            print("Invalid Input!")
        except ValueError:
          print("Invalid Input!")

      if ((1 in pos_x_list) and (2 in pos_x_list) and (3 in pos_x_list)):
        st.penup()
        st.goto(-dis, dis*2/3)
        st.pendown()
        st.fd(dis*2)
        print("Player 1 won!")
        result_xo("x_winner")
        break
      elif ((4 in pos_x_list) and (5 in pos_x_list) and (6 in pos_x_list)):
        st.penup()
        st.goto(-dis, 0)
        st.pendown()
        st.fd(dis*2)
        print("Player 1 won!")
        result_xo("x_winner")
        break
      elif ((7 in pos_x_list) and (8 in pos_x_list) and (9 in pos_x_list)):
        st.penup()
        st.goto(-dis, -dis*2/3)
        st.pendown()
        st.fd(dis*2)
        print("Player 1 won!")
        result_xo("x_winner")
        break
      elif ((1 in pos_x_list) and (4 in pos_x_list) and (7 in pos_x_list)):
        st.penup()
        st.goto(-dis*2/3, dis)
        st.pendown()
        st.rt(ang)
        st.fd(dis*2)
        print("Player 1 won!")
        result_xo("x_winner")
        break
      elif ((2 in pos_x_list) and (5 in pos_x_list) and (8 in pos_x_list)):
        st.penup()
        st.goto(0, dis)
        st.pendown()
        st.rt(ang)
        st.fd(dis)
        print("Player 1 won!")
        result_xo("x_winner")
        break
      elif ((3 in pos_x_list) and (6 in pos_x_list) and (9 in pos_x_list)):
        st.penup()
        st.goto(dis*2/3, dis)
        st.pendown()
        st.rt(ang)
        st.fd(dis*2)
        print("Player 1 won!")
        result_xo("x_winner")
        break
      elif ((1 in pos_x_list) and (5 in pos_x_list) and (9 in pos_x_list)):
        st.penup()
        st.goto(-dis, dis)
        st.pendown()
        st.rt(ang/2)
        st.fd(hypot2)
        print("Player 1 won!")
        result_xo("x_winner")
        break
      elif ((3 in pos_x_list) and (5 in pos_x_list) and (7 in pos_x_list)):
        st.penup()
        st.goto(dis, dis)
        st.pendown()
        st.rt(135)
        st.fd(hypot2)
        print("Player 1 won!")
        result_xo("x_winner")
        break
      elif ((1 in pos_x_list + pos_o_list) and (2 in pos_x_list + pos_o_list) and (3 in pos_x_list + pos_o_list) and (4 in pos_x_list + pos_o_list) and (5 in pos_x_list + pos_o_list) and (6 in pos_x_list + pos_o_list) and (7 in pos_x_list + pos_o_list) and (8 in pos_x_list + pos_o_list) and (9 in pos_x_list + pos_o_list)):
        print("Tie!")
        result_xo("tie")
        break
      while True:
        try:
          pos_o_list[i] = int(input("Enter position of O: "))
          if pos_o_list[i] >= 1 and pos_o_list[i] <= 9 and pos_xo_list[pos_o_list[i]-1] == "":
            draw_o(pos_o_list[i])
            pos_xo_list[pos_o_list[i]-1] = "Faleminderit Erik!"
            break
          else:
            print("Invalid Input!")
        except ValueError:
          print("Invalid Input!")

      if ((1 in pos_o_list) and (2 in pos_o_list) and (3 in pos_o_list)):
        st.penup()
        st.goto(-dis, dis*2/3)
        st.pendown()
        st.fd(dis*2)
        print("Player 2 won!")
        result_xo("o_winner")
        break
      elif ((4 in pos_o_list) and (5 in pos_o_list) and (6 in pos_o_list)):
        st.penup()
        st.goto(-dis, 0)
        st.pendown()
        st.fd(dis*2)
        print("Player 2 won!")
        result_xo("o_winner")
        break
      elif ((7 in pos_o_list) and (8 in pos_o_list) and (9 in pos_o_list)):
        st.penup()
        st.goto(-dis, -dis*2/3)
        st.pendown()
        st.fd(dis*2)
        print("Player 2 won!")
        result_xo("o_winner")
        break
      elif ((1 in pos_o_list) and (4 in pos_o_list) and (7 in pos_o_list)):
        st.penup()
        st.goto(-dis*2/3, dis)
        st.pendown()
        st.rt(ang)
        st.fd(dis*2)
        print("Player 2 won!")
        result_xo("o_winner")
        break
      elif ((2 in pos_o_list) and (5 in pos_o_list) and (8 in pos_o_list)):
        st.penup()
        st.goto(0, dis)
        st.pendown()
        st.rt(ang)
        st.fd(dis*2)
        print("Player 2 won!")
        result_xo("o_winner")
        break
      elif ((3 in pos_o_list) and (6 in pos_o_list) and (9 in pos_o_list)):
        st.penup()
        st.goto(dis*2/3, dis)
        st.pendown()
        st.rt(ang)
        st.fd(dis*2)
        print("Player 2 won!")
        result_xo("o_winner")
        break
      elif ((1 in pos_o_list) and (5 in pos_o_list) and (9 in pos_o_list)):
        st.penup()
        st.goto(-dis, dis)
        st.pendown()
        st.rt(ang/2)
        st.fd(hypot2)
        print("Player 2 won!")
        result_xo("o_winner")
        break
      elif ((3 in pos_o_list) and (5 in pos_o_list) and (7 in pos_o_list)):
        st.penup()
        st.goto(dis, dis)
        st.pendown()
        st.rt(135)
        st.fd(hypot2)
        print("Player 2 won!")
        result_xo("o_winner")
        break
      elif ((1 in pos_x_list + pos_o_list) and (2 in pos_x_list + pos_o_list) and (3 in pos_x_list + pos_o_list) and (4 in pos_x_list + pos_o_list) and (5 in pos_x_list + pos_o_list) and (6 in pos_x_list + pos_o_list) and (7 in pos_x_list + pos_o_list) and (8 in pos_x_list + pos_o_list) and (9 in pos_x_list + pos_o_list)):
        print("Tie!")
        result_xo("tie")
        break
  result_check_xo()

  restart = input("Would you like to restart? ")
  if restart.lower() == "yes":
    x.clear()
    o.clear()
    st.clear()
    w.clear()
    main()
main()