from siman.core.structure import Structure
from siman.calc_manage import smart_structure_read
import sys
pp = '/Users/ndavydov/Documents/Skoltech/Science/GB_py'
sys.path.append(pp+'/Grain')
from siman.geo import create_supercell

import supercell
from grain import grain_const


nio = smart_structure_read('nio.cif')
# print(type(nio))
#unitcell LiNiO2 R3m
st1 = smart_structure_read("/Users/ndavydov/Documents/Skoltech/Science/cifs/POSCAR_LiNiO2_r3m_su_4uiAg_100_end_from_dima_aks")
st2 = "/Users/ndavydov/Documents/Skoltech/Science/cifs/POSCAR_LiNiO2_r3m_su_4uiAg_100_end_from_dima_aks"

# sc = create_supercell(st1, [[1, 0, 0], [0, 2, 0], [0, 0, 1]])

# st = supercell.tools(sc)
# st = st.find_unitcell()
# print(isinstance(nio, Structure) )
# print(st)
#Constraction of the grain with creatrd vectors from GB plane (-1,1,-2) and roationa axis [-1,-1,0]
sc_gr = grain_const(st1, [-1,1,-2], [-1,-1,0] )
# sc_gr = grain_const(st2, [-1,1,-2], [-1,-1,0] )
sc_gr.printme()
gr = supercell.tools(sc_gr)
prim_gr = gr.find_unitcell()



# gr = smart_structure_read(prim_gr)