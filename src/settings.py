from typing import Dict, List, Optional, Union

from dataset_tools.templates import (
    AnnotationType,
    Category,
    CVTask,
    Domain,
    Industry,
    License,
    Research,
)

##################################
# * Before uploading to instance #
##################################
PROJECT_NAME: str = "Chest Xray Masks and Labels"
PROJECT_NAME_FULL: str = "Chest Xray Masks and Labels"
HIDE_DATASET = False  # set False when 100% sure about repo quality

##################################
# * After uploading to instance ##
##################################
LICENSE: License = License.CC0_1_0()
APPLICATIONS: List[Union[Industry, Domain, Research]] = [Industry.Medical()]
CATEGORY: Category = Category.Medical()

CV_TASKS: List[CVTask] = [
    CVTask.InstanceSegmentation(),
    CVTask.SemanticSegmentation(),
    CVTask.ObjectDetection(),
]
ANNOTATION_TYPES: List[AnnotationType] = [AnnotationType.InstanceSegmentation()]

RELEASE_DATE: Optional[str] = None  # e.g. "YYYY-MM-DD"
if RELEASE_DATE is None:
    RELEASE_YEAR: int = 2019

HOMEPAGE_URL: str = "https://www.kaggle.com/datasets/nikhilpandey360/chest-xray-masks-and-labels"
# e.g. "https://some.com/dataset/homepage"

PREVIEW_IMAGE_ID: int = 2082282
# This should be filled AFTER uploading images to instance, just ID of any image.

GITHUB_URL: str = "https://github.com/dataset-ninja/chest-xray"
# URL to GitHub repo on dataset ninja (e.g. "https://github.com/dataset-ninja/some-dataset")

##################################
### * Optional after uploading ###
##################################
DOWNLOAD_ORIGINAL_URL: Optional[
    Union[str, dict]
] = "https://www.kaggle.com/datasets/nikhilpandey360/chest-xray-masks-and-labels/download?datasetVersionNumber=1"
# Optional link for downloading original dataset (e.g. "https://some.com/dataset/download")

CLASS2COLOR: Optional[Dict[str, List[str]]] = None
# If specific colors for classes are needed, fill this dict (e.g. {"class1": [255, 0, 0], "class2": [0, 255, 0]})

PAPER: Optional[str] = "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4256233/"
CITATION_URL: Optional[
    str
] = "https://www.kaggle.com/datasets/nikhilpandey360/chest-xray-masks-and-labels"
AUTHORS: Optional[List[str]] = [
    "Stefan Jaeger",
    "Sema Candemir",
    "Sameer Antani",
    "Yì-Xiáng J. Wáng",
    "Pu-Xuan Lu",
    "George Thoma",
]
AUTHORS_CONTACTS: Optional[List[str]] = ["stefan.jaeger@nih.gov"]

ORGANIZATION_NAME: Optional[Union[str, List[str]]] = [
    "National Institutes of Health, USA",
    "The Chinese University of Hong Kong, China",
    "The Shenzhen No. 3 People's Hospital, China",
]
ORGANIZATION_URL: Optional[Union[str, List[str]]] = [
    "https://www.nih.gov/",
    "https://www.cuhk.edu.hk/",
    "https://www.szhospital.com/",
]

SLYTAGSPLIT: Optional[Dict[str, List[str]]] = {
    "origins of data": [
        "Montgomery County",
        "Shenzhen",
    ],
    "__POSTTEXT__": 'Additionaly, every image has <span style="background-color: #ecdefc; padding: 2px 4px; border-radius: 4px;">info</span> with text medical recordings',
}
TAGS: List[str] = None

##################################
###### ? Checks. Do not edit #####
##################################


def check_names():
    fields_before_upload = [PROJECT_NAME, PROJECT_NAME_FULL]
    if any([field is None for field in fields_before_upload]):
        raise ValueError("Please fill all fields in settings.py before uploading to instance.")


def get_settings():
    if RELEASE_DATE is not None:
        global RELEASE_YEAR
        RELEASE_YEAR = int(RELEASE_DATE.split("-")[0])

    settings = {
        "project_name": PROJECT_NAME,
        "license": LICENSE,
        "hide_dataset": HIDE_DATASET,
        "applications": APPLICATIONS,
        "category": CATEGORY,
        "cv_tasks": CV_TASKS,
        "annotation_types": ANNOTATION_TYPES,
        "release_year": RELEASE_YEAR,
        "homepage_url": HOMEPAGE_URL,
        "preview_image_id": PREVIEW_IMAGE_ID,
        "github_url": GITHUB_URL,
    }

    if any([field is None for field in settings.values()]):
        raise ValueError("Please fill all fields in settings.py after uploading to instance.")

    settings["release_date"] = RELEASE_DATE
    settings["project_name_full"] = PROJECT_NAME_FULL or PROJECT_NAME
    settings["download_original_url"] = DOWNLOAD_ORIGINAL_URL
    settings["class2color"] = CLASS2COLOR
    settings["paper"] = PAPER
    settings["citation_url"] = CITATION_URL
    settings["authors"] = AUTHORS
    settings["authors_contacts"] = AUTHORS_CONTACTS
    settings["organization_name"] = ORGANIZATION_NAME
    settings["organization_url"] = ORGANIZATION_URL
    settings["slytagsplit"] = SLYTAGSPLIT
    settings["tags"] = TAGS

    return settings
