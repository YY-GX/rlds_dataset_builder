import os
import shutil
import glob

TASKS = [
    "KITCHEN_SCENE10_close_the_top_drawer_of_the_cabinet",
    "KITCHEN_SCENE10_put_the_black_bowl_in_the_top_drawer_of_the_cabinet",
    "KITCHEN_SCENE1_open_the_bottom_drawer_of_the_cabinet",
    "KITCHEN_SCENE1_open_the_top_drawer_of_the_cabinet",
    "KITCHEN_SCENE1_put_the_black_bowl_on_the_plate",
    "KITCHEN_SCENE1_put_the_black_bowl_on_top_of_the_cabinet",
    "KITCHEN_SCENE2_open_the_top_drawer_of_the_cabinet",
    "KITCHEN_SCENE2_put_the_black_bowl_at_the_back_on_the_plate",
    "KITCHEN_SCENE2_put_the_black_bowl_at_the_front_on_the_plate",
    "KITCHEN_SCENE2_put_the_middle_black_bowl_on_the_plate",
    "KITCHEN_SCENE2_put_the_middle_black_bowl_on_top_of_the_cabinet",
    "KITCHEN_SCENE2_stack_the_black_bowl_at_the_front_on_the_black_bowl_in_the_middle",
    "KITCHEN_SCENE2_stack_the_middle_black_bowl_on_the_back_black_bowl",
    "KITCHEN_SCENE3_put_the_frying_pan_on_the_stove",
    "KITCHEN_SCENE3_put_the_moka_pot_on_the_stove",
    "KITCHEN_SCENE3_turn_on_the_stove",
    "KITCHEN_SCENE4_close_the_bottom_drawer_of_the_cabinet",
    "KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet",
    "KITCHEN_SCENE4_put_the_black_bowl_on_top_of_the_cabinet",
    "KITCHEN_SCENE4_put_the_wine_bottle_in_the_bottom_drawer_of_the_cabinet",
    "KITCHEN_SCENE4_put_the_wine_bottle_on_the_wine_rack",
    "KITCHEN_SCENE5_close_the_top_drawer_of_the_cabinet",
    "KITCHEN_SCENE5_put_the_black_bowl_in_the_top_drawer_of_the_cabinet",
    "KITCHEN_SCENE5_put_the_black_bowl_on_the_plate",
    "KITCHEN_SCENE5_put_the_black_bowl_on_top_of_the_cabinet",
    "KITCHEN_SCENE5_put_the_ketchup_in_the_top_drawer_of_the_cabinet",
    "KITCHEN_SCENE6_close_the_microwave",
    "KITCHEN_SCENE7_open_the_microwave",
    "KITCHEN_SCENE7_put_the_white_bowl_on_the_plate",
    "KITCHEN_SCENE7_put_the_white_bowl_to_the_right_of_the_plate",
    "KITCHEN_SCENE8_put_the_right_moka_pot_on_the_stove",
    "KITCHEN_SCENE8_turn_off_the_stove",
    "KITCHEN_SCENE9_put_the_frying_pan_on_the_cabinet_shelf",
    "KITCHEN_SCENE9_put_the_frying_pan_on_top_of_the_cabinet",
    "KITCHEN_SCENE9_put_the_frying_pan_under_the_cabinet_shelf",
    "KITCHEN_SCENE9_put_the_white_bowl_on_top_of_the_cabinet",
    "KITCHEN_SCENE9_turn_on_the_stove",
    "LIVING_ROOM_SCENE5_put_the_red_mug_on_the_left_plate",
    "LIVING_ROOM_SCENE5_put_the_red_mug_on_the_right_plate",
    "LIVING_ROOM_SCENE5_put_the_white_mug_on_the_left_plate",
    "LIVING_ROOM_SCENE6_put_the_chocolate_pudding_to_the_left_of_the_plate",
    "LIVING_ROOM_SCENE6_put_the_chocolate_pudding_to_the_right_of_the_plate",
    "LIVING_ROOM_SCENE6_put_the_red_mug_on_the_plate",
    "LIVING_ROOM_SCENE6_put_the_white_mug_on_the_plate",
]

EXISTING_TASKS = [
    "KITCHEN_SCENE10_close_the_top_drawer_of_the_cabinet",
    "KITCHEN_SCENE1_open_the_top_drawer_of_the_cabinet",
    "KITCHEN_SCENE1_put_the_black_bowl_on_the_plate",
]

PARENT_DIR = "."


def camel_case(task_name):
    words = task_name.split("_")
    return words[0].lower() + ''.join(word.capitalize() for word in words[1:])


def create_task_folder(task_name):
    # Create folder
    task_dir = os.path.join(PARENT_DIR, task_name)
    os.makedirs(task_dir, exist_ok=True)

    # Copy common files from an existing task folder
    existing_task_dir = os.path.join(PARENT_DIR, EXISTING_TASKS[0])
    common_files = ["CITATIONS.bib", "conversion_utils.py", "__init__.py", "README.md"]
    for file_name in common_files:
        shutil.copy(os.path.join(existing_task_dir, file_name), task_dir)

    # Copy the existing dataset_builder.py file and modify it
    existing_dataset_builder = os.path.join(existing_task_dir, f"{EXISTING_TASKS[0]}_dataset_builder.py")
    new_dataset_builder = os.path.join(task_dir, f"{task_name}_dataset_builder.py")
    with open(existing_dataset_builder, "r") as f:
        content = f.read()

    # Modify the class name and the dataset path in the copied content
    class_name = camel_case(task_name)
    content = content.replace(camel_case(EXISTING_TASKS[0]), class_name)
    content = content.replace(f"{EXISTING_TASKS[0]}_demo.hdf5", f"{task_name}_demo.hdf5")

    # Write the modified content to the new dataset_builder.py file
    with open(new_dataset_builder, "w") as f:
        f.write(content)


def main():
    for task in TASKS:
        if task not in EXISTING_TASKS:
            create_task_folder(task)
            print(f"Created folder and files for: {task}")

if __name__ == "__main__":
    main()
