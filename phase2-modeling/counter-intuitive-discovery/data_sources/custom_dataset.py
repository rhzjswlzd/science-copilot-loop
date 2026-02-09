"""
Custom Dataset Template

Copy this file and implement the required methods for your own dataset.
"""

from typing import List
import pandas as pd
import numpy as np
from .base import BaseDataset


class CustomDataset(BaseDataset):
    """
    Template for creating your own dataset plugin.
    
    Steps to use:
    1. Copy this file to a new name (e.g., my_material_dataset.py)
    2. Implement the four required methods below
    3. Update the config YAML to point to your plugin
    """
    
    def load_raw_data(self) -> pd.DataFrame:
        """
        Load your raw data here.
        
        Examples:
        - pd.read_csv(self.config['data_path'])
        - Load from JSON, HDF5, database, API, etc.
        """
        raise NotImplementedError("Implement data loading logic")
    
    def extract_features(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Engineer features from raw data.
        
        Tips:
        - Use meaningful column names
        - Document physical units
        - Consider both raw signals and derived statistics
        """
        raise NotImplementedError("Implement feature engineering")
    
    def get_target(self, df: pd.DataFrame) -> np.ndarray:
        """
        Return the target variable (what you want to predict).
        
        Example:
            return df['performance_metric'].values
        """
        raise NotImplementedError("Specify target variable")
    
    def label_conventional_features(self) -> List[str]:
        """
        List features that domain experts typically rely on.
        
        These are the "obvious" metrics that will be blocked in experiments
        to force discovery of hidden patterns.
        
        Examples:
        - For materials: composition, synthesis temperature
        - For catalysts: surface area, pore volume
        - For reactions: yield, conversion rate
        """
        raise NotImplementedError("Label conventional features")
