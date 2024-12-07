#AGUA

from rdkit import Chem
from rdkit.Chem import AllChem
import py3Dmol

smiles = "O"
mol = Chem.MolFromSmiles(smiles)
mol = Chem.AddHs(mol)
AllChem.EmbedMolecule(mol, AllChem.ETKDG())

block = Chem.MolToMolBlock(mol)

view = py3Dmol.view(width=400, height=400)
view.addModel(block, "mol")
view.setStyle({'stick': {}})
view.zoomTo()
view.show()

#ETANOL

from rdkit import Chem
from rdkit.Chem import AllChem
import py3Dmol

smiles = "CCO"
mol = Chem.MolFromSmiles(smiles)
mol = Chem.AddHs(mol)
AllChem.EmbedMolecule(mol, AllChem.ETKDG()) 

block = Chem.MolToMolBlock(mol)

view = py3Dmol.view(width=400, height=400)
view.addModel(block, "mol")
view.setStyle({'stick': {}})
view.zoomTo()
view.show()

#CICLOHEXANO

from rdkit import Chem
from rdkit.Chem import AllChem
import py3Dmol

smiles = "C1CCCCC1"
mol = Chem.MolFromSmiles(smiles)
mol = Chem.AddHs(mol)
AllChem.EmbedMolecule(mol, AllChem.ETKDG())

block = Chem.MolToMolBlock(mol)

view = py3Dmol.view(width=400, height=400)
view.addModel(block, "mol")
view.setStyle({'stick': {}})
view.zoomTo()
view.show()

#ACIDO ACETICO

from rdkit import Chem
from rdkit.Chem import AllChem
import py3Dmol

smiles = "CC(=O)O"
mol = Chem.MolFromSmiles(smiles)
mol = Chem.AddHs(mol)
AllChem.EmbedMolecule(mol, AllChem.ETKDG())

block = Chem.MolToMolBlock(mol)

view = py3Dmol.view(width=400, height=400)
view.addModel(block, "mol")
view.setStyle({'stick': {}})
view.zoomTo()
view.show()

#BENCENO

from rdkit import Chem
from rdkit.Chem import AllChem
import py3Dmol

smiles = "C1=CC=CC=C1"
mol = Chem.MolFromSmiles(smiles)
mol = Chem.AddHs(mol)
AllChem.EmbedMolecule(mol, AllChem.ETKDG()) 

block = Chem.MolToMolBlock(mol)

view = py3Dmol.view(width=400, height=400)
view.addModel(block, "mol")
view.setStyle({'stick': {}})
view.zoomTo()
view.show()

#METANO

from rdkit import Chem
from rdkit.Chem import AllChem
import py3Dmol

smiles = "C"
mol = Chem.MolFromSmiles(smiles)
mol = Chem.AddHs(mol)
AllChem.EmbedMolecule(mol, AllChem.ETKDG()) 

block = Chem.MolToMolBlock(mol)

view = py3Dmol.view(width=400, height=400)
view.addModel(block, "mol")
view.setStyle({'stick': {}})
view.zoomTo()
view.show()

#METANOL

from rdkit import Chem
from rdkit.Chem import AllChem
import py3Dmol

smiles = "CO"
mol = Chem.MolFromSmiles(smiles)
mol = Chem.AddHs(mol)
AllChem.EmbedMolecule(mol, AllChem.ETKDG())

block = Chem.MolToMolBlock(mol)

view = py3Dmol.view(width=400, height=400)
view.addModel(block, "mol")
view.setStyle({'stick': {}})
view.zoomTo()
view.show()

#ETANO

from rdkit import Chem
from rdkit.Chem import AllChem
import py3Dmol

smiles = "CC"
mol = Chem.MolFromSmiles(smiles)
mol = Chem.AddHs(mol)
AllChem.EmbedMolecule(mol, AllChem.ETKDG())

block = Chem.MolToMolBlock(mol)

view = py3Dmol.view(width=400, height=400)
view.addModel(block, "mol")
view.setStyle({'stick': {}})
view.zoomTo()
view.show()

