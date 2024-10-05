import os
import pyautogui
import cv2
import os
import numpy as np
#import clipboard
def get_image_answer():
    # Define a list of coordinates and sizes for the regions
    regions = [
        #(809, 753, 56, 60),
        #(871, 753, 56, 60),
        #(929, 753, 56, 60),
        #(989, 753, 56, 60),
        #(1049, 753, 56, 60)
        #(811, 709, 56, 60),
        #(872, 709, 56, 60),
        #(931, 709, 56, 60),
        #(990, 709, 56, 60),
        #(1049, 709, 56, 60),
        ###########################
        (806, 737, 56, 60),
        (865, 737, 56, 60),
        (924, 737, 56, 60),
        (982, 737, 56, 60),
        (1042, 737, 56, 60)
    ]

    def capture_screenshots(regions):
        # Create a subfolder named "cropped" if it doesn't exist
        cropped_folder = "cropped"
        if not os.path.exists("cropped"):
            os.makedirs("cropped")
        else:
            # Delete any existing images or files in the folder
            for file in os.listdir(cropped_folder):
                file_path = os.path.join(cropped_folder, file)
                try:
                    if os.path.isfile(file_path):  # Check if it's a file
                        os.remove(file_path)  # Remove the file
                except Exception as e:
                    print(f"Error deleting {file_path}: {e}")
        for i, region in enumerate(regions):
            x, y, width, height = region
            # Take a screenshot of the specified region
            screenshot = pyautogui.screenshot(region=(x, y, width, height))
            #screenshot.save(f'C:/Users/Coder/Desktop/MoneyFarmV6/cropped/{i}.png')
            root_folder = os.path.dirname(os.path.abspath(__file__))
            # Define the path to save the screenshot
            screenshot_path = os.path.join(root_folder, 'cropped', f'{i}.png')
            screenshot.save(screenshot_path)
                        

    # Capture 5 screenshots of the specified areas
    capture_screenshots(regions)

    pyautogui.sleep(1)
    # Get the current script's directory (assuming this is the root folder)
    root_folder = os.path.dirname(os.path.abspath(__file__))

    # Define the relative path to the 'cropped' directory inside the root folder
    image_dir = os.path.join(root_folder, 'cropped')

    # Threshold value for filtering similar images
    threshold = 0.9

    # Dictionary to store image similarities
    similarities = {}

    # Iterate over all image pairs and calculate their structural similarity
    for i, img_file in enumerate(os.listdir(image_dir)):
        img_path = os.path.join(image_dir, img_file)
        if not os.path.isfile(img_path):
            continue
        img1 = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        for j in range(i+1, len(os.listdir(image_dir))):
            other_img_file = os.listdir(image_dir)[j]
            other_img_path = os.path.join(image_dir, other_img_file)
            if not os.path.isfile(other_img_path):
                continue
            img2 = cv2.imread(other_img_path, cv2.IMREAD_GRAYSCALE)
            similarity = cv2.matchTemplate(img1, img2, cv2.TM_CCOEFF_NORMED)[0][0]
            similarities[(img_path, other_img_path)] = similarity
            similarities[(other_img_path, img_path)] = similarity

    # Calculate the average similarity score for each image
    image_scores = {}
    for img_path in os.listdir(image_dir):
        img_path = os.path.join(image_dir, img_path)
        if not os.path.isfile(img_path):
            continue
        similar_scores = [v for k, v in similarities.items() if k[0] == img_path]
        avg_score = np.mean(similar_scores)
        image_scores[img_path] = avg_score

    # Find the image with the least similarity to other images
    min_score = min(image_scores.values())
    min_images = [k for k, v in image_scores.items() if v == min_score]
    if len(min_images) == 1:
        min_image_name = os.path.basename(min_images[0])
        print(f"Image {min_image_name} has the least similarity with an average score of {min_score}")
        #clipboard.copy(min_image_name)
        return min_image_name
    else:
        # If there are multiple images with the same minimum similarity score,
        # choose the image with the smallest file size as the least similar image
        min_size = float('inf')
        min_image = None
        for image in min_images:
            size = os.path.getsize(image)
            if size < min_size:
                min_size = size
                min_image = image
        min_image_name = os.path.basename(min_image)
        print(f"Image {min_image_name} has the least similarity with an average score of {min_score}")
        #clipboard.copy(min_image_name)
        return min_image_name

#Image Verification
def solve_image_skylom():
    print('start solve img')
    answer = get_image_answer()
    print(answer, "is less similar image in here")
    if answer == "0.png":
        pyautogui.click(835 ,759)
        print(answer,"Clicked...")
    elif answer == "1.png":
        pyautogui.click(885 ,759)
        print(answer,"Clicked...")
    elif answer == "2.png":
        pyautogui.click(955 ,759)
        print(answer,"Clicked...")
    elif answer == "3.png":
        pyautogui.click(1009 ,759)
        print(answer,"Clicked...")
    elif answer == "4.png":
        pyautogui.click(1070 ,759)
        print(answer,"Clicked...")       
    else:
        print("No image number found..",answer)
        pyautogui.click(835 ,759)

#get_image_answer()
