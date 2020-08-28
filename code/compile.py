import rd
import sys

args = sys.argv[1:]
model_root, fold, out_path = args
rd.create_images(model_root, fold, out_path)

print("done!")
