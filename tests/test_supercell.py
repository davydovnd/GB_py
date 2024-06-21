from siman.calc_manage import smart_structure_read
from siman.geo import create_supercell

from Grain import supercell
from Grain import grain

#unitcell
nio = smart_structure_read('nio.cif')
print('unitcell', nio.natom)
#supercell 
super_nio = create_supercell(nio, [[1, 0, 0], [0, 2, 0], [0, 0, 1]])


workinstance = supercell.tools(super_nio)
unitcell = workinstance.find_unitcell()

for k, v in unitcell.items():
    print(k, v)