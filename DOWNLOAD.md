Dataset **Chest Xray Masks and Labels** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/remote/eyJsaW5rIjogImZzOi8vYXNzZXRzLzE1NThfQ2hlc3QgWHJheSBNYXNrcyBhbmQgTGFiZWxzL2NoZXN0LXhyYXktbWFza3MtYW5kLWxhYmVscy1EYXRhc2V0TmluamEudGFyIiwgInNpZyI6ICJ5ZzJ5bXF0NnpmdmM0cVhjUVFTWUErNWFReGk1a1ZxcHlBSnBud3UxR1VVPSJ9)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='Chest Xray Masks and Labels', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

The data in original format can be [downloaded here](https://www.kaggle.com/datasets/nikhilpandey360/chest-xray-masks-and-labels/download?datasetVersionNumber=1).