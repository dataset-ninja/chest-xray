import os

import supervisely as sly
from cv2 import connectedComponents
from supervisely.io.fs import file_exists, get_file_name, get_file_name_with_ext


def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:
    dataset_path = "/home/iwatkot/supervisely/ninja-datasets/chest_xray/Lung Segmentation"

    ds_name = "ds"
    batch_size = 30

    images_folder_name = "CXR_png"
    masks_folder_name = "masks"
    tag_data_folder_name = "ClinicalReadings"

    def create_ann(image_path):
        labels = []

        image_name = get_file_name_with_ext(image_path)
        image_np = sly.imaging.image.read(image_path)[:, :, 0]
        img_height = image_np.shape[0]
        img_wight = image_np.shape[1]
        mask_path = os.path.join(masks_path, image_name)
        if file_exists(mask_path):
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
            tag_diagnosis = sly.Tag(meta=tag_meta, value=content)

        return sly.Annotation(
            img_size=(img_height, img_wight), labels=labels, img_tags=[tag_diagnosis]
        )

    images_path = os.path.join(dataset_path, images_folder_name)
    images_names = os.listdir(images_path)
    masks_path = os.path.join(dataset_path, masks_folder_name)
    tags_data_path = os.path.join(dataset_path, tag_data_folder_name)

    obj_class = sly.ObjClass("lung", sly.Bitmap)
    obj_class_collection = sly.ObjClassCollection([obj_class])

    tag_meta = sly.TagMeta("info", sly.TagValueType.ANY_STRING)

    project = api.project.create(workspace_id, project_name, change_name_if_conflict=True)
    meta = sly.ProjectMeta(obj_classes=obj_class_collection, tag_metas=[tag_meta])
    api.project.update_meta(project.id, meta.to_json())
    dataset = api.dataset.create(project.id, ds_name, change_name_if_conflict=True)

    progress = sly.Progress("Create dataset {}".format(ds_name), len(images_names))

    for img_names_batch in sly.batched(images_names, batch_size=batch_size):
        images_pathes_batch = [
            os.path.join(images_path, image_name) for image_name in img_names_batch
        ]

        anns_batch = [create_ann(image_path) for image_path in images_pathes_batch]

        img_infos = api.image.upload_paths(dataset.id, img_names_batch, images_pathes_batch)
        img_ids = [im_info.id for im_info in img_infos]

        api.annotation.upload_anns(img_ids, anns_batch)

        progress.iters_done_report(len(img_names_batch))

    return project
