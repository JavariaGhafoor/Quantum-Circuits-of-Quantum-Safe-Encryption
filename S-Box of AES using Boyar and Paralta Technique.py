import math

from projectq.ops import CNOT, Mea-
sure, X, Toffoli

from projectq import MainEngine

from projectq.meta import Compute, Un-
compute

from projectq.backends import Circuit-
Drawer,

ResourceCounter, ClassicalSimulator
import projectq.libs.math
drawing_engine = CircuitDrawer()
resource_counter = ResourceCounter()
sim = ClassicalSimulator()
eng = MainEngine(sim)

def aes-box(eng):
  U = eng.allocate_qureg(8)
  T = eng.allocate_qureg(15)
  Z = eng.allocate_qureg(1)
  S = eng.allocate_qureg(8)

input_m = [0]*(8)
output_m = [0]*(8)

with Compute(eng):
  CNOT | (U[0], U[5])
  CNOT | (U[3], U[5])
  CNOT | (U[6], U[5])
  CNOT | (U[0], U[4])
  CNOT | (U[3], U[4])
  CNOT | (U[6], U[4])
  Toffoli | (U[5], U[4], T[0]) #t2
  CNOT | (T[0], T[5])

  CNOT | (U[1], U[3])
  CNOT | (U[2], U[3])
  CNOT | (U[7], U[3])
  Toffoli | (U[3], U[7], T[0]) #t6
  CNOT | (U[0], U[6])
  CNOT | (U[0], U[2])
  CNOT | (U[4], U[2])
  CNOT | (U[5], U[2])
  CNOT | (U[6], U[2])
  Toffoli | (U[6], U[2], T[1]) #t7
  CNOT | (T[1], T[2])

  CNOT | (U[2], U[1])
  CNOT | (U[4], U[1])
  CNOT | (U[5], U[1])
  CNOT | (U[7], U[1])
  CNOT | (U[1], U[0])
  CNOT | (U[6], U[0])
  Toffoli | (U[1], U[0], T[1]) #t9

  CNOT | (U[1], U[6])
  CNOT | (U[0], U[2])
  Toffoli | (U[6], U[2], T[2]) #t11

  CNOT | (U[6], U[3])
  CNOT | (U[7], U[2])
  Toffoli | (U[3], U[2], T[3]) #t12
  CNOT | (T[3], T[4])
  
  CNOT | (U[1], U[6])
  CNOT | (U[5], U[6])
  CNOT | (U[2], U[0])
  CNOT | (U[4], U[0])
  CNOT | (U[7], U[0])
  Toffoli | (U[6], U[0], T[3]) #t14
  
  CNOT | (U[6], U[3])
  CNOT | (U[2], U[0])
  Toffoli | (U[3], U[0], T[4]) #t16
  
  CNOT | (T[3], T[1]) #t19
  
  CNOT | (U[1], U[3])
  CNOT | (U[7], U[4])
  Toffoli | (U[3], U[4], T[5]) #t4
  
  CNOT | (T[5], T[3]) #t17
  
  CNOT | (T[4], T[0]) #t18
  
  CNOT | (T[2], T[4]) #t20
  
  CNOT | (U[1], U[6])
  CNOT | (U[2], U[6])
  CNOT | (U[3], U[6])
  CNOT | (U[6], T[3]) #t21
  
  CNOT | (U[0], U[1])
  CNOT | (U[3], U[1])
  CNOT | (U[1], T[0]) #t22
  
  CNOT | (U[1], U[5])
  CNOT | (U[4], U[5])
  CNOT | (U[6], U[5])
  CNOT | (U[7], U[5])
  CNOT | (U[5], T[1]) #t23
  
  CNOT | (U[1], U[4])
  CNOT | (U[3], U[4])
  CNOT | (U[5], U[4])
  CNOT | (U[4], T[4]) #t24
  
  Toffoli | (T[3], T[1], T[6]) #t26
  CNOT | (T[0], T[3]) #t25
  
  CNOT | (T[4], T[7])
  CNOT | (T[6], T[7]) #t27
  
  CNOT | (T[0], T[6]) #t31
  Toffoli | (T[3], T[7], T[0]) #t29
  
  CNOT | (T[1], T[8])
  CNOT | (T[4], T[8]) #t30
  
  Toffoli | (T[6], T[8], T[9]) #t32
  
  #clean up T[8]:
  CNOT | (T[4], T[8])
  CNOT | (T[1], T[8])
  #t[8] is free to reuse
  
  CNOT | (T[4], T[9]) #t33
  CNOT | (T[9], T[1]) #t34
  
  CNOT | (T[7], T[8])
  CNOT | (T[9], T[8]) #t35
  
  Toffoli | (T[4], T[8], T[10]) #t36
  
  #clean up T[8] again:
  CNOT | (T[9], T[8])
  CNOT | (T[7], T[8])
  #t[8] is free to reuse
  
  CNOT | (T[10], T[1]) #t37
  CNOT | (T[10], T[7]) #t38

  Toffoli | (T[0], T[7], T[3]) #t40
  
  CNOT | (T[3], T[8])
  CNOT | (T[1], T[8]) #t41
  
  CNOT | (T[0], T[11])
  CNOT | (T[9], T[11]) #t42

  CNOT | (T[0], T[12])
  CNOT | (T[3], T[12]) #t43
  
  CNOT | (T[9], T[13])
  CNOT | (T[1], T[13]) #t44
  
  CNOT | (T[11], T[14])
  CNOT | (T[8], T[14]) #t45
  
  CNOT | (U[0], U[2])
  CNOT | (U[1], U[2])
  CNOT | (U[6], U[2]) #for z16
  
  CNOT | (U[1], U[4])
  CNOT | (U[3], U[4])
  CNOT | (U[5], U[4]) #for z1
  
  CNOT | (U[1], U[6])
  CNOT | (U[3], U[6])
  CNOT | (U[4], U[6])
  CNOT | (U[5], U[6])
  CNOT | (U[7], U[6]) #for z11
  
  CNOT | (U[1], U[0])
  CNOT | (U[3], U[0]) #for z13
  
  CNOT | (U[0], U[3])
  CNOT | (U[2], U[3])
  CNOT | (U[6], U[3]) #for z14

