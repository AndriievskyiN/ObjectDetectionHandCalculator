import cv2
import os
import time
from datetime import datetime
import uuid

def take_pictures(dir:str, n_pictures:int):
    '''
    -------------------------------
    Takes pictures of each target class
    -------------------------------
    Arguments:
        * dir (str): path to the data directory
        * n_pictures (int): number of images to take
    -------------------------------
    '''

    # Get class names from the data directory
    class_names = ["one", "two", "three", "four", "five", "plus", "minus"]

    cap = cv2.VideoCapture(0)

    sleep_time = 1
    print(f"Images for each class are now going to be collected. \nYou will have {sleep_time}s to change positions")

    # Loop through each class name
    for label in class_names:
        print(f"Taking pictures for class \"{label}\"... Please wait for 3 seconds")
        time.sleep(3)
        
        # Loop n_pictures amount of times
        for i in range(n_pictures):
            print(f"Collecting image: {i}")

            # Take pictures
            ret, frame = cap.read()

            # Create a unique identifier for the image
            img_id = str(uuid.uuid4())

            # Create the full path for the image
            img_path = os.path.join(dir, "train", label, f"{img_id}.jpeg")

            # Write image to a file
            cv2.imwrite(img_path, frame)
            
            if not cv2.imwrite(img_path, frame):
                raise Exception("Could not write image")

            time.sleep(sleep_time)
            
            # Break if "q" is clicked
            if cv2.waitKey(1) & 0xff == ord("q"):
                break
    
    # Release and destory all windows
    cap.release()
    cv2.destroyAllWindows()



