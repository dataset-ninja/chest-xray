Presented **Chest Xray Masks and Labels**  contains x-rays and corresponding masks. Some masks are missing so it is advised to cross-reference the images and masks. It is a modification of an [original dataset](https://www.kaggle.com/kmader/pulmonary-chest-xray-abnormalities/home) which consists of two public chest x-ray datasets.

The authors of the dataset address the significant global health concern posed by tuberculosis (TB) and the growing interest in developing computer-aided diagnostic systems for TB detection. They recognize that the progress in this field has been hindered by the scarcity of publicly available radiographs suitable for training machine learning algorithms for diagnostic systems. In response, the U.S. National Library of Medicine has released two datasets of postero-anterior (PA) chest radiographs, namely the Montgomery County (MC) set and the Shenzhen set, for research purposes. Both sets include clinical readings, and the MC set also offers manually segmented lung masks, enhancing the scope for evaluating automatic lung segmentation methods. These datasets were de-identified and exempted from institutional review board (IRB) review. Initial classification and lung segmentation results have been presented, serving as benchmarks for the research community.

The Montgomery County chest X-ray set (MC) was collected in collaboration with the Department of Health and Human Services in Maryland, USA. Comprising 138 frontal chest X-rays, this set includes both normal cases (80) and cases with TB manifestations (58). Captured using a stationary X-ray machine, the images are provided in 12-bit gray level PNG format, with the option of obtaining them in DICOM format. The image dimensions are either 4,020×4,892 or 4,892×4,020 pixels. Each reading contains patient information including age, gender, and observed lung abnormalities. Additionally, manual lung segmentations are available, created under radiologist supervision.

Here is the pattern of a typical medical reading:

```txt
Patient’s Sex: F
Patient’s Age: 031Y
cavitary nodular infiltrate in RUL; active TB
```

The Shenzhen chest X-ray set was gathered in collaboration with Shenzhen No.3 People's Hospital in China. This set comprises 662 frontal chest X-rays, encompassing normal cases (326) and cases with TB manifestations (336), including pediatric X-rays (AP). The X-rays were captured as part of routine outpatient clinic activities over a 1-month period using a Philips DR Digital Diagnost system. Provided in PNG format, these X-rays have an approximate size of 3K × 3K pixels. Each reading includes patient details and observed lung abnormalities.

Here is the pattern of a typical medical reading:

```txt
male 46yrs
bilateral PTB
```

Both sets contribute valuable resources to the research community, enabling the development and assessment of computer-aided diagnostic systems for TB detection.
