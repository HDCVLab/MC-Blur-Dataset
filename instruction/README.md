Download datasets from the google drive links. Your directory tree should look like this


## RHM subset
This subset consists of 87500 blurry images together with 87500 sharp images. The dataset is arranged in the structure as follows:
```
RHM subset (87500 blurry / 87500 sharp)
    |
    |--motion_avg
    |   |--Train
    |   |    |--blurry (70000 images)
    |   |    |--sharp  (70000 images)
    |   |--Test (250 fps images: 5000 500 fps images: 5000 1000 fps images: 7500)
    |        |--blurry (17500 images)      
    |        |--sharp  (17500 images)
```

### Visual some examples
1. Blurry images

![](../examples/Blurry_RHM.png)

2. Sharp images

![](../examples/Sharp_RHM.png)

## UHDM subet
This subset consists of 10000 pairs UHD blury and sharp images. The dataset is arranged in the structure as follows:
```
UHDM subset (10000 blurry / 10000 sharp)
    |
    |--Conv
    |   |--Train
    |   |    |--blurry (8000 images)
    |   |    |--sharp  (8000 images)
    |   |--Test
    |        |--blurry (2000 images)      
    |        |--sharp  (2000 images)
```
### Visual some examples
1. Blurry images

![](../examples/Blurry_UHDM.png)

2. Sharp images

![](../examples/Sharp_UHDM.png)
## LSDM subet

This subset consists of 22000 pairs blury and sharp images. The dataset is arranged in the structure as follows:
```
LSDM subset (22000 blurry / 22000 sharp)
    |
    |--defocus_crop
    |   |--Train
    |   |    |--blurry (18000 images)
    |   |    |--sharp  (18000 images)
    |   |--Test
    |        |--blurry (4400 images)      
    |        |--sharp  (4400 images)
```

**Note:**  LSD contains 4, 500 image pairs of sharp images and blurry images with the defocus effect in the training set, and 1,100 image pairs for testing.  For the convenience of training, we crop four patches without overlap from each images during the training and testing stages.

### Visual some examples
1. Blurry images

![](../examples/Blurry_LSD.png)

2. Sharp images

![](../examples/Sharp_LSD.png)
## RMBQ subset

This subset consists of 10000 real-world blurry images. The dataset is arranged in the structure as follows:
```
RMBQ subset (10000 blurry images )
    |
    |--real (10000 images)
```
### Visual some examples
Real-world blurry images

![](../examples/RMBQ.png)

