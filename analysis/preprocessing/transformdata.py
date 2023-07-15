def transformdata(datapath):

    # Libraries

    import pandas as pd

    # Import data

    rawdata = pd.read_csv(datapath)
    rawdata = data.rename(columns={"subj":"subject", "rxn_time":"rt"})
    
    # Return
    
    return(rawdata)