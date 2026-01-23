"""This module defines class StructureDF.

A local structure or cluster of atoms is represented in a DataFrame
format.
"""

import pandas as pd
from pymatgen.core import Structure

# -------------------------


class StructureDF(pd.DataFrame):
    """Define a structure or cluster of atoms in a pandas DataFrame
    format. Each row corresponds to an atom, and columns represent
    atomic properties: species, xyz coordinates, and (optionally)
    coordination shells, specifying the central atom (0) and its
    neighboring atoms (1, 2, ...).

    Parameters
    ----------
    structure : pymatgen.core.Structure, optional
        A Structure object from pymatgen.core to initialize the DataFrame.
    filename : str, optional
        Path to a file to read the structure (or cluster) from.
        Accepted file formats include cif and xyz.
    """

    def __init__(self, structure=None, site_index=None, filename=None):
        # load from Structure object if provided
        if isinstance(structure, Structure):
            self._from_structure(structure, site_index)
            return
        # load from file if a filename is provided (without a Structure)
        elif filename is not None:
            self._from_file(filename, site_index)
            return
        else:
            raise ValueError("Either structure or filename must be provided.")
