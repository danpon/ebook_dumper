import os
import time
import pyscreenshot
from pynput.mouse import Button, Controller


book_name = "CAP"
#nb_pages = 5
nb_pages = 435

scrnshot_x_1 = 48
scrnshot_y_1 = 98
scrnshot_x_2 = 1918
scrnshot_y_2 = 1035
next_page_x = 1795
next_page_y = 611


mouse = Controller()

# Click the left button
mouse.click(Button.left, 1)

os.mkdir(book_name)

print("Start and wait 3s...")
time.sleep(3) # Sleep for 3 seconds

for page in range(nb_pages):
    screenshot_name = book_name+"_00"+str(page)
    if page>9 and page <100 :
        screenshot_name = book_name+"_0"+str(page)
    elif page > 99 :
        screenshot_name = book_name+"_"+str(page)
    print(screenshot_name)    
    image = pyscreenshot.grab(bbox=(scrnshot_x_1, scrnshot_y_1, scrnshot_x_2, scrnshot_y_2))
    image.save("./"+book_name+"/"+screenshot_name+".png") 
    time.sleep(1)
    # Click the left button
    mouse.position = (next_page_x, next_page_y)
    mouse.click(Button.left, 1)

print("End.")