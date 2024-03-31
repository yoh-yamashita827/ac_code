import sys
import pandas as pd
import string

def main(argv):
    # このコードは引数と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use arguments and outputs.
    # Edit and remove this code as you like.
    form = argv[0]
    file_path = argv[1]

    df = pd.read_csv(file_path)
    # print(df)
    if form == 'dropouts':
        df['drop'] = (df.iloc[:, 1:] <= 49).sum(axis=1)
        drop_id = df[df['drop'] >= 2]['ID']
        output_df = pd.DataFrame({'ID': drop_id})
        print(output_df)

    else:
        df['Mean'] = ((df.iloc[:,1:]).mean(axis=1)).round(3)
        output_df = pd.DataFrame({'ID':df['ID'],'Mean':df['Mean']})
        print(output_df)


if __name__ == '__main__':
    main(sys.argv[1:])
