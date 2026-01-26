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

    Methods
    -------
    from_structure(structure, site_index=None)
        Load structure data from a pymatgen Structure object.
    from_file(filename, site_index=None)
        Load structure data from a file.

    Attributes
    ----------
    _constructor : property
        Ensures that DataFrame operations return StructureDF objects.
    """

    @property
    def _constructor(self):
        return StructureDF

    def __init__(
        self, *args, structure=None, site_index=None, filename=None, **kwargs
    ):
        """Initialize StructureDF from a Structure object, a file, or
        generic DataFrame arguments.

        Parameters
        ----------
        structure : pymatgen.core.Structure, optional
            The pymatgen Structure object to load the structure from.
        site_index : int, optional
            The index of atom in the structure to be treated as the
            central atom.
        filename : str, optional
            The path to the structure file.
            Accepted formats include CIF and XYZ.
        *args, **kwargs
            The arguments to initialize a pandas DataFrame with a
            generic pandas constructor.
            Accepted arguments are described in
            https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html.
        """
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
