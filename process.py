import glob, os

# Current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

print(current_dir)

current_dir = r"/Applications/Computer Science/Morgan_Sig_Net/YOLO-Annotation-Tool/Multi-Image-Train/"
print("Current path", current_dir)

# Directory where the data will reside, relative to 'darknet.exe'
#path_data = './NFPAdataset/'

# Percentage of images to be used for the test set
percentage_test = 10;

# Create and/or truncate train.txt and test.txt
file_train = open('train.txt', 'w')
file_test = open('test.txt', 'w')

# Populate train.txt and test.txt
counter = 1
index_test = round(100 / percentage_test)
# The glob module finds all the pathnames matching a specified pattern
# according to the rules used by the Unix shell, although results are returned in arbitrary order.
lists = glob.iglob(os.path.join(current_dir, "*.jpg"))
print(sorted(lists))
for pathAndFilename in glob.iglob(os.path.join(current_dir, "*.jpg")):
    print("pathfilename",pathAndFilename)
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))
    print(title,ext)

    if counter == index_test:
        counter = 1
        file_test.write(current_dir + "/" + title + '.jpg' + "\n")
    else:
        file_train.write(current_dir + "/" + title + '.jpg' + "\n")
        counter = counter + 1
