import numpy as np
from siman.calc_manage import smart_structure_read

LN = smart_structure_read(input_geo_file = "/Users/ndavydov/Documents/Skoltech/Science/cifs/POSCAR_LiNiO2_r3m_su_4uiAg_100_end_from_dima_aks")
LNconv = LN.copy()
st = LN.get_conventional_cell()
LNconv.end = st.rotate([0,0,1], 30)

if 0:
    LNconv.path["input_geo"] = 'xyz/LNconv.geo'
    LNconv.write_geometry(geotype = 'end', override = 1)
    LNconv.end.write_poscar()
# print(LN.rprimd)
# print(max([LN.rprimd[0],LN.rprimd[1],LN.rprimd[2]]))
# print(LN.rprimd[0])
# print(LN.rprimd[1])
# print(LN.rprimd[2])
# print(np.cross(LN.rprimd[0], LN.rprimd[1]) )
# print(np.linalg.norm(LN.rprimd[0]),np.linalg.norm(LN.rprimd[1]))
# print(np.linalg.norm( np.cross(LN.rprimd[0], LN.rprimd[1])  ))
# print(np.linalg.norm( np.cross(LN.rprimd[0], LN.rprimd[2])  ))
# print(np.linalg.norm( np.cross(LN.rprimd[1], LN.rprimd[2])  ))

#finding GB area 
A_ab = np.linalg.norm( np.cross(LN.rprimd[0], LN.rprimd[1])  ) 
A_ac = np.linalg.norm( np.cross(LN.rprimd[0], LN.rprimd[2])  )
A_bc = np.linalg.norm( np.cross(LN.rprimd[1], LN.rprimd[2])  )
A = min(A_ab, A_ac, A_bc) #finding GB area
# print(A)


from siman.geo import hkl2uvw, three2four_index, create_supercell, four2three_index

rprimd = [[np.sqrt(0.75)*2.9380, -5.0000000000E-01*2.9380,  0.0000000000E+00],
[0.0000000000E+00,  1.0000000000E+00*2.9380,  0.0000000000E+00],
[0.0000000000E+00,  0.0000000000E+00,  1.0000000000E+00*14.6445]]


hkl = [1,-1,2]

# print(hkl2uvw(hkl, rprimd))
# print( three2four_index ( hkl2uvw(hkl, rprimd) ) )
# uvtw = three2four_index ( hkl2uvw(hkl, rprimd) )
# print(uvtw)
# print(four2three_index(uvtw)  )

# print(hkl2uvw([1,-1, 8], LNconv.end.rprimd) )
# print(hkl2uvw([1,-1,-4], LNconv.end.rprimd) )
# print( three2four_index (  hkl2uvw([1,-1,-4], LNconv.end.rprimd) ))
# print( three2four_index (  hkl2uvw([1,-1,8], LNconv.end.rprimd) ))
# uvw = np.array([0,0,1])
# print( three2four_index ( uvw ) )
# print(dir(LN))
# for uvtw in [8, -8, 0, 1], [-1,1,0,1],[-1,-1,2,0]:
#     ''
#     print(four2three_index(uvtw)  )

# st = create_supercell(LNconv.end, [[8, -8, 1],[-1,1,1],[-1,-1,0]], mul = (1/3, 1/3, 1)) #
# st.jmol()
rprimd = LNconv.end.rprimd
hkl = [-1,1,-2]
uvw = [-1,-1,0]
print('rprimd', rprimd)
print()
print('hkl', hkl)
print()
print('uvw', uvw)
