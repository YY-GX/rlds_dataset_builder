#!/bin/zsh

PARENT_DIR="."
TASKS=(
    "KITCHEN_SCENE10_close_the_top_drawer_of_the_cabinet"
    "KITCHEN_SCENE10_put_the_black_bowl_in_the_top_drawer_of_the_cabinet"
    "KITCHEN_SCENE1_open_the_bottom_drawer_of_the_cabinet"
    "KITCHEN_SCENE1_open_the_top_drawer_of_the_cabinet"
    "KITCHEN_SCENE1_put_the_black_bowl_on_the_plate"
    "KITCHEN_SCENE1_put_the_black_bowl_on_top_of_the_cabinet"
    "KITCHEN_SCENE2_open_the_top_drawer_of_the_cabinet"
    "KITCHEN_SCENE2_put_the_black_bowl_at_the_back_on_the_plate"
    "KITCHEN_SCENE2_put_the_black_bowl_at_the_front_on_the_plate"
    "KITCHEN_SCENE2_put_the_middle_black_bowl_on_the_plate"
    "KITCHEN_SCENE2_put_the_middle_black_bowl_on_top_of_the_cabinet"
    "KITCHEN_SCENE2_stack_the_black_bowl_at_the_front_on_the_black_bowl_in_the_middle"
    "KITCHEN_SCENE2_stack_the_middle_black_bowl_on_the_back_black_bowl"
    "KITCHEN_SCENE3_put_the_frying_pan_on_the_stove"
    "KITCHEN_SCENE3_put_the_moka_pot_on_the_stove"
    "KITCHEN_SCENE3_turn_on_the_stove"
    "KITCHEN_SCENE4_close_the_bottom_drawer_of_the_cabinet"
    "KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet"
    "KITCHEN_SCENE4_put_the_black_bowl_on_top_of_the_cabinet"
    "KITCHEN_SCENE4_put_the_wine_bottle_in_the_bottom_drawer_of_the_cabinet"
    "KITCHEN_SCENE4_put_the_wine_bottle_on_the_wine_rack"
    "KITCHEN_SCENE5_close_the_top_drawer_of_the_cabinet"
    "KITCHEN_SCENE5_put_the_black_bowl_in_the_top_drawer_of_the_cabinet"
    "KITCHEN_SCENE5_put_the_black_bowl_on_the_plate"
    "KITCHEN_SCENE5_put_the_black_bowl_on_top_of_the_cabinet"
    "KITCHEN_SCENE5_put_the_ketchup_in_the_top_drawer_of_the_cabinet"
    "KITCHEN_SCENE6_close_the_microwave"
    "KITCHEN_SCENE7_open_the_microwave"
    "KITCHEN_SCENE7_put_the_white_bowl_on_the_plate"
    "KITCHEN_SCENE7_put_the_white_bowl_to_the_right_of_the_plate"
    "KITCHEN_SCENE8_put_the_right_moka_pot_on_the_stove"
    "KITCHEN_SCENE8_turn_off_the_stove"
    "KITCHEN_SCENE9_put_the_frying_pan_on_the_cabinet_shelf"
    "KITCHEN_SCENE9_put_the_frying_pan_on_top_of_the_cabinet"
    "KITCHEN_SCENE9_put_the_frying_pan_under_the_cabinet_shelf"
    "KITCHEN_SCENE9_put_the_white_bowl_on_top_of_the_cabinet"
    "KITCHEN_SCENE9_turn_on_the_stove"
    "LIVING_ROOM_SCENE5_put_the_red_mug_on_the_left_plate"
    "LIVING_ROOM_SCENE5_put_the_red_mug_on_the_right_plate"
    "LIVING_ROOM_SCENE5_put_the_white_mug_on_the_left_plate"
    "LIVING_ROOM_SCENE6_put_the_chocolate_pudding_to_the_left_of_the_plate"
    "LIVING_ROOM_SCENE6_put_the_chocolate_pudding_to_the_right_of_the_plate"
    "LIVING_ROOM_SCENE6_put_the_red_mug_on_the_plate"
    "LIVING_ROOM_SCENE6_put_the_white_mug_on_the_plate"
)

for TASK in "${TASKS[@]}"
do
    TASK_DIR="$PARENT_DIR/$TASK"
    if [ -d "$TASK_DIR" ]; then
        echo "Building dataset for $TASK"
        cd "$TASK_DIR" || exit
        tfds build --overwrite --data_dir /mnt/arc/yygx/pkgs_baselines/openvla/datasets/libero_44_split/
        cd "$PARENT_DIR" || exit
    else
        echo "Directory for $TASK not found!"
    fi
done

echo "All tasks processed."
