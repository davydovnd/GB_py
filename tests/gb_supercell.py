from siman.geo import create_supercell
from siman.calc_manage import smart_structure_read
from Grain import supercell
from Grain.grain import grain_const

r3m = smart_structure_read('lno.r3m.conventional.POSCAR')

gr = grain_const(r3m, [-1, 1, -2], [-1, -1, 0])


workinstance = supercell.tools(gr)
workinstance.threshold = 0.0001
unitcell = workinstance.find_unitcell()

print(f'unitcell natoms: {len(unitcell.keys())}')
# for k, v in unitcell.items():
#     print(k, v)
gr.write_poscar('./POSCAR_gr')