"""
Battery Dataset Plugin (Example Template)

This is a template for loading battery lifecycle data.
Users should adapt this to their specific data format.
"""

from typing import List
import pandas as pd
import numpy as np
from .base import BaseDataset


class BatteryDataset(BaseDataset):
    """
    Example plugin for battery cycle life prediction datasets.
    
    Expected config keys:
        - data_path: str, path to data files
        - test_size: float, train/test split ratio
        - (add more as needed)
    """
    
    def load_raw_data(self) -> pd.DataFrame:
        """
        Load battery data from disk.
        
        TODO: Implement actual data loading logic based on your format
        (JSON, CSV, HDF5, etc.)
        """
        data_path = self.config.get('data_path')
        # Placeholder implementation
        # Replace with actual data loading code
        raise NotImplementedError(
            "Please implement load_raw_data() for your specific data format"
        )
    
    def extract_features(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Extract features from battery cycling data.
        
        Common features for battery datasets:
        - Differential capacity (dQ/dV) statistics
        - Voltage curve descriptors
        - Temperature trends
        - Internal resistance evolution
        
        TODO: Implement your feature engineering pipeline
        """
        raise NotImplementedError(
            "Please implement extract_features() for your dataset"
        )
    
    def get_target(self, df: pd.DataFrame) -> np.ndarray:
        """
        Extract target variable (e.g., cycle life).
        
        TODO: Specify which column contains the target
        """
        # Example:
        # return df['cycle_life'].values
        raise NotImplementedError(
            "Please implement get_target() for your dataset"
        )
    
    def label_conventional_features(self) -> List[str]:
        """
        Label conventional battery engineering metrics.
        
        Examples of conventional features:
        - Rated capacity
        - Internal resistance (DC or AC)
        - Temperature (mean, max, min)
        - Charge/discharge time
        - Capacity fade at cycle N
        
        These will be blocked in experiments to discover hidden patterns.
        """
        return [
            'rated_capacity',
            'internal_resistance',
            'temperature_mean',
            'charge_time',
            'capacity_fade_100',
            # Add more conventional features here
        ]
    
    def get_feature_metadata(self) -> dict:
        """
        Optional: Provide feature descriptions.
        """
        return {
            'rated_capacity': 'Nominal battery capacity (Ah)',
            'internal_resistance': 'DC internal resistance at 50% SOC (mΩ)',
            'temperature_mean': 'Average cycling temperature (°C)',
            # ...
        }
