import view
import controller

if view.Mode() == 1:
    controller.Export()
else:
    controller.Import()