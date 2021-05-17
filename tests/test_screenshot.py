
# Program for partial screenshot
  
import pyscreenshot
import os
  
# im=pyscreenshot.grab(bbox=(x1,y1,x2,y2))
image = pyscreenshot.grab(bbox=(48, 98, 1918, 1035))
  
# To view the screenshot
#image.show()
  
# To save the screenshot
screenshot_name = "test_prt_scrn"
os.mkdir(screenshot_name);

image.save("./"+screenshot_name+"/"+screenshot_name+".png")