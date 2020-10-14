# Detect Hook, Helmet, Head
## 1. labels
- Hook: Safty Hook
- Helmet : Helmet on
- Head : Helmet off

## 2. Download Image Files

> Folders
>
> ----data-preprocessed
>
> ​	 ---- hook_helmet
>
> ​				---- images
>
> ​						---- train
>
> ​						----valid
>
> ​				---- labels
>
> ​						---- train
>
> ​						----valid

## 3. Run Inference
- install packages
```
pip install -qr '../requirements.txt'  # install dependencies
```
- Inference
> Parameters 

<'location of detect.py file'>

--source <'location of image/ video/folder to predict'>

--weight <'location of the saved best weights'>

--output <'location of output files after prediction'>

> example (photo)


```
python detect.py --source data-preprocessed/hook_helmet/images/valid/ --weights 'codes/runs/exp3_HookHelmet/weights/best_HookHelmet.pt' --output 'codes/inference/output'

```

## Checkout 'codes/inference/output'!

## Done!



<br>

<br>

# Data pre-process files

- codes/mp42jpgs.py

> convert mp4 file to jpg files

example:

```
python codes/mp42jpgs.py --videopath add.mp4 --output train/
```

