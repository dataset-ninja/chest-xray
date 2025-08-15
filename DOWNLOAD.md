Dataset **Chest Xray Masks and Labels** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/remote/eyJsaW5rIjogInMzOi8vc3VwZXJ2aXNlbHktZGF0YXNldHMvMTU1OF9DaGVzdCBYcmF5IE1hc2tzIGFuZCBMYWJlbHMvY2hlc3QteHJheS1tYXNrcy1hbmQtbGFiZWxzLURhdGFzZXROaW5qYS50YXIiLCAic2lnIjogIk5PYWZRSUVXOTYvS1N5VURpMkVublNEdDE1dGJuaEF4R2hxVG1ONC9GL2M9In0=?response-content-disposition=attachment%3B%20filename%3D%22chest-xray-masks-and-labels-DatasetNinja.tar%22)

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