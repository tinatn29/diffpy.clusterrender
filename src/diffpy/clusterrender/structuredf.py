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
    *args, **kwargs
        Arguments passed to the pandas DataFrame constructor to initialize
        the DataFrame.
        These are ignored if `structure` or `filename` is provided.
    structure : pymatgen.core.Structure, optional
        A Structure object from pymatgen.core to initialize the DataFrame.
    filename : str, optional
        Path to a file to read the structure (or cluster) from.
        Accepted file formats include cif and xyz.
    site_index : int, optional
        Index of the central atom in the structure.
    """

    def __init__(
        self, *args, structure=None, site_index=None, filename=None, **kwargs
    ):
        # load from Structure object if provided
        if isinstance(structure, Structure):
            self.from_structure(structure, site_index)
            return
        # load from file if a filename is provided (without a Structure)
        elif filename is not None:
            self.from_file(filename, site_index)
            return
        # or try initializing with generic DataFrame arguments
        else:
            super().__init__(*args, **kwargs)
            return
