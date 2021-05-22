from qiskit import *
from qiskit.visualization import matplotlib

IBMQ.save_account('c695948acddb2a06dfaa5f4c5769ec3acca95a30876d3dc0840c8aed9521fd692009b8aa91e67697ebb796896700630c78c2ba7d36891dcb62268bf832c14880')
print(IBMQ.load_account())
qr = QuantumRegister(2)
cr = ClassicalRegister(2)
circuit = QuantumCircuit(qr, cr)
%matplotlib inline
circuit.draw()
