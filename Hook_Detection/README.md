# Detect Hook, Helmet, Head
## 1. labels
- Hook: Safty Hook
- Helmet : Helmet on
- Head : Helmet off

## 2. Run Inference
- install packages
```
pip install -qr 'codes/requirements.txt'  # install dependencies
```
- Inference
> Parameters 
 > <'location of detect.py file'>
 > --source <'location of image/ folder to predict'>
 > --weight <'location of the saved best weights'>
 > --output <'location of output files after prediction'>


```
python detect.py --source data-preprocessed/hook_helmet/images/valid/ --weights 'codes/runs/exp3_HookHelmet/weights/best_HookHelmet.pt' --output 'codes/inference/output'

```

## Checkout 'codes/inference/output'!
## Done!
