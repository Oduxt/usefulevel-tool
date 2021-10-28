def on_forever():
    x = input.acceleration(Dimension.X)
    y = input.acceleration(Dimension.Y)
    if abs(x) > 32:
        basic.show_icon(IconNames.NO)
    elif abs(y) > 32:
        basic.show_icon(IconNames.ANGRY)
    else:
        basic.show_icon(IconNames.YES)

    basic.forever(on_forever)
