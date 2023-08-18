# https://www.kaggle.com/datasets/nikhilpandey360/chest-xray-masks-and-labels

import os
import numpy as np
import supervisely as sly
from supervisely.io.fs import get_file_name_with_ext, get_file_name, file_exists, get_file_ext
from cv2 import connectedComponents
from dotenv import load_dotenv


# if sly.is_development():
# load_dotenv("local.env")
# load_dotenv(os.path.expanduser("~/supervisely.env"))

# api = sly.Api.from_env()
# team_id = sly.env.team_id()
# workspace_id = sly.env.workspace_id()

def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:
    project_name = "Chest Xray"
    dataset_path = "APP_DATA/Lung Segmentation"
    ds_name = "ds"
    batch_size = 30

    images_folder_name = "CXR_png"
    masks_folder_name = "masks"
    tag_data_folder_name = "ClinicalReadings"

    folder_to_ds_name = {"CXRpng-train": images_folder_name, "test": "test"}


    def create_ann(image_path):
        labels = []

        image_name = get_file_name_with_ext(image_path)
        image_np = sly.imaging.image.read(image_path)[:, :, 0]
        img_height = image_np.shape[0]
        img_wight = image_np.shape[1]
        source_name = image_name.split("_")[0]
        if source_name == "MCUCXR":
            mask_path = os.path.join(masks_path, image_name)
        else:
            mask_path = os.path.join(
                masks_path, get_file_name(image_name) + "_mask" + get_file_ext(image_name)
            )
        if file_exists(mask_path):
            obj_class = name_to_class[image_name.split("_")[-1]]
            mask_np = sly.imaging.image.read(mask_path)[:, :, 0]
            mask = mask_np == 255
            ret, curr_mask = connectedComponents(mask.astype("uint8"), connectivity=8)
            for i in range(1, ret):
                obj_mask = curr_mask == i
                curr_bitmap = sly.Bitmap(obj_mask)
                curr_label = sly.Label(curr_bitmap, obj_class)
                labels.append(curr_label)

        tag_data_path = os.path.join(tags_data_path, get_file_name(image_path) + ".txt")
        with open(tag_data_path) as f:
            content = f.read()
            if len(content) > 255:
                content = content[:255]
            tag_diagnosis = sly.Tag(meta=tag_meta, value=content)

        source_tag = source_to_tag[source_name]

        return sly.Annotation(
            img_size=(img_height, img_wight), labels=labels, img_tags=[tag_diagnosis, source_tag]
        )


    masks_path = os.path.join(dataset_path, masks_folder_name)
    tags_data_path = os.path.join(dataset_path, tag_data_folder_name)

    obj_class_healthy = sly.ObjClass("healthy lung", sly.Bitmap)
    obj_class_tuberculous = sly.ObjClass("tuberculosis lung", sly.Bitmap)
    name_to_class = {"0.png": obj_class_healthy, "1.png": obj_class_tuberculous}

    tag_meta = sly.TagMeta("info", sly.TagValueType.ANY_STRING)
    tag_montgomery = sly.TagMeta("Montgomery County", sly.TagValueType.NONE)
    tag_shenzhen = sly.TagMeta("Shenzhen", sly.TagValueType.NONE)

    source_to_tag = {"CHNCXR": tag_shenzhen, "MCUCXR": tag_montgomery}


    project = api.project.create(workspace_id, project_name, change_name_if_conflict=True)
    meta = sly.ProjectMeta(
        obj_classes=[obj_class_healthy, obj_class_tuberculous],
        tag_metas=[tag_meta, tag_montgomery, tag_shenzhen],
    )
    api.project.update_meta(project.id, meta.to_json())


    for ds_name in ["CXRpng-train", "test"]:
        images_folder_name = folder_to_ds_name[ds_name]
        images_path = os.path.join(dataset_path, images_folder_name)
        images_names = os.listdir(images_path)

        dataset = api.dataset.create(project.id, ds_name, change_name_if_conflict=True)

        progress = sly.Progress("Create dataset {}".format(ds_name), len(images_names))

        for img_names_batch in sly.batched(images_names, batch_size=batch_size):
            images_pathes_batch = [
                os.path.join(images_path, image_name) for image_name in img_names_batch
            ]

            img_infos = api.image.upload_paths(dataset.id, img_names_batch, images_pathes_batch)
            img_ids = [im_info.id for im_info in img_infos]

            if ds_name != "test":
                anns_batch = [create_ann(image_path) for image_path in images_pathes_batch]
                api.annotation.upload_anns(img_ids, anns_batch)

            progress.iters_done_report(len(img_names_batch))
    return project