#!/usr/bin/env python3
# -*- coding: utf-8 -*-
### https://medium.com/dunder-data/selecting-subsets-of-data-in-pandas-6fcd0170be9c
### http://3480-3590-data-conversion.com/article-reading-cobol-layouts-4.html    
### http://www.ibmmainframeforum.com/ibm-cobol/topic11747.html
### https://datatofish.com/round-values-pandas-dataframe/
from FixedLengthData import *

def main():
    #TODO signal manipulation
    #TODO filter/mask
    #TODO date time types
    #TODO extend Pandas DataFrame
    try:
        
        
        
        fixed_length_data_frame = FixedLengthDataFrame( 
            fixed_length_data_fields = [
                FixedLengthField( 'data_pregao', '9', 2, 8, 0 )
                , FixedLengthField( 'codigo_negociacao', 'X', 12, 12, 0 )
                , FixedLengthField( 'preco_ultimo', '9', 108, 11, 2 )
            ]
            , file_name = sys.argv[1] 
            
        )
        
        print( fixed_length_data_frame.convert_to_pandas_data_frame() )
        
    except: 
        traceback.print_exc() 

        
if __name__ == "__main__":
    
    main()

