import os
import re

PARENT_DIR = "."
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

def remove_class_suffix(task_name):
    # Locate the dataset_builder.py file
    task_dir = os.path.join(PARENT_DIR, task_name)
    dataset_builder_file = os.path.join(task_dir, f"{task_name}_dataset_builder.py")

    if os.path.exists(dataset_builder_file):
        # Read and modify the file to remove the 'DatasetBuilder' suffix from the class name
        with open(dataset_builder_file, "r") as f:
            content = f.read()

        # Use regex to find and replace the class name with the suffix removed
        content = re.sub(r'class (\w+)DatasetBuilder\(', r'class \1(', content)

        # Write the modified content back to the file
        with open(dataset_builder_file, "w") as f:
            f.write(content)

        print(f"Updated class name for: {task_name}")
    else:
        print(f"Dataset builder file not found for: {task_name}")

def main():
    for task in TASKS:
        remove_class_suffix(task)

if __name__ == "__main__":
    main()
