#!/usr/bin/env python3
# -*- coding: utf-8 -*-
### https://medium.com/dunder-data/selecting-subsets-of-data-in-pandas-6fcd0170be9c
### http://3480-3590-data-conversion.com/article-reading-cobol-layouts-4.html    
### http://www.ibmmainframeforum.com/ibm-cobol/topic11747.html
### https://datatofish.com/round-values-pandas-dataframe/
import pandas as  pd
import sys, traceback
import numpy as np
import pandas as pd

pd.options.display.max_columns = None


class FixedLengthField( ):
    
    ##TODO assert that values are correct
    def __init__(self, name=None, data_type=None, start=None, length=None, decimals=None ):
        self.name = name
        self.data_type = data_type
        self.start=start
        self.length = length
        self.decimals = ( decimals if (decimals is not None) else 0 )
        self.values = []
    
    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)
        # ~ return "member of Test"
    
    ## TODO implement special negative indicators
    def append_value( self, line ):
        string = line[self.start:self.start+self.length+self.decimals]
                    
        # ~ print( string )
        if( self.data_type == 'X' ):
            ## Strip will remove the padding spaces
            self.values.append( string.strip() )
        else:
            # ~ print( self.name, string )
            if( self.decimals == 0 ):
                self.values.append( int( string ) )
            else:
                self.values.append(  float( string )  / ( 10 ** self.decimals ) )

class FixedLengthDataFrame(  ):
    def __init__( self, fixed_length_data_fields=None, file_name=None ):

        if( fixed_length_data_fields is not None ):
            self.fixed_length_data_fields = fixed_length_data_fields
        else:
            self.fixed_length_data_fields = []
            
        if( file_name is not None ):
            self.load_data( file_name )
                
    def load_data( self, file_name ):
        with open ( file_name ) as data_file:
            for line in data_file:
                start = 0
                line.strip()
                for field in self.fixed_length_data_fields:
                    field.append_value( line )
    def convert_to_pandas_data_frame( self ):
        pandas_data_frame = pd.DataFrame()
        for field in self.fixed_length_data_fields:
            pandas_data_frame[ field.name ] = field.values
        return pandas_data_frame
