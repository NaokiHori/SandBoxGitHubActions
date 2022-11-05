import pyvista as pv


def sphere():
    p = pv.Plotter(off_screen=True)
    p.add_mesh(pv.Sphere(), color="tan", show_edges=True)
    p.show(screenshot='sphere.png')
    p.close()

if __name__ == "__main__":
    sphere()

