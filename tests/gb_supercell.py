from siman.geo import create_supercell
from siman.calc_manage import smart_structure_read
from Grain import supercell
from Grain import grain

r3m = smart_structure_read('lno.r3m.conventional.POSCAR')

gr = grain_const(r3m, [-1, 1, -2], [-1, -1, 0])


super_r3m = create_supercell(r3m, [[3, 0, 0], [0, 3, 0], [0, 0, 3]])
super_r3m.printme()

workinstance = supercell.tools(super_r3m)
workinstance.threshold = 0.01
unitcell = workinstance.find_unitcell()

print(f'unitcell natoms: {len(unitcell.keys())}')
# for k, v in unitcell.items():
#     print(k, v)
