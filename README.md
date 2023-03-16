# [Play now!](https://spphire.github.io/RM-labeling-tool/)

# click "Play now!" link above, you can quickly get vast datasets of Energy Mechanism

## Instrcutions

### Moving:

·Press the WASD keys and cooperate with the mouse

### Controling:

#### For Energy Mechanism

·Press the **R** keys to turn on or off the rotation of Energy Mechanism

·Press the **T** keys to randomly set the state of the fan blades of Energy Mechanism (OFF,UNACTIVATED,ACTIVATED)

#### For Armor Plate

·Press the **F** keys to create a new armor plate on your current position

·**Move the center of the screen to the armor plate**, and that the armor can be controled(with green outline)
 
 Press the **2,3,4,5,6** keys to set the tag of the armor controled(with green outline)

 Press the **C** keys to switch the light color of the armor controled(with green outline) red or blue

 Hold on pressing **right mouse button**, you can grab the armor with you

### Photoing:

·Press the **P** keys to get a screenshot and it will be labeled automatically

(**Tips:** Turn off "Asking before downloading" in your browser settings and set the default download path *so that* You don't need to manually confirm the download every time you photo)

You will get 4 files, one is .jpg which is raw picture, two are .json and .txt which includes label information (2 format), one is .png which visualizes the label information to check if there's something wrong.

**explanation of label information:**

#### For Energy Mechanism：

0: blue R, 1: blue Unactivated, 2: blue Activated, 3: red R, 4: red Unactivated, 5: red Activated .

#### For Armor Plate：

final label = color*9+tag

with color, 0: blue, 1: red, 2: grey, 3: purple

with tag, 0: sentry, 1: hero, 2: engineer, 3: infantry3, 4: infantry4, 5: infantry5, 6: outpost, 7: base(small), 8: base(big)

## labeling performance

![draw2023_3_8_17_40_33_832](https://user-images.githubusercontent.com/56157591/223679161-afcae665-30b0-40bf-9553-21adc28698b2.png)

可控装甲板