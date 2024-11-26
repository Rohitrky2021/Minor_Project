# Night Image Enhancement

This is an implementation of the paper:

**Unsupervised Night Image Enhancement: When Layer Decomposition Meets Light-Effects Suppression**  
*European Conference on Computer Vision (ECCV 2022)*  
Yeying Jin, Wenhan Yang and Robby T. Tan

## Prerequisites

Follow these steps to set up the environment:

```bash
git clone https://github.com/jinyeying/night-enhancement.git
cd night-enhancement/
conda create -n night python=3.7
conda activate night
conda install pytorch=1.10.2 torchvision torchaudio cudatoolkit=11.3 -c pytorch
python3 -m pip install -r requirements.txt
```

## Datasets

### Light-Effects Suppression on Night Data

1. **Light-effects Data**
   - [Dropbox] | [BaiduPan (code:self)]
   - Collected from Flickr and self-collected, with multiple light colors in various scenes
   - Related to CVPR 2021 paper: "Nighttime Visibility Enhancement by Increasing the Dynamic Range and Suppression of Light Effects"

2. **LED Data**
   - [Dropbox] | [BaiduPan (code:ledl)]
   - Captured images with dimmer light as reference images

3. **GTA5 Nighttime Fog**
   - [Dropbox] | [BaiduPan (code:67ml)]
   - Synthetic GTA5 nighttime fog data
   - Related to ECCV 2020 paper: "Nighttime Defogging Using High-Low Frequency Decomposition and Grayscale-Color Networks"

4. **Syn-light-effects**
   - [Dropbox] | [BaiduPan (code:synt)]
   - Synthetic light-effects data from ICCV 2017 paper
   - Generate using Matlab code: `glow_rendering_code/repro_ICCV2007_Fig5.m`

## Low-Light Enhancement

### Pre-trained Model

1. Download the pre-trained LOL model:
   - [Dropbox] | [BaiduPan (code:lol2)]
   - Place in `./results/LOL/model/`
2. Put test images in `./LOL/`

### Online Test
Try the online test: https://replicate.com/cjwbw/night-enhancement

### Low-light Enhancement Test

Run the test:
```python
python main.py
```

### Low-light Enhancement Training

#### Datasets
1. LOL dataset (BMVC 2018)
   - [Baiduyun (code:sdd0)] | [Google Drive]

2. LOL_Cap dataset (TIP 2021)
   - [Baiduyun (code:l9xm)] | [Google Drive]

Dataset Structure:
```
|-- LOL_Cap
    |-- trainA ## Low
    |-- trainB ## Normal
    |-- testA ## Low
    |-- testB ## Normal
```

#### Training
Train the model:
```bash
python main.py --train --train_DatasetPath ./dataset/LOL_Cap/ --pretrain_path ./pretrained_model/LOL_params_0900000.pt
```

#### Testing
Test the model:
```bash
python main.py --test --test_DatasetPath ./dataset/LOL_Cap/testA --output ./results/LOL/testA_output
```

## Citation
If you use this code or dataset, please cite the original paper:
```
@inproceedings{jin2022unsupervised,
  title={Unsupervised Night Image Enhancement: When Layer Decomposition Meets Light-Effects Suppression},
  author={Jin, Yeying and Yang, Wenhan and Tan, Robby T},
  booktitle={European Conference on Computer Vision},
  year={2022}
}
```
\

## Contact
Rohit Yadav (rohiykumaryadav499@gmail.com)