#PROPANO

from rdkit import Chem
from rdkit.Chem import AllChem
import py3Dmol

smiles = "CCC"
mol = Chem.MolFromSmiles(smiles)
mol = Chem.AddHs(mol)
AllChem.EmbedMolecule(mol, AllChem.ETKDG()) 

block = Chem.MolToMolBlock(mol)

view = py3Dmol.view(width=400, height=400)
view.addModel(block, "mol")
view.setStyle({'stick': {}})
view.zoomTo()
view.show()

#BUTANO

from rdkit import Chem
from rdkit.Chem import AllChem
import py3Dmol

smiles = "CCCC"
mol = Chem.MolFromSmiles(smiles)
mol = Chem.AddHs(mol)
AllChem.EmbedMolecule(mol, AllChem.ETKDG()) 

block = Chem.MolToMolBlock(mol)

view = py3Dmol.view(width=400, height=400)
view.addModel(block, "mol")
view.setStyle({'stick': {}})
view.zoomTo()
view.show()
#ACETONA

from rdkit import Chem
from rdkit.Chem import AllChem
import py3Dmol

smiles = "CC(=O)C"
mol = Chem.MolFromSmiles(smiles)
mol = Chem.AddHs(mol)
AllChem.EmbedMolecule(mol, AllChem.ETKDG()) 

block = Chem.MolToMolBlock(mol)

view = py3Dmol.view(width=400, height=400)
view.addModel(block, "mol")
view.setStyle({'stick': {}})
view.zoomTo()
view.show()

#GLICINA

from rdkit import Chem
from rdkit.Chem import AllChem
import py3Dmol

smiles = "C(C(=O)O)N"
mol = Chem.MolFromSmiles(smiles)
mol = Chem.AddHs(mol)
AllChem.EmbedMolecule(mol, AllChem.ETKDG()) 

block = Chem.MolToMolBlock(mol)

view = py3Dmol.view(width=400, height=400)
view.addModel(block, "mol")
view.setStyle({'stick': {}})
view.zoomTo()
view.show()

#ALANINA

from rdkit import Chem
from rdkit.Chem import AllChem
import py3Dmol

smiles = "CC(C(=O)O)N"
mol = Chem.MolFromSmiles(smiles)
mol = Chem.AddHs(mol)
AllChem.EmbedMolecule(mol, AllChem.ETKDG())

block = Chem.MolToMolBlock(mol)

view = py3Dmol.view(width=400, height=400)
view.addModel(block, "mol")
view.setStyle({'stick': {}})
view.zoomTo()
view.show()

#FENOL

from rdkit import Chem
from rdkit.Chem import AllChem
import py3Dmol

smiles = "C1=CC=C(C=C1)O"
mol = Chem.MolFromSmiles(smiles)
mol = Chem.AddHs(mol)
AllChem.EmbedMolecule(mol, AllChem.ETKDG())

block = Chem.MolToMolBlock(mol)

view = py3Dmol.view(width=400, height=400)
view.addModel(block, "mol")
view.setStyle({'stick': {}})
view.zoomTo()
view.show()

#TETRAHIDROFURANO

from rdkit import Chem
from rdkit.Chem import AllChem
import py3Dmol

smiles = "C1CCOC1"
mol = Chem.MolFromSmiles(smiles)
mol = Chem.AddHs(mol)
AllChem.EmbedMolecule(mol, AllChem.ETKDG())

block = Chem.MolToMolBlock(mol)

view = py3Dmol.view(width=400, height=400)
view.addModel(block, "mol")
view.setStyle({'stick': {}})
view.zoomTo()
view.show()

#ETANOLAMINA

from rdkit import Chem
from rdkit.Chem import AllChem
import py3Dmol

smiles = "NCCO"
mol = Chem.MolFromSmiles(smiles)
mol = Chem.AddHs(mol)
AllChem.EmbedMolecule(mol, AllChem.ETKDG())  

