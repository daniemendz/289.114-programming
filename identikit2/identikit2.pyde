add_library('controlP5')

def setup():
    size(720,485)
    global cp5
    cp5 = ControlP5(this)
    
    # alias
    (cp5.addTextfield('alias')
        .setPosition(500,20)
        .setSize(200,25)
    )

    # eye distance
    (cp5.addSlider('eye distance')
        .setPosition(500, 80)
        .setSize(200,20)
        .setRange(30,120)
        .setValue(80)
    )
    (cp5.addController('eye distance')
        .getCaptionLabel()
        .align(ControlP5.LEFT, ControlP5.BOTTOM_OUTSIDE)
        .setPaddingX(0)
    )
    
def draw():
    background('#004477')
    stroke('#ffffff')
    strokeWeight(3)
    axis = 250
    
    noFill()
    ellipse(axis , 220, 370,370)
    
    fill('#ffffff')
    textSize(20)
    textAlign(CENTER)
    alias = cp5.getController('alias').getText()
    text(alias, axis, 450)
    noFill()
    
    #eyes
    eyeDistance = cp5.getController('eye distance').getValue()
    eyesize = cp5.getController('eye size').getValue()
    ellipse(axis-eyedistance,180, eyesize,eyesize)
    ellipse(axis+eyedistance,180, eyesize,eyesize)
