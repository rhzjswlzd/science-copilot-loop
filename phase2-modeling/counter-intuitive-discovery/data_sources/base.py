"""
Base Dataset Interface for Counter-Intuitive Feature Discovery

All dataset plugins must inherit from this abstract class and implement
the required methods to ensure compatibility with the experimental framework.
"""

from abc import ABC, abstractmethod
from typing import List, Dict, Any
import pandas as pd
import numpy as np


class BaseDataset(ABC):
    """
    Abstract base class for dataset plugins.
    
    Each dataset plugin encapsulates domain-specific knowledge:
    - How to load and preprocess raw data
    - How to extract features
    - Which features are "conventional" (to be blocked in experiments)
    """
    
    def __init__(self, config: Dict[str, Any]):
        """
        Initialize dataset with configuration.
        
        Args:
            config: Dictionary containing dataset-specific parameters
                   (e.g., file paths, preprocessing options)
        """
        self.config = config
        self.data = None
        self.features = None
        self.target = None
    
    @abstractmethod
    def load_raw_data(self) -> pd.DataFrame:
        """
        Load raw data from source (files, database, API, etc.).
        
        Returns:
            DataFrame containing raw data
        """
        pass
    
    @abstractmethod
    def extract_features(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Perform feature engineering on raw data.
        
        This method should implement all domain-specific transformations:
        - Statistical aggregations
        - Frequency-domain features
        - Shape descriptors
        - Derivative features
        
        Args:
            df: Raw data DataFrame
            
        Returns:
            DataFrame with extracted features (samples × features)
        """
        pass
    
    @abstractmethod
    def get_target(self, df: pd.DataFrame) -> np.ndarray:
        """
        Extract target variable from data.
        
        Args:
            df: DataFrame (can be raw or processed)
            
        Returns:
            1D numpy array of target values
        """
        pass
    
    @abstractmethod
    def label_conventional_features(self) -> List[str]:
        """
        Identify which features are "conventional engineering metrics".
        
        These are features that domain experts typically prioritize:
        - Direct physical measurements (e.g., capacity, resistance)
        - Well-known correlates (e.g., temperature, voltage)
        
        In blocked experiments, these features will be removed to force
        the model to discover non-intuitive patterns.
        
        Returns:
            List of feature names considered "conventional"
        """
        pass
    
    def get_feature_metadata(self) -> Dict[str, str]:
        """
        Optional: Provide descriptions for features.
        
        Returns:
            Dictionary mapping feature names to descriptions/units
        """
        return {}
    
    def prepare(self):
        """
        Full data preparation pipeline (convenience method).
        
        Calls load_raw_data -> extract_features -> get_target in sequence
        and stores results in instance variables.
        """
        raw = self.load_raw_data()
        self.features = self.extract_features(raw)
        self.target = self.get_target(raw)
        return self
