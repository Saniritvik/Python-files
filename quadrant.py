cord=[-1,-1]
# if cord[0] > 0 and cord[1] > 0:
#     print("Quadrant 1")
# elif cord[0] < 0 and cord[1] > 0:
#     print("Quadrant 2")
# elif cord[0] < 0 and cord[1] < 0:
#     print("Quadrant 3")
# elif cord[0] > 0 and cord[1] < 0:
#     print("Quadrant 4")
# else:
#     print("No quadrant")
if cord[0] > 0:
    if cord[1] >0:
        print("Q1")
    else:
        print("Q2")
else:
    if cord[1]>0:
        print("Q4")
    else:
        print("Q3")