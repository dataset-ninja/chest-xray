Dataset **Chest Xray Masks and Labels** can be downloaded in Supervisely format:

 [Download](https://assets.supervise.ly/supervisely-supervisely-assets-public/teams_storage/Q/9/N4/xiLyeuZ1oY94yQUjjm7fznhqWTbMl9x3BYoynDqdUeEA42YoQlxpKPIKhL02BMcKOHMFAmOjnTS9r8aRtuO7Nu5vwKXTiZpcTgDiizCAT31dJJQdMjtvAK0HdgZO.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='Chest Xray Masks and Labels', dst_path='~/dtools/datasets/Chest Xray Masks and Labels.tar')
```
The data in original format can be 🔗[downloaded here.](https://www.kaggle.com/datasets/nikhilpandey360/chest-xray-masks-and-labels/download?datasetVersionNumber=1)