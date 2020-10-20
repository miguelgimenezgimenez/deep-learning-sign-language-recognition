import cv2
import glob


images = [
    *glob.glob("data/kerry/**/*.jpeg"),
]

for img_path in images:
  print(img_path)
  img = cv2.imread(img_path)
  # img_rotate_180 = cv2.rotate(img, cv2.ROTATE_180)
  flipHorizontal = cv2.flip(img, 1)
  print(flipHorizontal)
  cv2.imwrite(img_path, flipHorizontal)
  # True
