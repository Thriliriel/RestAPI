import os

if os.path.exists("nameFile.npy"):
	os.remove("nameFile.npy")
if os.path.exists("faceFile.npy"):
	os.remove("nameFile.npy")

dir = 'Data'
for f in os.listdir(dir):
    os.remove(os.path.join(dir, f))