Toffoli | (T[0], U[3], S[2]) #z14

CNOT | (S[2], S[5])
CNOT | (U[0], U[3])
Toffoli | (T[12], U[3], S[6]) #z12

CNOT | (S[6], S[2])
CNOT | (S[6], S[5])
CNOT | (U[0], U[3])
Toffoli | (T[1], U[4], S[1]) #z1

CNOT | (S[1], S[3])
CNOT | (S[1], S[4])
CNOT | (U[7], U[4])
Toffoli | (T[13], U[4], S[7]) #z0

CNOT | (S[7], S[1])
CNOT | (S[7], S[2])
CNOT | (S[7], S[3])
CNOT | (S[7], S[5])
CNOT | (U[7], U[4])
Toffoli | (T[3], U[0], S[6]) #z13

CNOT | (S[6], S[7])
CNOT | (U[3], U[6])
Toffoli | (T[11], U[6], S[0]) #z15

CNOT | (S[0], S[2])
CNOT | (U[3], U[6])
Toffoli | (T[14], U[2], S[0]) #z16

CNOT | (S[0], S[1])
CNOT | (S[0], S[3])
CNOT | (S[0], S[4])
CNOT | (S[0], S[5])
CNOT | (S[0], S[6])
CNOT | (S[0], S[7])
Toffoli | (T[9], U[7], Z[0]) #z2

CNOT | (Z[0], S[2])
CNOT | (Z[0], S[4])
CNOT | (Z[0], S[5])
CNOT | (Z[0], S[7])
Toffoli | (T[9], U[7], Z[0])

with Compute(eng):
  CNOT | (U[0], U[5])
  CNOT | (U[3], U[5])
  Toffoli | (T[12], U[5], Z[0]) #z3
CNOT | (Z[0], S[0])
CNOT | (Z[0], S[3])
CNOT | (Z[0], S[5])
CNOT | (Z[0], S[7])
Uncompute(eng)

with Compute(eng):
  CNOT | (U[1], U[6])
  CNOT | (U[2], U[6])
  CNOT | (U[3], U[6])
  CNOT | (U[4], U[6])
  Toffoli | (T[3], U[6], Z[0]) #z4
CNOT | (Z[0], S[0])
CNOT | (Z[0], S[3])
CNOT | (Z[0], S[4])
CNOT | (Z[0], S[5])
CNOT | (Z[0], S[6])
Uncompute(eng)

with Compute(eng):
  CNOT | (U[0], U[6])
  CNOT | (U[1], U[6])
  CNOT | (U[2], U[6])
  CNOT | (U[4], U[6])
  CNOT | (U[5], U[6])
  Toffoli | (T[0], U[6], Z[0]) #z5
CNOT | (Z[0], S[4])
CNOT | (Z[0], S[6])
CNOT | (Z[0], S[7])
Uncompute(eng)

with Compute(eng):
  CNOT | (U[0], U[7])
  CNOT | (U[1], U[7])
  CNOT | (U[2], U[7])
  CNOT | (U[4], U[7])
  CNOT | (U[5], U[7])
  CNOT | (U[6], U[7])
  Toffoli | (T[11], U[7], Z[0]) #z6
CNOT | (Z[0], S[0])
CNOT | (Z[0], S[1])
CNOT | (Z[0], S[2])
Uncompute(eng)

with Compute(eng):
  CNOT | (U[0], U[7])
  CNOT | (U[3], U[7])
  CNOT | (U[4], U[7])
  CNOT | (U[5], U[7])
  Toffoli | (T[14], U[7], Z[0]) #z7
CNOT | (Z[0], S[0])
CNOT | (Z[0], S[1])
CNOT | (Z[0], S[5])
CNOT | (Z[0], S[6])
Uncompute(eng)

with Compute(eng):
  CNOT | (U[1], U[6])
  CNOT | (U[2], U[6])
  CNOT | (U[3], U[6])
  Toffoli | (T[8], U[6], Z[0]) #z8
CNOT | (Z[0], S[2])
CNOT | (Z[0], S[5])
CNOT | (Z[0], S[6])
Uncompute(eng)

with Compute(eng):
  CNOT | (U[0], U[3])
  CNOT | (U[2], U[3])
  Toffoli | (T[13], U[3], Z[0]) #z9
CNOT | (Z[0], S[0])
CNOT | (Z[0], S[1])
CNOT | (Z[0], S[3])
CNOT | (Z[0], S[4])
Uncompute(eng)

with Compute(eng):
  CNOT | (U[0], U[6])
  CNOT | (U[2], U[6])
  CNOT | (U[3], U[6])
  Toffoli | (T[1], U[6], Z[0]) #z10
CNOT | (Z[0], S[0])
CNOT | (Z[0], S[1])
CNOT | (Z[0], S[3])
CNOT | (Z[0], S[4])
CNOT | (Z[0], S[5])
Uncompute(eng)

CNOT | (U[2], U[6])
CNOT | (U[3], U[6])
Toffoli | (T[8], U[6], S[2]) #z17
CNOT | (U[3], U[6])
CNOT | (U[2], U[6])

Toffoli | (T[9], U[6], S[5]) #z11

X | S[1]
X | S[2]
X | S[6]
X | S[7]

Uncompute(eng)
