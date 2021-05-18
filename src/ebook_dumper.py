import os
import shutil
import threading
import time
import pyscreenshot
from pynput.mouse import Button, Controller




book_name = "CAP"
nb_pages = 435
page = 0

scrnshot_x_1 = 48
scrnshot_y_1 = 98
scrnshot_x_2 = 1918
scrnshot_y_2 = 1035
next_page_x = 1795
next_page_y = 611

mouse = Controller()

def take_screenshot():
    # here goes some long calculation
    if page==0:    
        time.sleep(5)
    else:
        time.sleep(3)
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


def main():

    global page
    
    try:
        shutil.rmtree(book_name)
    except OSError as e:
        print("Error: %s - %s." % (e.filename, e.strerror))
    
    os.mkdir(book_name)

    print("Start...")
    
    while page < nb_pages:        
        #start screen shot thread
        thread = threading.Thread(target=take_screenshot)
        thread.start()
        # wait here for the result to be available before continuing
        thread.join()
        #next page
        page+=1

    print("End.")

  
if __name__ == '__main__':
    main()