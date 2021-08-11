import cv2

img = cv2.imread("out.png")
GRID_SIZE = 8

height, width, channels = img.shape
height, width, channels = 8 * 8, 8 * 8, 3

window = "output"
cv2.namedWindow(window, cv2.WINDOW_NORMAL)
ims = cv2.resize(img, (height, width)) 

for x in range(0, width -1, GRID_SIZE):
     cv2.line(ims, (x, 0), (x, height), (255, 0, 0), 1, 1)
for y in range(0, height -1, GRID_SIZE):
     cv2.line(ims, (0, y), (width, y), (255, 0, 0), 1, 1)

cv2.imshow(window, ims)
while(1):
    k = cv2.waitKey(33)
    if k == 113:    # Q key to stop
        break
    elif k == -1:  # normally -1 returned,so don't print it
        continue
    else:
        print(k) # else print its value
