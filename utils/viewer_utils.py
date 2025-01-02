import py3Dmol

def view_mol(mol, color="white"):
    viewer = py3Dmol.view()

    xyz_data = str(len(mol)) + "\n" + "comment line\n" + mol.to_xyz()
    viewer.addModel(xyz_data, "xyz")

    for i, atom in enumerate(mol):
        viewer.addSphere(
            {
                "center": {"x": atom.x, "y": atom.y, "z": atom.z},
                "radius": 0.3,
                "color": color,
            }
        )

        viewer.addLabel(
            str(i + 1),
            {
                "position": {"x": atom.x, "y": atom.y, "z": atom.z},
                # "fontSize": 12,
                "fontSize": 8,
                "fontColor": color,
                "backgroundColor": "black",
                "backgroundOpacity": 0.6,
            },
        )

    # draw bonds
    viewer.setStyle({}, {"stick": {"radius": 0.15}})

    viewer.zoomTo()
    viewer.show()
