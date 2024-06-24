from siman.geo import create_supercell
from siman.calc_manage import smart_structure_read
from Grain import supercell

# from Grain import grain
# unitcell
r3m = smart_structure_read(
    '/Users/lusigeondzian/root/GB_py/tests/POSCAR_LiNiO2_r3m_su_4uiAg_100_end')
print('unitcell', r3m.natom)
# supercell
super_r3m = create_supercell(r3m, [[3, 0, 0], [0, 3, 0], [0, 0, 3]])
print(super_r3m.natom)
workinstance = supercell.tools(super_r3m)
print(workinstance.soft_match(0, 0.3))
unitcell = workinstance.find_unitcell()

for k, v in unitcell.items():
    print(k, v)
