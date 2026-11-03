# Chasing Quixote — minimal notebook UI prototype.
# Requires the cq_evidence default from game/script.rpy.
# Shown on the overlay, above the launcher quick menu, so it can be read and closed.
screen cq_notebook():
    layer "overlay"
    modal True
    zorder 200

    frame:
        xalign 0.5
        yalign 0.5
        xmaximum 850
        xpadding 36
        ypadding 32

        vbox:
            spacing 16
            text "Fox's Notebook" size 36 id "notebook_title"
            text "Observations (prototype)" size 19

            if cq_evidence:
                for item in cq_evidence:
                    if item == "schedule":
                        text "Event schedule — revised times overlap." id "notebook_schedule"
                    elif item == "noticeboard":
                        text "Noticeboard — room changed this morning." id "notebook_noticeboard"
                    else:
                        text "[item]"
            else:
                text "Nothing recorded yet." id "notebook_empty"

            if cq_reconstruction_complete:
                text "Working theory: check whether the room change explains the conflict." id "notebook_theory"
            else:
                text "Working theory: no reconstruction completed." id "notebook_theory_empty"

            textbutton "Close notebook":
                id "notebook_close"
                action Return()
                xalign 1.0

    key "K_ESCAPE" action Return()
    key "game_menu" action Return()
