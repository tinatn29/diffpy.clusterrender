import pandas as pd
import pytest

from diffpy.clusterrender.clusterdataframe import ClusterDataFrame

"""
Tests for the ClusterDataFrame class.
"""
# set up test data
dict_input = {
    "species": ["C", "O", "O"],
    "x": [0.0, 1.0, -1.0],
    "y": [0.0, 0.0, 0.0],
    "z": [0.0, 0.0, 0.0],
}
df_input = pd.DataFrame(dict_input)

# basic outputs (specifying center but not coordination shells)
output_C0 = pd.DataFrame(
    {
        "species": ["C", "O", "O"],
        "x": [0.0, 1.0, -1.0],
        "y": [0.0, 0.0, 0.0],
        "z": [0.0, 0.0, 0.0],
        "shell": [0, None, None],
    }
)
output_O1 = pd.DataFrame(
    {
        "species": ["O", "C", "O"],
        "x": [0.0, -1.0, -2.0],
        "y": [0.0, 0.0, 0.0],
        "z": [0.0, 0.0, 0.0],
        "shell": [0, None, None],
    }
)

test_data = [
    # (input, expected_output) or
    # (input, test_index, expected_output)
    # basic inputs: read from dict or DataFrame
    # without any changes
    (dict_input, df_input),
    (df_input, df_input),
    # with site_index specified
    (dict_input, 0, df_input),
    (dict_input, 1, output_O1),
]


@pytest.mark.parametrize("input_test_data", test_data)
def test_clusterdataframe(input_test_data):
    """Test ClusterDataFrame initialization and parsing."""
    if len(input_test_data) == 2:
        input_structure, expected_output = input_test_data
        cdf = ClusterDataFrame(input_structure)
    else:
        input_structure, site_index, expected_output = input_test_data
        cdf = ClusterDataFrame(input_structure, site_index=site_index)

    # check if the output matches the expected DataFrame
    pd.testing.assert_frame_equal(
        cdf.reset_index(drop=True), expected_output.reset_index(drop=True)
    )
