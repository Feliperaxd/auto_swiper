import json, os
from pathlib import Path
from typing import Any, List, Union


class Utils:


    @staticmethod
    def rename_like_last(
        directory: Union[Path, str],
        file_name: str,
        file_extension: str
    ) -> str:
        
        n_in_directory = len(os.listdir(directory))
        return f'{file_name}_{n_in_directory}{file_extension}'

    @staticmethod   
    def save_data(
        data: Any,
        data_key: Union[str, List[str]],
        file_path: Union[Path, str] 
    ) -> None:
        
        with open(file_path, 'r+') as file:
            all_data = json.load(file)

            if isinstance(data_key, list):
                for key in data_key[:-1]:
                    cursor = all_data[key]  
                cursor[data_key[-1]] = data
                all_data[data_key[0]] = cursor

            elif isinstance(data_key, str):
                all_data[data_key] = data

            file.seek(0)
            file.truncate()
            json.dump(all_data, file)

    @staticmethod
    def get_data(
        data_key: Union[str, List[str]],
        file_path: Union[Path, str] 
    ) -> Any:
        
        with open(file_path, 'r') as file:
            all_data = json.load(file)

            if isinstance(data_key, list):
                for key in data_key[:-1]:
                    cursor = all_data[key]  
                data = cursor[data_key[-1]]
                
            elif isinstance(data_key, str):
                data = all_data[data_key]
            
        return data   
        