# Chasing Quixote — minimal notebook UI prototype.
# Requires the cq_evidence default from game/script.rpy.
screen cq_notebook():
    modal True
    zorder 100

    frame:
        xalign 0.5
        yalign 0.5
        xmaximum 850
        xpadding 36
        ypadding 32

        vbox:
            spacing 16
            text "Fox's Notebook" size 36
            text "Observations (prototype)" size 19

            if cq_evidence:
                for item in cq_evidence:
                    if item == "schedule":
                        text "Event schedule — revised times overlap."
                    elif item == "noticeboard":
                        text "Noticeboard — room changed this morning."
                    else:
                        text "[item]"
            else:
                text "Nothing recorded yet."

            if cq_reconstruction_complete:
                text "Working theory: check whether the room change explains the conflict."
            else:
                text "Working theory: no reconstruction completed."

            textbutton "Close notebook":
                action Return()
                xalign 1.0

    key "K_ESCAPE" action Return()
