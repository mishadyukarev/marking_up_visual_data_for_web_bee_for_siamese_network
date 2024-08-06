# Marking up data app
With this app you can easily mark up data.
street_image_name,crop_name,target



```
street_image_name | crop_name        | target
image0.jpg        | image0_crop0.jpg | 1
image0.jpg        | image1_crop1.jpg | 0
image1.jpg        | image0_crop2.jpg | 1
```

## Notes
1. You need to check if your python version is the same as in '.python-version' file.
2. Activate your python environment ```$ conda activate base```.
3. Download frameworks from 'requirements.txt'.
4. Put images into ```app/data/images``` folder for marking up.
5. Naming pictures: ```image0.jpg, image1.png, image2.jpg, ...```
6. First stage is cropping images.
7. Second stage is marking up images with 1 or 0.
8. Don't take more than 10 pictures with advertising.
9. Please, record video during marking up data.

## Launching
```
$ cd app
$ python main.py
```

## Using
First stage:
1. Left mouse click - make a crop
2. Center mouse click - skip image

When image is cropped, and you see zoomed image:
1. Left mouse click - accept crop.
2. Right mouse click - reject crop.

Second stage:
1. Left mouse click - set 1 to target (has image on picture).
2. Right mouse click - set 0 to target (has not image on picture).


## Additional notes
1. You can skip second stage of marking up images, but you will have null in target.
2. You can see ```result.csv``` file in ```app/data/images``` during second stage.