block = Chem.MolToMolBlock(mol)

view = py3Dmol.view(width=400, height=400)
view.addModel(block, "mol")
view.setStyle({'stick': {}})
view.zoomTo()
view.show()

#ACIDO ASPARTICO (AMINOACIDO)

from rdkit import Chem
from rdkit.Chem import AllChem
import py3Dmol

smiles = "C(C(=O)O)(N)C(=O)O"
mol = Chem.MolFromSmiles(smiles)
mol = Chem.AddHs(mol)
AllChem.EmbedMolecule(mol, AllChem.ETKDG())

block = Chem.MolToMolBlock(mol)

view = py3Dmol.view(width=400, height=400)
view.addModel(block, "mol")
view.setStyle({'stick': {}})
view.zoomTo()
view.show()

#TRIETILAMINA

from rdkit import Chem
from rdkit.Chem import AllChem
import py3Dmol

smiles = "CCN(CC)CC"
mol = Chem.MolFromSmiles(smiles)
mol = Chem.AddHs(mol)
AllChem.EmbedMolecule(mol, AllChem.ETKDG()) 

block = Chem.MolToMolBlock(mol)

view = py3Dmol.view(width=400, height=400)
view.addModel(block, "mol")
view.setStyle({'stick': {}})
view.zoomTo()
view.show()

#DIETIL ETER

from rdkit import Chem
from rdkit.Chem import AllChem
import py3Dmol

smiles = "CCOCC"
mol = Chem.MolFromSmiles(smiles)
mol = Chem.AddHs(mol)
AllChem.EmbedMolecule(mol, AllChem.ETKDG())  

block = Chem.MolToMolBlock(mol)

view = py3Dmol.view(width=400, height=400)
view.addModel(block, "mol")
view.setStyle({'stick': {}})
view.zoomTo()
view.show()

#ACIDO LACTICO 

from rdkit import Chem
from rdkit.Chem import AllChem
import py3Dmol

smiles = "C(C(=O)O)O"
mol = Chem.MolFromSmiles(smiles)
mol = Chem.AddHs(mol)
AllChem.EmbedMolecule(mol, AllChem.ETKDG())

block = Chem.MolToMolBlock(mol)

view = py3Dmol.view(width=400, height=400)
view.addModel(block, "mol")
view.setStyle({'stick': {}})
view.zoomTo()
view.show()

#NAFTALENO

from rdkit import Chem
from rdkit.Chem import AllChem
import py3Dmol

smiles = "C1=CC=C2C=CC=CC2=C1"
mol = Chem.MolFromSmiles(smiles)
mol = Chem.AddHs(mol)
AllChem.EmbedMolecule(mol, AllChem.ETKDG())  

block = Chem.MolToMolBlock(mol)

view = py3Dmol.view(width=400, height=400)
view.addModel(block, "mol")
view.setStyle({'stick': {}})
view.zoomTo()
view.show()

#DIMETILFORMAMINA

from rdkit import Chem
from rdkit.Chem import AllChem
import py3Dmol

smiles = "CN(C)C=O"
mol = Chem.MolFromSmiles(smiles)
mol = Chem.AddHs(mol)
AllChem.EmbedMolecule(mol, AllChem.ETKDG())

block = Chem.MolToMolBlock(mol)

iew = py3Dmol.view(width=400, height=400)
view.addModel(block, "mol")
view.setStyle({'stick': {}})
view.zoomTo()
view.show()

#ACIDO CITRICO

from rdkit import Chem
from rdkit.Chem import AllChem
import py3Dmol

smiles = "C(C(=O)O)(C(=O)O)C(=O)O"
mol = Chem.MolFromSmiles(smiles)
mol = Chem.AddHs(mol)
AllChem.EmbedMolecule(mol, AllChem.ETKDG())

block = Chem.MolToMolBlock(mol)

view = py3Dmol.view(width=400, height=400)
view.addModel(block, "mol")
view.setStyle({'stick': {}})
view.zoomTo()
view.show()
