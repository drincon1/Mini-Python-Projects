import pyscreenshot
import datetime

def main():
    choice = int(input("Take a screenshot:\n(1) Whole screen\n(2) Just a piece\n"))
    if choice == 1:
        image = pyscreenshot.grab()
        
        image.show()
        
        image.save(f"{datetime.datetime.now()}.png")
    elif choice == 2:
        image = pyscreenshot.grab(bbox = (10,10,500,500))
        
        image.show()
        
        image.save(f"{datetime.datetime.now()}.png")        


if __name__ == '__main__':
    main()