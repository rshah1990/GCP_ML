import numpy as np 
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

#Custom Transformer that extracts columns passed as argument to its constructor 
class FeatureSelector( BaseEstimator, TransformerMixin ):
    #Class Constructor 
    def __init__( self, feature_names ):
        self.feature_names = feature_names 
    
    #Return self nothing else to do here    
    def fit( self, X, y = None ):
        return self 
    
    #Method that describes what we need this transformer to do
    def transform( self, X, y = None ):
        return X[ self.feature_names] 
    
class categorical_transform(BaseEstimator,TransformerMixin):
    # constructore method
    def __init__(self,use_date=['year','month','day']):
        self.use_date = use_date
        
    # return self in fit as nothing else need to be done here 
    def fit(self,X,y=None):
        return self
    
    # create helper functions to extract year,month & day from the string
    
    def get_year(self,obj):
        return str(obj)[:4]
    
    def get_month(self,obj):
        return str(obj)[4:6]
    
    def get_day(self,obj):
        return str(obj)[6:8]
    
    # helper function to create binary on input
    
    def create_binary(self,obj):
        if obj == 0:
            return 'No'
        else:
            return 'Yes'
    
    def transform(self,X,y=None):
        # depending on the argument create new columns for date 
        for spec in self.use_date:
            exec( "X.loc[:,'{}'] = X['date'].apply(self.get_{})".format( spec, spec ) )
        
        X =X.drop('date',axis=1)
        X.loc[:,'waterfront'] = X['waterfront'].apply(self.create_binary)
        X.loc[:,'view'] = X['view'].apply( self.create_binary ) 
        X.loc[:,'yr_renovated'] = X['yr_renovated'].apply( self.create_binary )
        return X.values 
    
class numerical_transform(BaseEstimator,TransformerMixin):
    # class constrctor
    def __init__(self,bath_per_bed = True, years_old = True):
        self._bath_per_bed = bath_per_bed
        self._years_old = years_old
    
    def fit(self,X,y=None):
        return self
    
    def transform(self,X,y=None):
        if self._bath_per_bed:
            X.loc[:,'bath_per_bed'] = X['bathrooms'] / X['bedrooms']
            X.drop('bathrooms', axis = 1 )
            
        #Check if needed     
        if self._years_old:
            #create new column
            X.loc[:,'years_old'] =  2019 - X['yr_built']
            #drop redundant column 
            X.drop('yr_built', axis = 1)
        
        X = X.replace( [ np.inf, -np.inf ], np.nan )
        return X.values