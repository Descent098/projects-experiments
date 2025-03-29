from threading import Lock
Any = object

class ConcurrentDict:
    def __init__(self, fields:list[list[Any, Any]]):
        """A thread-safe dictionary that locks values

        Parameters
        ----------
        fields : list[list[Any, Any]]
            A list of fields to initialize in [key, value] pairs, by default None

        Examples
        --------
        ### Basic Usage
        ```
        a = ConcurrentDict([["key","value"], ["key2", "value2"]])
        
        # Getting a value
        print(a["key"]) # Prints "value"
        
        # Setting values
        a["key3"] = "value3" # New value
        a["key"] = "value1"  # Updating old one
        
        print(a["key"]) # Prints "value1"
        print(a["key3"]) # Prints "value3"
        ```
        
        """
        self._items = dict()
        if not fields: # Nothing to add
            return
        
        for [field_label, field_value] in fields:
            self._items[field_label] = {"value": field_value, "mutex": Lock()}
        
    def __getitem__(self, label:Any) -> Any:
        """Gets an item from the underlying dict

        Parameters
        ----------
        label : Any
            The label of the item to get

        Returns
        -------
        Any
            The value of the item based on the label
            
        Examples
        --------
        ### Getting an item
        
        ```
        a = ConcurrentDict([["key","value"], ["key2", "value2"]])
        
        print(a["key"]) # Prints "value"
        ``` 
        """
        mutex = self._items[label]["mutex"]
        with mutex:
            val = self._items[label]["value"]
        return val
        
        
    def __setitem__(self, label:Any, value:Any):
        """Sets an item to the underlying dict

        Parameters
        ----------
        label : Any
            The label of the item to set (must be Hashable)
        
        value : Any
            The value to set the label to
            
        Examples
        --------
        ### Setting an item
        
        ```
        a = ConcurrentDict([["key","value"], ["key2", "value2"]])
        
        a["key3"] = "value3" # uses __setitem__
        
        print(a["key3"]) # Prints "value3"
        ``` 
        
        ### Resetting an item
        
        ```
        a = ConcurrentDict([["key","value"], ["key2", "value2"]])
        
        a["key"] = "value1" # uses __setitem__
        
        print(a["key"]) # Prints "value1"
        ``` 
        """
        if self._items.get(label, False):
            mutex = self._items[label]["mutex"]
            with mutex:
                self._items[label]["value"] = value
        else:
            self._items[label] = {"value": value, "mutex":Lock()}
    
    def __repr__(self):
        """Function to make printing look nicer
        
        Notes
        -----
        - Printing only shows values, skips showing mutexes for those values
        """
        res = "{"
        for key in self._items:
            res += f"{key}: {self._items[key]['value']}, "
        res = res[:-2]+"}"
        return res
            

if __name__ == "__main__":
    # Testing code
    a = ConcurrentDict([["key","value"], ["key2", "value2"]])
    
    assert a["key"]
    assert a["key2"]
    
    assert a["key"] == "value"
    assert a["key2"] == "value2"
    
    a["key3"] = "value3"
    assert a["key3"]
    assert a["key3"] == "value3"
    
    with a._items["key"]["mutex"]:
        assert a._items["key"]["mutex"].locked()
        
    a["key"] = "value1"
    
    assert a["key"] == "value1"

    print(f"Final state of dict is: {a=}")

    
    
    
    
    