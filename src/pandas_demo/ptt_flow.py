import glob

import pandas as pd

COLUMNS = ['推',
'噓',
'分數',
'作者',
'標題',
'時間']

def get_paths() -> list[str]:
    return glob.glob('/workspaces/demo-devcontainer-main/res_gossiping/*.txt')

def e_text_file(path: str) -> str:
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def t_text_to_df_row_list(artical_str: str) -> list[str]:
    reply_info_str = artical_str.split('---split---')[1]
    return reply_info_str.split('\n')[1:-1]

def t_combine_list_to_df(reply_info_list: list[list]) -> pd.DataFrame:
    return pd.DataFrame(columns=COLUMNS, data = reply_info_list)

def l_df_to_csv(df: pd.DataFrame) -> None:
    df.to_csv('ptt.csv', index=False)



if __name__ == '__main__':
    # get paths of all text files
    path_list = get_paths()

    # loop for file paths
    data = []
    for path in path_list:
        #extract text files
        artical_str = e_text_file(path)
        # text to list-element in df
        reply_info_list = t_text_to_df_row_list(artical_str)
        data.append(reply_info_list)
    # concat lists to df
    df = t_combine_list_to_df(data)

    # load df to csv
    l_df_to_csv(df)