
# Program for partial screenshot
  
import pyscreenshot
  
# im=pyscreenshot.grab(bbox=(x1,y1,x2,y2))
image = pyscreenshot.grab(bbox=(48, 98, 1918, 1035))
  
# To view the screenshot
#image.show()
  
# To save the screenshot
image.save("GeeksforGeeks.png")