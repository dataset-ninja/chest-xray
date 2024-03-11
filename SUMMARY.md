**Chest Xray Masks and Labels** is a dataset for instance segmentation, semantic segmentation, and object detection tasks. It is used in the medical industry. 

The dataset consists of 896 images with 1627 labeled objects belonging to 2 different classes including *healthy lung* and *tuberculosis lung*.

Images in the Chest Xray Masks and Labels dataset have pixel-level instance segmentation annotations. Due to the nature of the instance segmentation task, it can be automatically transformed into a semantic segmentation (only one mask for every class) or object detection (bounding boxes for every object) tasks. There are 192 (21% of the total) unlabeled images (i.e. without annotations). There are 2 splits in the dataset: *CXRpng-train* (800 images) and *test* (96 images). Alternatively, the dataset could be split into 2 origins of data: ***Shenzhen*** (662 images) and ***Montgomery County*** (138 images). Additionaly, every image has <span style="background-color: #ecdefc; padding: 2px 4px; border-radius: 4px;">info</span> with text medical recordings. The dataset was released in 2019 by the <span style="font-weight: 600; color: grey; border-bottom: 1px dashed #d3d3d3;">National Institutes of Health, USA</span>, <span style="font-weight: 600; color: grey; border-bottom: 1px dashed #d3d3d3;">The Chinese University of Hong Kong, China</span>, and <span style="font-weight: 600; color: grey; border-bottom: 1px dashed #d3d3d3;">The Shenzhen No. 3 People's Hospital, China</span>.

Here is the visualized example grid with animated annotations:

[animated grid](https://github.com/dataset-ninja/chest-xray/raw/main/visualizations/horizontal_grid.webm)
