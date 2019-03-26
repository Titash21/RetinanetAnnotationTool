import json
import os
import cv2
from collections import OrderedDict


def resize_images(input_folder):
    ref = [file for file in os.listdir(input_folder) if file.endswith(".jpg")]
    count = 0
    for image in ref:
        print("reading image ",image,end=" ")
        imageRead = cv2.imread(input_folder+image,0)
        image_resize = cv2.resize(imageRead,(600,800))
        print("resized image")
        count+=1
        cv2.imwrite(input_folder+"signature-"+str(count)+'.jpg',image_resize)




def create_csv_image():
    print("HELLO")
    '''
    / data / imgs / img_001.jpg, 837, 346, 981, 456, cow
    / data / imgs / img_002.jpg, 215, 312, 279, 391, cat
    / data / imgs / img_002.jpg, 22, 5, 89, 84, bird
    / data / imgs / img_003.jpg,, , , ,
    '''
    input_files_txt = [file for file in os.listdir("./Labels/005/") if file.endswith("_other_.txt")]
    for file in input_files_txt:
            image_name = file.split("_")[0]+".jpg"
            print("INPUT->", file, image_name, end=" ")
            imageRead = cv2.imread("./Images/005/" +image_name ,0)
            with open("./Labels/005/" + file) as inputfile , open("retinanet_signature.csv","a") as training_data:

                lists = inputfile.readlines()
                if(len(lists)>1):
                    for i,item in enumerate(lists[1:]):
                        print(item, end=" , ")
                        coordinates = item.split(" ")
                        x1, y1,x2, y2 = coordinates[0],coordinates[1],coordinates[2],coordinates[3].strip()
                        imageRead = cv2.rectangle(imageRead, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
                        string = image_name+","+ x1+","+y1+","+x2+","+y2+","+"other"+"\n"
                        training_data.write(string)
                    cv2.imwrite("./Labels/output/005/" +image_name, imageRead)
                else:
                    print(file, image_name , end=" ")
                    print(lists,end=" ")
                    string = image_name + ","  + "," + "," + "," + "," + "\n"
                    print(string)
                    training_data.write(string)

# create_csv_image()
# resize_images("./Images/005/")
# create_annotation("./Labels/005/")
import pandas as pd
import numpy as np
def create_train_test_splits(input_path,csv_name):
    csv_read = pd.read_csv(input_path+csv_name)
    mask = np.random.rand(len(csv_read)) < 0.8
    test = csv_read[~mask]
    train = csv_read[mask]
    test.to_csv(input_path+"test_retinatnet.csv")
    train.to_csv(input_path+"train_retinanet.csv")

create_train_test_splits("","retinanet_signature.csv")