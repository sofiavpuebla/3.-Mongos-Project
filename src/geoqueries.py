import numpy as np

def TransformGeoPoints(dataFrame):
    """
  
    if np.isnan(dataFrame.lat) or np.isnan(dataFrame.lng):
        return None
    """
    
    return {
    "type":"Point",
    "coordinates":[dataFrame.lng, dataFrame.lat]
    }

def TransformGeo(dataFrame):
  
    if np.isnan(dataFrame.lat) or np.isnan(dataFrame.lng):
        return None

    else:
        return {
    "type":"Point",
    "coordinates":[dataFrame.lng, dataFrame.lat]
    }