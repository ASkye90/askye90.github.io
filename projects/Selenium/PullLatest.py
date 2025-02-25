import os
import shutil

dir_path = "C:\\Users\\jenkins\\AppData\\Local\\Jenkins\\.jenkins\\SeleniumPractice\\reports\\"
copy_path = "\\"

copy_path = os.path.dirname(__file__) + copy_path

map = {}

# Collect all the file names
for filename in os.listdir(dir_path):
	map[os.path.getmtime(dir_path + filename)] = filename

# Copy only the last n files
keys = list(map.keys())
for key in keys[len(keys)-1:]:
	shutil.copy(dir_path + map[key],copy_path)


print(map[max(map)])

os.replace(copy_path + map[max(map)],copy_path + "latestReport.html")