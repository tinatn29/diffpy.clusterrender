"""This module defines class ClusterDataFrame.

A local structure or cluster of atoms is represented in a DataFrame
format.
"""

import pandas as pd

# -------------------------


class ClusterDataFrame(pd.DataFrame):
    """Define a cluster of atoms in a pandas DataFrame format.

    Each row corresponds to an atom, and columns represent
    atomic properties: species, xyz coordinates, and (optionally)
    coordination shells, specifying the central atom (0) and its
    neighboring atoms (1, 2, ...).

    Methods
    -------
    parse_structure(structure_input, site_index=0)
        Parse structure data from a structure, a file, a dictionary,
        or a DataFrame into ClusterDataFrame.

    Attributes
    ----------
    _constructor : property
        Ensures that DataFrame operations return ClusterDataFrame objects.
    """

    @property
    def _constructor(self):
        return ClusterDataFrame

    def __init__(self, structure_input, site_index=0):
        """Initialize ClusterDataFrame from a Structure object, a file,
        or generic DataFrame arguments.

        Parameters
        ----------
        structure_input : pymatgen.core.Structure, pathlib.Path, str,
        dict, or pd.DataFrame
            The input structure or cluster of atoms to be visualized.
        site_index : int, optional
            The index of atom in the structure to be treated as the
            central atom.
            Default is 0.
        """
        # parse and load structure_input
        self._parse_structure(structure_input, site_index)
