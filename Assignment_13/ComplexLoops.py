import arcade


COLUMN_SPACING = 20
ROW_SPACING = 20
LEFT_MARGIN = 110
BOTTOM_MARGIN = 110
ANGLE = 45

arcade.open_window(400, 400, "Complex Loops - Box")
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()

for row in range(10):
    for column in range(10):
        x = column * COLUMN_SPACING + LEFT_MARGIN
        y = row * ROW_SPACING + BOTTOM_MARGIN

        if row % 2 == 0:
            if column % 2 == 0:
                arcade.draw_rectangle_filled(x, y, 10, 10, arcade.color.RED, ANGLE)
            else:
                arcade.draw_rectangle_filled(x, y, 10, 10, arcade.color.BLUE, ANGLE)
        else:
            if column % 2 == 0:
                arcade.draw_rectangle_filled(x, y, 10, 10, arcade.color.BLUE, ANGLE)
            else:
                arcade.draw_rectangle_filled(x, y, 10, 10, arcade.color.RED, ANGLE)

arcade.finish_render()
arcade.run()