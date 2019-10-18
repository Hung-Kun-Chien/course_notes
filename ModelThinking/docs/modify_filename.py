from glob import glob
import shutil

for fn in glob("*.pdf"):
    if fn.startswith("_"):
        src = fn
        dst = "_".join(fn.split("_")[2:])
        print("dst={}".format(dst))
        shutil.move(src, dst)
