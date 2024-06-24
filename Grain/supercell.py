import numpy as np

from siman.calc_manage import smart_structure_read
from siman.geo import create_supercell
from siman.core.structure import Structure

"""
To do: 
- fix reduced coordinates
- convert back to siman structure
- check all three dimenstions
- simplify the code
    - use of np.unique
    - get rid of local_format
    - etc
"""


class tools:
    """Object to manipulate supercell structures

    arguments:
    supercell - siman structure object
    """

    def __init__(self, supercell: Structure) -> None:

        self.supercell = supercell
        self.log = {0: {}, 1: {}, 2: {}}
        self.unitcell = None
        self.threshold = 0.01
        self.local_format = dict()
        self.structure_to_dict()
        self.soft_match = lambda x, y: True if abs(
            x-y) <= self.threshold else False

    def structure_to_dict(self):
        """Converts siman structure to local format with elements symbols and position treated at the same level
        """

        for index, (name, pos) in enumerate(zip(self.supercell.get_elements(), self.supercell.xred)):
            self.local_format.update({index: dict(element=name, pos=pos)})

    def find_unitcell(self):
        """Method to find unitcell. It goes through directions (a,b,c) and layers to find repititons in the sturcture."""
        atoms = self.local_format
        for direction in range(3):
            print('processing direction:', direction)
            # preporcessing.  finds layers in one direction and create log structure with atoms splited by layers.
            self.log[direction]['unique'] = np.unique(
                [np.floor(atoms[atom_index]['pos'][direction]/self.threshold).astype(int)*self.threshold for atom_index in atoms])

            for layer_index, position in enumerate(self.log[direction]['unique']):
                self.log[direction][layer_index] = {sub_index: item for sub_index, item in atoms.items(
                ) if self.soft_match(atoms[sub_index]['pos'][direction], position)}
            # print(self.log[direction]['unique'])
            subcell = {}  # here subsctructure will be written
            # iterates through layers
            for layer_index in range(0, len(self.log[direction]['unique'])):
                # checks if two layers match
                # print(self.log[direction][layer_index],
                #       self.log[direction][0], direction)
                tmp = self.check_if_layers_match(
                    self.log[direction][layer_index], self.log[direction][0], direction)
                # print(tmp)
                if tmp:  # if match then checks all other layers
                    next_layer_match = True  # assumtion
                    # checks if you layers below can be translated to the layers above. if not - no translations possible
                    if layer_index - 1 < len(self.log[direction]['unique'])/2:
                        for j in range(1, layer_index):
                            # checking other layers
                            check_all = self.check_if_layers_match(
                                self.log[direction][layer_index+j], self.log[direction][j], direction)
                            if not check_all:
                                next_layer_match = False  # we shoud go to another layers
                        if next_layer_match:  # everthing is fine, we did find unitcell
                            break
                # writes layer to subcell if everthing is ok
                subcell.update(self.log[direction][layer_index])
            atoms = subcell  # update for next direction
        self.unitcell = subcell
        return subcell

    def check_if_layers_match(self, layer1, layer2, direction):
        """
        Checks if two layers match (differs only in specified direction)
        Args:
         layer1, layer2 - local_format dictionaries
         direction - int
        """

        match = False
        for (k1, item1), (k2, item2) in zip(layer1.items(), layer2.items()):
            if item1['pos'][direction] != item2['pos'][direction]:
                # filter position can be improved, oneliner?
                tmp1 = [v for i, v in enumerate(
                    item1['pos']) if i != direction]
                tmp2 = [v for i, v in enumerate(
                    item2['pos']) if i != direction]
                # iteratire through every atom in the layers, order metter!  maybe needs to changed
                for position1, position2 in zip(tmp1, tmp2):
                    if abs(position1-position2) <= self.threshold and item1['element'] == item2['element']:
                        match = True
                    else:
                        match = False
                        break
        return match
